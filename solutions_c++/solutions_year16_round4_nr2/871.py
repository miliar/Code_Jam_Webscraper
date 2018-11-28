#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <fstream>
#include <cstdio>
using namespace std;

double P[210];
int SZ, K;
#define ZERO 205

double mat[16][16];

double solve(vector<double> V){
	memset(mat,0,sizeof(mat));
	mat[0][0] = 1;
	for(int k = 0; k < K; ++k){
		for(int i = K; i >= 0; --i){
			for(int j = K; j >= 0; --j){
				if(i+j != k+1)continue;
				double t = 0;
				if(i > 0)
					t += mat[i-1][j] * V[k];
				if(j)
					t += mat[i][j-1] * (1-V[k]);
				mat[i][j] += t;
			}
		}
	}
	return mat[K/2][K/2];
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC; ++tc){
		cin >> SZ >> K;
		for(int k = 0; k < SZ; ++k)
			cin >> P[k];
		
		double b = 0;
		for(int i = 1; i < (1<<SZ); ++i){
			if(__builtin_popcount(i) != K)continue;
			vector<double> V;
			for(int j = 0; j < SZ; ++j)
				if((1<<j) & i)
					V.push_back(P[j]);
			b = max(b, solve(V));
		}
		printf("Case #%d: %0.9lf\n", tc, b);
		
		continue;
		sort(P,P+SZ);
		vector<double> V;
		for(int i = 0; i < K/2; ++i){
			V.push_back(P[i]);
			V.push_back(P[SZ-1-i]);
		}
		printf("Case #%d: %0.9lf\n", tc, mat[K/2][K/2]);
	}
	
}

/*




 
*/
