#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;


#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define y1 y1_gedjcdgfce
#define y0 y0_sadasdasdsa
#define ws ws_sadsadsada
#define left left_asdsadsadsadsa
#define right right_asdasdsadasda
#define hash hash_asdasdasdsad

#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

const int maxn = 23;

int A[maxn], B[maxn];
int X[maxn], V[maxn];
int N;


int go(int L) {
	if (L != 0) {
		int res = 1;
		for (int i = 0; i < L - 1; i++) {
			if (X[i] < X[L - 1]) res = max(res, A[i] + 1);
		}
		if (res != A[L - 1]) return 0;
	}
	if (L == N) {
		for (int i = L - 1; i >= 0; i--) {
			int res = 1;
			for (int j = i + 1; j < N; j++) {
				if (X[i] > X[j]) res = max(res, B[j] + 1);
			}
			if (res != B[i]) return 0;
		}                            
		return 1;
	}
	for (int i = 0; i < N; i++) {
		if (!V[i]) {
            V[i] = 1;
			X[L] = i;
			if (go(L + 1)) return 1;
			V[i] = 0;
		}
	}
	return 0;
}
void solve(int test) {
	scanf("%d", &N);
	memset(V, 0, sizeof V);
	for (int i = 0; i < N; i++) {
		scanf("%d" , &A[i]);
	}
	for (int i = 0; i < N; i++) {
		scanf("%d", &B[i]);
	}	
	assert(go(0) == 1);
	printf("Case #%d: ", test);
	for (int i = 0; i < N; i++) {
		printf("%d%c", X[i] + 1, " \n"[i + 1 == N]);
	}
}
int main(){
	int T; assert(scanf("%d", &T) == 1);
	for (int test = 1; test <= T; test++) {
		solve(test);
		eprintf("test = %d\n", test);
	}	
	return 0;
}
