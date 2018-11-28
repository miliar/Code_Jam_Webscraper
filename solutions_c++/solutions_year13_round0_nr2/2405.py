#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)

using namespace std;
int T;
int N,M;

 int main(){
	ifstream in("A.txt");  
	ofstream out("resultado.txt");
	in >> T;
	cout << "T = " << T << endl;
	for(int test =1; test<=T; test++){

		in >> N >> M;
		vector< vector<int> > L(N, vector<int> (M+1));

		for(int i = 0; i<N; i++){
			for(int j = 0; j<M; j++){
				in >> L[i][j];
			}
		}

		vector<int> maxR(N,-99999),minR(N,99999);
		for(int i = 0; i<N; i++){
			for(int j = 0; j<M; j++){
				maxR[i] = MAX(maxR[i], L[i][j]);
				minR[i] = MIN(minR[i], L[i][j]);
			}
		}

		
		vector<int> maxC(M,-99999),minC(M,99999);
		for(int i = 0; i<M; i++){
			for(int j = 0; j<N; j++){
				maxC[i] = MAX(maxC[i], L[j][i]);
				minC[i] = MIN(minC[i], L[j][i]);
			}
		}

		bool can = true;
		for(int i = 0; i<N; i++)
			for(int j = 0; j<M; j++){
				if(L[i][j] < maxR[i] && L[i][j] < maxC[j]){
					can = false;
				}
			}

		out << "Case #" << test << ": ";
		cout << "Case #" << test << ": ";		
		if(can){
			cout << "YES" << endl;
			out << "YES" << endl;
		}
		else{
			cout << "NO" << endl;
			out << "NO" << endl;
		}
	}
	return 0;
 }
    