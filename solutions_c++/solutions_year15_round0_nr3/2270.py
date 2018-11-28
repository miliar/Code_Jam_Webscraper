#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

char multiply(char c, char i, int& s){
	if (c=='1')
		return i;
	else if (c=='i' && i=='i'){
		s = -s;
		return '1';
	}else if (c=='i' && i=='j'){
		return 'k';
	}else if (c=='i' && i=='k'){
		s=-s;
		return 'j';
	}else if  (c=='j' && i=='i'){
		s=-s;
		return 'k';
	}else if (c=='j' && i=='j'){
		s=-s;
		return '1';
	}else if (c=='j' && i=='k'){
		return 'i';
	}else if (c=='k' && i=='i'){
		return 'j';
	}else if (c=='k' && i=='j'){
		s=-s;
		return 'i';
	}else if (c=='k' && i=='k'){
		s=-s;
		return '1';
	}
	else
		return 'x';
}



char evaluate(vector<char> v){
	char c='1';
	int sign=1;
	for(int i=0; i<v.size();i++){
		c = multiply(c, v[i], sign);
	}
	if(sign==1)
		return c;
	else 
		return sign;
}


int main(){
	ifstream fin("C-small-attempt1.in.txt");
	ofstream fout("small.txt");
	//ifstream fin("simple.txt");
	//ofstream fout("s.txt");
	string line;
	getline(fin, line);
	int cases = stoi(line);
	for(int i=1;i<=cases;i++){
		fout << "Case #" << i <<": ";
		vector<char> v;
		int L, X;
		fin >> L >> X;
		//read input
		for(int i=0;i<L;i++){
			char c;
			fin>>c;
			v.push_back(c);
		}
		//duplicate input X times
		vector<char> f;
		for(int i=0;i<X;i++){	
			for(int j=0;j<L;j++){
				f.push_back(v[j]);
			}
		}

		bool right = false;
		char t = 'i';
		int correct =0;
		char c='1';
		int sign=1;
		int k=0;
		for(; k<f.size()-1;k++){
			c = multiply(c, f[k], sign);
			if(c == t && sign == 1){
				correct++;
				c = '1';
				if(t=='i')
					t = 'j';
				else
					break;
			}

		}
		if (correct!=2)
			fout << "NO" << endl;
		else{
			t = 'k';
			if (evaluate( vector<char>(f.begin()+k+1, f.end()))=='k')
				fout << "YES" << endl;
			else
				fout << "NO" << endl;
		}

	}

	return 0;
}