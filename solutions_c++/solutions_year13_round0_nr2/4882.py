#include<iostream>
#include<fstream>
#include<algorithm>
#include<cmath>

using namespace std;
int N, M;
int mat[110][110];
int V[110];
int H[110];


void maxes(){
	for(int i = 0; i < N; i++){
		int m = 0;
		for(int j = 0; j < M; j++){
			m = max(m, mat[i][j]);	
		}
		H[i] = m;
	}
	
	for(int j = 0; j < M; j++){
		int m = 0;
		for(int i = 0; i < N; i++){
			m = max(m, mat[i][j]);	
		}
		V[j] = m;	
	}
}

bool good(){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if(mat[i][j] < V[j] && mat[i][j] < H[i]) return false;	
		}
	}
	return true;
}


int main(){
	ifstream infile;
	ofstream ofile;
	infile.open ("test.txt");
	ofile.open("out.txt");
	int t, cases = 0;
	infile >> t;
	while(cases++ < t){
		infile >> N >> M;
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				infile >> mat[i][j];
			}
		}
		maxes();
		
		ofile << "Case #" << cases << ": ";
		if(good()) ofile << "YES\n";
		else ofile << "NO\n";
	}// while more inputs
	
	infile.close();
	ofile.close();
	return 0;
}