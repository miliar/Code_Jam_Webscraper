#include<stdio.h>
#include<string.h>
#include<list>
using namespace std;

#define NK 200

int T, TT, N;
int K[256], R[256], A[256];
char used[256], vst[256];
list<int> containKey[256], needKey[256], inChest[256];

inline bool hasPath(int k) {
	if(vst[k]) return false;
	if(K[k] > 0) return true;
	vst[k] = 1;
	list<int>::iterator itr;
	for(itr = containKey[k].begin(); itr != containKey[k].end(); ++itr)
		if(!used[*itr] && hasPath(R[*itr])) return true;
	return false;
}

inline bool possible(int k) {
	list<int>::iterator itr;
	bool empty = true;
	for(itr = needKey[k].begin(); itr != needKey[k].end(); ++itr)
		if(!used[*itr]) { empty = false; break; }
	if(empty) return true;
	memset(vst, 0, sizeof(vst));
	return hasPath(k);
}

inline void take(int x, int v) {
	used[x] += v;
	K[R[x]] -= v;
	list<int>::iterator itr;
	for(itr = inChest[x].begin(); itr != inChest[x].end(); ++itr) K[*itr] += v;
}

int main() {
	scanf("%d", &TT);
	for(T = 1; T <= TT; ++T) {
		for(int i = 1; i <= NK; ++i)
			containKey[i].clear(), needKey[i].clear(), K[i] = 0;
		int nK;
		scanf("%d %d", &nK, &N);
		for(int t; nK > 0; --nK) {
			scanf("%d", &t);
			K[t]++;
		}
		for(int i = 0, k, n; i < N; ++i) {
			used[i] = 0;
			inChest[i].clear();
			scanf("%d %d", &k, &n);
			R[i] = k;
			needKey[k].push_back(i);
			for(int t; n > 0; --n) {
				scanf("%d", &t);
				inChest[i].push_back(t);
				containKey[t].push_back(i);
			}
		}
		char ok = 1;
		for(int i = 0, j; i < N && ok; ++i) {
			for(j = 0; j < N; ++j) if(!used[j] && K[R[j]] > 0) {
				take(j, 1);
				if(K[R[j]] > 1) break;
				if(possible(R[j])) break;
				take(j, -1);
			}
			if(j == N) ok = 0;
			else A[i] = j;
		}
		printf("Case #%d:", T);
		if(!ok) puts(" IMPOSSIBLE");
		else {
			for(int i = 0; i < N; ++i)
				printf(" %d", A[i]+1);
			puts("");
		}
	}
}

