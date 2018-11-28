#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;
void solve(vector< vector<int> >& D,vector< vector< vector<int> > >& A,ofstream& output, int N, int M, int& casenum){
	bool hassol = true;
	for (int i=0; i<100; i++){
		int J = A[i].size();
		for (int j=0; j<J; j++){
			int x = A[i][j][0];
			int y = A[i][j][1];
			int cnt = 0;
			//check row:
			for (int m=0; m<M; m++){
				if (D[x][m]>i+1){
					cnt++; break;
				}
			}
			//check col:
			for (int n=0; n<N; n++){
				if (D[n][y]>i+1){
					cnt++; break;
				}
			}
			if (cnt==2){
				hassol = false; break;
			}
		}
		if (!hassol) break;
	}
	if (hassol)
		output<<"Case #"<<casenum++<<": YES"<<endl;
	else
		output<<"Case #"<<casenum++<<": NO"<<endl;
}
int main(){
	ifstream input("input.txt");
	ofstream output;
	output.open("output.txt");
	if (input.is_open()){
		int numcases = -1;
		int casenum = 1;
		bool dimdata = true;
		int N, M;
		int rowscanned = 0;
		vector< vector<int> > D(100);	
		vector< vector< vector<int> > > A(100);
		while (input.good()){
			string line;
			getline(input, line);
			if (line.size()==0)
				continue;
			istringstream iss(line);
			if (numcases == -1){
				iss>>numcases;
				continue;
			}
			if (dimdata){
				iss>>N;
				iss>>M;
				dimdata = false;
				continue;
			}
			for (int i=0; i<M; i++){
				int t;
				iss>>t;
				D[rowscanned].push_back(t);
				vector<int> coord;
				coord.push_back(rowscanned);
				coord.push_back(i);
				A[t-1].push_back(coord);
			}
			if(++rowscanned==N){
				solve(D,A,output,N,M,casenum);
				rowscanned = 0;
				dimdata = true;
				for (int i=0; i<100; i++){
					D[i].clear();
					A[i].clear();
				}
/*
cout<<"D:"<<N<<"x"<<M<<endl;
for (int i=0; i<N; i++){
	for (int j=0; j<M; j++){
		cout<<D[i][j]<<" ";
	}
	cout<<endl;
}
*/
			}
		}
	}
	input.close();
	output.close();
	return 0;
}

