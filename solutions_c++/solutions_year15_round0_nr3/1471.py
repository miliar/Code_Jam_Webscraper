#include <iostream>
#include <fstream>
#include <vector>

int quat[4][4] = {
	{ 1, 2, 3, 4},
	{ 2,-1, 4,-3},
	{ 3,-4,-1, 2},
	{ 4, 3,-2,-1}
	};

int multiple (int a, int b) {
	bool pos = true;
	if (a < 0) {
		pos = false;
		a = -a;
	}
	if (b < 0) {
		pos = (pos == false);
		b = -b;
	}
	int product = quat[a-1][b-1];
	if (!pos) product *= -1;
	return product;
}

int get_product(char* str, int len) {
	int prod = 1;
	for (int i = 0;i<len;i++) {
		prod = multiple(prod,str[i]);
	}
	return prod;
}

bool canIjk(char * t, int x, int l) {

	int product = get_product(t,x);
	int unit = 4;
	if (product == 1) {
		return false; 		//ijk = -1
	}
	else if (product == -1) {
		if ((l % 2) == 0) return false;	//ijk = -1
		unit = 2;
	} else {
		if ((l % 4) != 2) return false;
	}
	//ha elég hosszú a sztring
	
	if (l >= 2*unit) {
		
		char* allstr = new char[unit*x];
		for (int j= 0; j<unit;j++) {
			for (int k=0;k<x;k++) {
				allstr[j*x+k] = t[k];
			}
		}
		std::vector<int> is;
		
		int prod = 1;
		for (int j = 0; j < unit *x; j++) {
			prod = multiple(prod,allstr[j]);
			if (prod == 2) {
				is.push_back (get_product(allstr + j +1,unit*x - j-1));
				
			}
		}
		
		
		std::vector<int> ks;
		prod = 1;
		for (int j = 0; j < unit *x; j++) {
			prod = multiple(allstr[unit * x -1 -j],prod);
			if (prod == 4) {
				ks.push_back (get_product(allstr,unit*x - j-1));	
			}
		}
		
		
		int tmp = 1;
		for (int j = 0; j< ((l - 2*unit) % unit );j++) {
			tmp = multiple(tmp,product);
		}
		
		for (unsigned int j = 0; j< is.size();j++) {
			is[j] = multiple (is[j],tmp);
		}
		
		for (unsigned int j = 0; j< is.size();j++) {
			for (unsigned int k = 0; k<ks.size();k++) {
				if (multiple(is[j],ks[k]) == 3) return true;
			}
		}
		
	} else {
		char* allstr = new char[l*x];
		for (int j= 0; j<l;j++) {
			for (int k=0;k<x;k++) {
				allstr[j*x+k] = t[k];
			}
		}
		
		std::vector<int> is;
		
		int prod = 1;
		for (int j = 0; j < l *x; j++) {
			prod = multiple(prod,allstr[j]);
			if (prod == 2 && get_product(allstr+j+1, l*x-1-j) == 2) {
				is.push_back(j);
			}
		}
		
		std::vector<int> ks;
		prod = 1;
		for (int j = 0; j < l *x; j++) {
			prod = multiple(allstr[l * x -1 -j],prod);
			if (prod == 4 && get_product(allstr,l*x - j-1) == 4) {
				ks.push_back (j);	
			}
		}
		
		for (unsigned int j = 0; j< is.size();j++) {
			for (unsigned int k = 0; k<ks.size();k++) {
				if (is[j]+ks[k] +2 < l*x) return true;
			}
		}
		
	}
	
	return false;

}

int main(int argc, char **argv) {
	int n;
	std::ifstream input;
	std::ofstream output;
	input.open("C-small-attempt2.in");
	output.open("out.txt");
	input >> n;
	for (int i = 1;i<=n;i++) {
		int x;
		
		
		
		input >> x;
		
		int l;
		input >> l;
		
		
		char* t = new char[x];
		for (int j=0;j<x;j++) {
			input >> t[j];
			
			t[j] -= ('i' -2);
			
		}
		bool can = canIjk(t,x,l);
	
		output << "Case #" << i << ": " << (can?"YES":"NO") << std::endl;
	
		delete[] t;
	}
    input.close();
	output.close();
	return 0;
}
