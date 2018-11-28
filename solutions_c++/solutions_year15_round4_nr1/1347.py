/* DIKRA */
/* DELAPAN.3gp */
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <utility>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;

#ifdef DEBUG
	#define debug(...) printf(__VA_ARGS__)
	#define GetTime() fprintf(stderr,"Running time: %.3lf second\n",((double)clock())/CLOCKS_PER_SEC)
#else
	#define debug(...) 
	#define GetTime() 
#endif

//type definitions
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
typedef vector<int> vint;

//abbreviations
#define A first
#define B second
#define MP make_pair
#define PB push_back

//macros
#define REP(i,n) for (int i = 0; i < (n); ++i)
#define REPD(i,n) for (int i = (n)-1; 0 <= i; --i)
#define FOR(i,a,b) for (int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for (int i = (a); (b) <= i; --i)
#define FORIT(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) ((int)(a).size())
#define RESET(a,x) memset(a,x,sizeof(a))
#define EXIST(a,s) ((s).find(a) != (s).end())
#define MX(a,b) a = max((a),(b));
#define MN(a,b) a = min((a),(b));

inline void OPEN(const string &s) {
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

/* -------------- end of DELAPAN.3gp's template -------------- */

int ntc;
char s[105][105];
int vis[105][105];
int ans;
int num;
int impossibru;
int dir;
int row, col;

int rm[] = {0,0,1,-1};
int cm[] = {1,-1,0,0};

int ff(int r, int c){
	if (r < 0 || r >= row || c < 0 || c >= col) return 1;
	if (s[r][c] != '.' && vis[r][c]) return 0;

	vis[r][c] = 1;
	if (s[r][c] == '^') dir = 3;
	else if (s[r][c] == 'v') dir = 2;
	else if (s[r][c] == '<') dir = 1;
	else if (s[r][c] == '>') dir = 0;

	return ff(r + rm[dir], c + cm[dir]);
}

int main(){
	scanf("%d", &ntc);
	FOR(itc, 1, ntc){
		scanf("%d %d", &row, &col);
		REP(i, row) scanf("%s", s[i]);

		// printf("\nCase %d\n", itc);
		// REP(i, row) printf("%s\n", s[i]);

		RESET(vis, 0);
		ans = 0;

		impossibru = 0;
		REP(i, row){
			REP(j, col){
				if (s[i][j] == '.') continue;

				int flag = 0;
				REP(k, col){
					if (k == j) continue;
					if (s[i][k] != '.') flag = 1;
				}
				REP(k, row){
					if (k == i) continue;
					if (s[k][j] != '.') flag = 1;
				}

				if (flag == 0){
					impossibru = 1;
					break;
				}
			}
			if (impossibru) break;
		}

		if (impossibru){
			printf("Case #%d: IMPOSSIBLE\n", itc);
			continue;
		}

		REP(i, row){
			REP(j, col){
				if (vis[i][j]) continue;
				if (s[i][j] == '.') continue;

				if (s[i][j] == '^') dir = 3;
				else if (s[i][j] == 'v') dir = 2;
				else if (s[i][j] == '<') dir = 1;
				else if (s[i][j] == '>') dir = 0;
				else assert(false);

				ans += ff(i, j);
			}
			if (impossibru) break;
		}



		printf("Case #%d: %d\n", itc, ans);
	}
	return 0;
}
