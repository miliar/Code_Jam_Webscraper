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

using namespace std;

#define REP(i,N) for (int i = 0; i < (N); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORD(i, b, a) for (int i = (b) - 1; i >= a; i--)
#define DP(arg...) fprintf(stderr, ## arg) //COMPILER SPECIFIC!!!

typedef long long ll;
int T;

int R,S;
char M[200][200];

bool to_edge(int r, int s, int dr, int ds) {
	while (true) {
		r += dr;
		s += ds;
		if (r < 0 || s < 0 || r >= R || s >= S)
			return true;
		if (M[r][s] != '.') return false;

	}


}

void solve(int num) {
	scanf("%d%d", &R, &S);
	int sol = 0;
	REP(r,R)
		scanf("%s", M[r]);
	
	REP(r,R) {
		REP(s,S) {
			if (M[r][s] == '.') {
				continue;
			}
			bool is_possible = !(to_edge(r,s,0,1) && to_edge(r,s,1,0) && to_edge(r,s,-1,0)
			&& to_edge(r,s,0,-1));
			if (M[r][s] == '>') {
				if (!to_edge(r,s,0,1)) continue;

			}
			if (M[r][s] == '<') {
				if (!to_edge(r,s,0,-1)) continue;

			}
			if (M[r][s] == 'v') {
				if (!to_edge(r,s,1,0)) continue;

			}
			if (M[r][s] == '^') {
				if (!to_edge(r,s,-1,0)) continue;

			}
			if (is_possible) sol++;
			else goto IMP;
		}

	}

	printf("Case #%d: %d\n", num, sol);
	return;


	IMP:
	printf("Case #%d: IMPOSSIBLE\n", num);

}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		solve(t+1);
	}
	return 0;
}
