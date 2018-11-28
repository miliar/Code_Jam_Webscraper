#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

#include<algorithm>
#include<utility>
#include<string>

#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include <iostream>

using namespace std;

#define FOR(i,N) for (int i = 0; i < (N); i++)
#define FORI(i, a, b) for (int i = (a); i < (b); i++)
#define FORD(i, b, a) for (int i = (b) - 1; i >= a; i--)
#define DP(arg...) fprintf(stderr, ## arg) //COMPILER SPECIFIC!!!


typedef long long ll;

int T, t;
int N, X;
int S[100000];
int M[1000];

void solve() {
	FOR(x,X+1) M[x] = 0;
	FOR(n,N)
		M[S[n]]++;
	
	int res = 0;

	for (int x = 1; x <= X; x++) {
		while (M[x]) {
			M[x]--; res++;
			for (int y = X - x; y >= 1; y--) {
				if (M[y]) { M[y]--; break; }
			}
		}
		
	}

	printf("Case #%d: %d\n", t, res);
}

int main() {
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d%d", &N, &X);
		FOR(n,N)
			scanf("%d", &S[n]);
		solve();
	}
	return 0;
}
