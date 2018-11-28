#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

int T, TT;
int N, A[2048], B[2048], cnt[2048], ans[2048];
vector<int> LT[2048];

inline void insert(int small, int large) {
	LT[small].push_back(large);
	cnt[large]++;
}

int main() {
	scanf("%d\n", &TT);
	for(int T = 1; T <= TT; ++T) {
		fprintf(stderr, "T = %d\n", T);
		scanf("%d", &N);
		for(int i = 0; i < N; ++i) scanf("%d", &A[i]);
		for(int i = 0; i < N; ++i) scanf("%d", &B[i]);
		memset(cnt, 0, sizeof(cnt));
		memset(ans, -1, sizeof(ans));
		for(int i = 0; i < N; ++i) LT[i].clear();
		for(int i = 0; i < N; ++i) {
			for(int j = i-1; j >= 0; --j) if(A[j] == A[i]-1) {
				insert(j, i);
				break;
			}
			for(int j = i+1; j < N; ++j) if(A[j] == A[i]) {
				insert(j, i);
				break;
			}
		}
		for(int i = N-1; i >= 0; --i) {
			for(int j = i+1; j < N; ++j) if(B[j] == B[i]-1) {
				insert(j, i);
				break;
			}
			for(int j = i-1; j >= 0; --j) if(B[j] == B[i]) {
				insert(j, i);
				break;
			}
		}
		for(int i = 1, j; i <= N; ++i) {
			for(j = 0; j < N; ++j)
				if(cnt[j] == 0 && ans[j] == -1) break;
			ans[j] = i;
			for(vector<int>::iterator itr = LT[j].begin(); itr != LT[j].end(); ++itr) {
				--cnt[*itr];
			}
		}
		printf("Case #%d:", T);
		for(int i = 0; i < N; ++i)
			printf(" %d", ans[i]);
		printf("\n");
	}
}


