#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <fstream>
#include <cstdio>
using namespace std;


int mat[4][4];
int alr[4][4];
int taken[4];
int N;

int can(vector<int> &V, int id = 0){
	
	if(id == N)return 1;
	int v = V[id];
	int f = 0;	
	for(int i = 0; i < N; ++i){
		if(mat[v][i] && !taken[i]){
			taken[i] = 1;
			f = 1;
			if(!can(V,id+1)) 
				return 0;
			taken[i] = 0;
		}
	}
	return f;
	
}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC; ++tc){
		cin >> N;
		int b = N*N;
		for(int i = 0; i < N; ++i){
			string S; cin >> S;
			for(int j = 0; j < N; ++j){
				alr[i][j] = S[j]-'0';
			}
		}
		for(int m = 0; m < (1<<(N*N)); ++m){
			int col = 0;
			for(int i = 0; i < N; ++i){
				for(int j = 0; j < N; ++j){
					mat[i][j] = ((m >> (i*N)) >> (j)) & 1;
					if(mat[i][j] && alr[i][j])
						col = 1;
				}
			}
			if(col)continue;
			for(int i = 0; i < N; ++i){
				for(int j = 0; j < N; ++j){
					mat[i][j] |= alr[i][j];
				}
			}
			vector<int> V;
			for(int i = 0; i < N; ++i)
				V.push_back(i);
			int all = 1;
			do{
				memset(taken,0,sizeof(taken));
				all &= can(V);
				
			}while(next_permutation(V.begin(),V.end()));
			if(all){
//				for(int i = 0; i < N; ++i){
//					for(int j = 0; j < N; ++j){
//						cout << mat[i][j] << " ";
//					}
//					cout << endl;
//				}
//				cout << m << " " << __builtin_popcount(m) << endl;
				b = min(b, (int)__builtin_popcount(m));
			}
		}
		cout << "Case #" << tc << ": " << b << endl;
	}
	
}

/*




 
*/
