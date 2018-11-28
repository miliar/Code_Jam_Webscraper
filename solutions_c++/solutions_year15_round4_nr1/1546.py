#include <functional>
#include <algorithm>
#include <iostream>
#include <climits>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

typedef long long        LL;
typedef pair<int, int>   pii;
typedef pair<int, pii>   piii;
typedef vector<int>      vi;
typedef vector<pii>      vii;
typedef vector<piii>     viii;

#ifdef _WIN32
#define getchar_unlocked getchar
#endif
inline void inpint( int &n ) {
  n=0; register int ch = getchar_unlocked(); bool sign = 0;
  while(ch < 48 || ch > 57) { if(ch == '-') sign = 1; ch = getchar_unlocked(); }
  while(ch >= 48 && ch <= 57) { n = (n << 3) + (n << 1) + ch - 48, ch = getchar_unlocked(); }
  if(sign) n = -n;
}

inline int sqr(int x){return x * x;}
inline int cube(int x){return x * x * x;}
inline LL sqrLL(LL x){return x * x;}
inline LL cubeLL(LL x){return x * x * x;}

const LL LLINF      = 9223372036854775807LL;
const LL LLINF17    = 100000000000000000LL;
const int INF       = 2147483647;
const int INF9      = 1000000000;
const int MOD       = 1000000007;
const double eps    = 1e-7;
const double PI     = acos(-1.0);

#define FOR(a,b,c)   for (int (a)=(b); (a)<(c); (a)++)
#define FORN(a,b,c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a,b,c)  for (int (a)=(b); (a)>=(c); (a)--)
#define REP(i,n)     FOR(i,0,n)
#define REPN(i,n)    FORN(i,1,n)
#define REPD(i,n)    FORD(i,n,1)

#define RESET(a,b)   memset(a,b,sizeof(a)) 
#define SYNC         ios_base::sync_with_stdio(0);
#define SIZE(a)      (int)(a.size())
#define MIN(a,b)     (a) = min((a),(b))
#define MAX(a,b)     (a) = max((a),(b))
#define ALL(a)       a.begin(),a.end()
#define RALL(a)      a.rbegin(),a.rend()
#define SIZE(a)      (int)(a.size())
#define LEN(a)       (int)(a.length())

#define fi           first
#define se           second
#define pb           push_back
#define mp           make_pair

int dr[] = {1,0,-1,0,-1,1,1,-1};
int dc[] = {0,-1,0,1,1,1,-1,-1};
int t, r, c;
char arr[105][105],tmp[105][105];
bool flag[105][105][4], bad[105][105];
char ch[] = {'^','>','v','<'};
int pos[250], row[105], col[105];
vii v;
inline int check(bool sec) {
	RESET(flag,0);
	int prev = -1, px, py, lx, ly;
	REPN(i,r) {
		REPN(j,c) {
			int posx = i, posy = j;
			int cnt = 0;
			if (arr[i][j] == '.') continue;
			while (1) {
				if (posx < 1 || posx > r || posy < 1 || posy > c) {
					break;
				}
				px = posx, py = posy;

				if (arr[posx][posy] != '.') {
					lx = posx, ly = posy;
				}

				if (arr[posx][posy] == '^') posx -= 1, prev = 0;
				else if (arr[posx][posy] == '>') posy += 1, prev = 1;
				else if (arr[posx][posy] == '<') posy -= 1, prev = 2;
				else if (arr[posx][posy] == 'v') posx += 1, prev = 3;
				else if (arr[posx][posy] == '.') {
					if (prev == 0) posx -= 1;
					else if (prev == 1) posy += 1;
					else if (prev == 2) posy -= 1;
					else if (prev == 3) posx += 1;
				}
				if (flag[posx][posy][prev]) break;
				flag[posx][posy][prev] = 1;
			}
			if (posx < 1 || posx > r || posy < 1 || posy > c) {
				bad[lx][ly] = 1;
			}
		}
	}
	return 1;
}

int main(){
	pos['^'] = 0;
	pos['>'] = 1;
	pos['v'] = 2;
	pos['<'] = 3;

	scanf("%d",&t);
	REPN(tc,t) {
		scanf("%d %d",&r,&c);
		RESET(row,0);
		RESET(col,0);
		RESET(flag,0);
		REPN(i,r) {
			REPN(j,c) {
				cin >> arr[i][j];
				tmp[i][j] = arr[i][j];
				bad[i][j] = 0;
				if (arr[i][j] != '.') row[i]++, col[j]++;
			}
		}

		printf("Case #%d: ",tc);
		
		v.clear();
		check(0);
		bool can = 1;
		REPN(i,r) {
			REPN(j,c) {
				if (bad[i][j]) {
					if (row[i] == 1 && col[j] == 1) can = 0;
				}
			}
		}
		if (!can) puts("IMPOSSIBLE");
		else {
			int ans = 0;
			REPN(i,r) REPN(j,c) ans += bad[i][j];
			printf("%d\n",ans);
		}
	}
	return 0;
}