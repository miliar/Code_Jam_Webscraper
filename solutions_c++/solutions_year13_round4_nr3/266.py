#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int A[2][2200];
int T[2][2200];
int R[2200];

int TT[2][2200];
int TR[2200];

int N;

int bit[2][2200];

void add(int k, int i, int v) {
	for (; i <= N; i += i & -1) bit[k][i] += v;
}


int main(){
	int tc, tcn;
	scanf("%d", &tcn);
	for(tc=0; tc<tcn; ++tc){
		printf("Case #%d:", tc+1);
		scanf ("%d", &N);
		for(int i=0; i<N; ++i){
			scanf("%d", &A[0][i]);
		}
		for(int i=0; i<N; ++i){
			scanf("%d", &A[1][i]);
			T[0][i] = T[1][i] = 1;
			R[i] = 0;
		}

		for(int k=0; k<N; ++k){
			int j;
			for(j=0; j<N; ++j){
				if(A[0][j] == T[0][j] && A[1][j] == T[1][j] && R[j] == k){
					for(int i=0; i<N; ++i){
						if(R[i] == k && i!=j){
							TR[i] = k+1;
						}else{
							TR[i] = R[i];
						}
					}
					int maxi = 0;
					for(int i=0; i<N; ++i){
						if(TR[i] == k+1){
							TT[0][i] = maxi + 1;
						}else{
							TT[0][i] = T[0][i];
							maxi = max(maxi, TT[0][i]);
						}
						if(TT[0][i] > A[0][i])
							goto next;
					}
					maxi = 0;
					for(int i=N; i --> 0;){
						if(TR[i] == k+1){
							TT[1][i] = maxi + 1;
						}else{
							TT[1][i] = T[1][i];
							maxi = max(maxi, TT[1][i]);
						}
						if(TT[1][i] > A[1][i])
							goto next;
					}
					for(int i=0; i<N; ++i){
						T[0][i] = TT[0][i];
						T[1][i] = TT[1][i];
						R[i] = TR[i];
					}
					break;
				}
next:
				;
			}
			/*
			if(j == N){
				for(int i=0; i<N; ++i){
					printf("%d %d %d %d %d\n", T[0][i], A[0][i], R[i], T[1][i], A[1][i]);
				}
				return 1;
			}
			*/
		}

		for(int i=0; i<N;  ++i){
			printf(" %d", R[i] + 1);
		}
		puts("");
	}
}
