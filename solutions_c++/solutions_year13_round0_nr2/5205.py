#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int lawn[101][101] = {0};
int M = 100;
int N = 100;
int T = 100;
string out = "YES";

int main()
{
	fin >> T;
	for(int i = 0; i < T; i++){
		fin >> N >> M;
		out = "YES";
		for(int j = 0; j < N; j++){ lawn[j][M] = 0;}
	    for(int j = 0; j < M; j++){ lawn[N][j] = 0;}
	    for(int j = 0; j < N; j++){
		    for(int k = 0; k < M; k++){
			    fin >> lawn[j][k];
			    if(lawn[j][k] > lawn[j][M]){
			    	lawn[j][M] = lawn[j][k];
			    }
			    if(lawn[j][k] > lawn[N][k]){
				    lawn[N][k] = lawn[j][k];
			    }
		    }
	    }
	    for(int j = 0; j < N; j++){
		    for(int k = 0; k < M; k++){
			    if(lawn[j][k] < lawn[j][M] && lawn[j][k] < lawn[N][k]){
                    out = "NO"; break;
				}
			}
			if("NO"==out) break;
	    }
		fout <<"Case #" << i+1 <<": "<< out;
		if(i < T-1) fout << endl;
	}
	return 1;
}