#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;



bool divide(vector<int> cakes, int max){
	bool divi = false;
	int m = *std::max_element(cakes.begin(),cakes.end());
	int n = 0;
	std::vector<int>::iterator position = std::find(cakes.begin(), cakes.end(), m);
	while(position != cakes.end()){
		n++;
		cakes.erase(position);
		position = std::find(cakes.begin(), cakes.end(), m);
	}
	if(m <= max)
		return false;
	else if ((m+1)/2 + 1*n < m) 
		return true;
	else 
		return false; 
	// else{
	// 	int i = 2;
	// 	int count = 1;
	// 	while ( (m + i-1)/i + (i-1)*n  <   (m+count-1)/count + (count -1)*n ){
	// 		i++;
	// 		count++;
	// 	}	
	// 	return count==1;
	// }
}


int update(int m, int n){
	int i = 2;
	int count = 1;
	while ( (m + i-1)/i + (i-1)*n  <   (m+count-1)/count + (count -1)*n ){
		i++;
		count++;
	}
	return count;
}


int main(){
	ifstream fin("B-small-attempt3.in.txt");
	//ifstream fin("simple.txt");
	//ofstream fout("s.txt");
	ofstream fout("small.txt");
	//ofstream fout("s.txt");
	string line;
	getline(fin, line);
	int cases = stoi(line);
	for(int i=1;i<=cases;i++){
		fout << "Case #" << i <<": ";
		int p;
		fin >> p;
		int total =0;
		std::vector<int> cakes;
		for (int j=0;j<p;j++){
			int n;
			fin >> n;
			total += n;
			cakes.push_back(n);
		}
		int num = *std::max_element(cakes.begin(),cakes.end());
		for(int i=cakes.size();i<=total;i++){
			int avg = (total+i-1) /i;
			int n = 0;
			for(int j=0;j<cakes.size();j++){
				n += (cakes[j] + avg -1)/avg - 1;
			}
			n += avg;
			if (n < num)
				num = n;
		}
		fout << num << endl;
	}
}