#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

char maxelem(vector<char> &vec){
	return *max_element(vec.begin(),vec.end());
}


int main(int argc, char ** argv){
	ifstream fin (argv[1]);
	
	unsigned int T;
	fin >> T;
	for(unsigned int t = 0; t != T; t++){
		unsigned int N,M;
		fin >> N >> M;
		vector<vector<char> > lawn (N, vector<char> (M));
		vector<vector<char> > lawntrans (M, vector<char> (N));

		for(unsigned int n = 0; n != N; n++){
			for(unsigned int m = 0; m != M; m++){
				int a;
				fin >> a;
				lawn[n][m] = a;
				lawntrans[m][n] = a;
			}
		}

		vector<char> lawnN (N);
		vector<char> lawnM (M);
		transform(lawn.begin(), lawn.end(), lawnN.begin(), maxelem);
		transform(lawntrans.begin(), lawntrans.end(), lawnM.begin(), maxelem);


		bool possible = true;
		for(unsigned int n = 0; n != N && possible; n++){
			for(unsigned int m = 0; m != M && possible; m++){
				if (lawn[n][m] < min(lawnN[n],lawnM[m])){
					possible = false;
				}
			}
		}




		cout << "Case #" << t+1 << ": ";
		if (possible)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
	return 0;
}
