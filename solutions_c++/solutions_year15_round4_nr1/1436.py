#include <bits/stdc++.h>
#define REP(x,n)  for(int x=0;x<(int)(n);x++)
#define RREP(x,n) for(int x=(int)(n)-1;x>=0;--x)
#define FOR(x,m,n) for(int x=(int)m;x<(int)(n);x++)
#define EACH(itr, cont) for(typeof((cont).begin()) itr = (cont).begin(); itr != (cont).end(); ++itr)
#define ALL(X)    (X).begin(),(X).end()
#define mem0(X)    memset((X),0,sizeof(X))
#define mem1(X)    memset((X),255,sizeof(X))

using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
const int ERROR = 100 * 100 + 5;
const int NOTCHECKED = 100 * 100 * 100 + 5;
void dostuff() {
	int R, C, change = 0;
	scanf("%i%i", &R, &C);
	vector<string> M(R);
	REP(r, R) cin >> M[r];

	REP(i, R)REP(j, C) if (M[i][j] != '.') {
		int need = ERROR;
		for (int r = i + 1; r < R; ++r) if (M[r][j] != '.') {
				int cur = 1;
				if (M[i][j] == 'v')cur = 0;
				need = min(need, cur);
			}
		for (int r = i - 1; r >= 0; --r) if (M[r][j] != '.') {
				int cur = 1;
				if (M[i][j] == '^')cur = 0;
				need = min(need, cur);
			}
		for (int c = j + 1; c < C; ++c) if (M[i][c] != '.') {
				int cur = 1;
				if (M[i][j] == '>')cur = 0;
				need = min(need, cur);
			}
		for (int c = j - 1; c >= 0; --c) if (M[i][c] != '.') {
				int cur = 1;
				if (M[i][j] == '<')cur = 0;
				need = min(need, cur);
			}
		if (need == ERROR) {printf("IMPOSSIBLE\n"); return;}
		change += need;
	}
	printf("%i\n", change);
}


int main() {
	int T;
	scanf("%i", &T);
	REP(t, T) printf("Case #%i: ", t + 1), dostuff();
}