#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>
#include <iomanip>

using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()
#define mp(a,b) make_pair((a),(b))

#define RESET(c,x) memset (c, x, sizeof (c))

#define oo 1000111000

#define PI acos(-1.0)
#define fi first
#define se second
#define SIZE(c) (c).size()


typedef vector<int> VI ;
typedef vector<string> VS ;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;

template<class T> inline int size(const T&c) { return c.size(); }

using namespace std;
int fastMax(int x, int y) { return (((y-x)>>(32-1))&(x^y))^y; }
int fastMin(int x, int y) { return (((y-x)>>(32-1))&(x^y))^x; }

const int maxn = 110;

const int hy[4] = {-1, 0, 1, 0};
const int hx[4] = {0, -1, 0, 1};
int T;
int n,m;
int y,x;
int dy,dx;
string st;
char a[maxn][maxn];

bool test(int y, int x, int dy, int dx) {
	bool ok = false;
	int yy = y;
	int xx = x;

	while (yy + dy >= 0 && yy + dy < n && xx + dx >= 0 && xx + dx < m) {
		yy += dy;
		xx += dx;
		if (a[yy][xx] != '.') {
			ok = true;
			break;
		}
	}
	return ok;
}

int main()
{
    freopen("A-large.in.txt","r",stdin);
    freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int t = 1; t <= T; t++) {
		scanf("%d%d",&n,&m);
		for (int i = 0; i < n; i++) {
			cin>>st;
			for (int j = 0; j < m; j++) {
				a[i][j] = st[j];
			}
		}
		int res = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int y = i;
				int x = j;
				if (a[y][x] != '.') {
					if (a[y][x] == '<') {
						dy = 0;
						dx = -1;
					}
					if (a[y][x] == '>') {
						dy = 0;
						dx = 1;
					}
					if (a[y][x] == '^') {
						dy = -1;
						dx = 0;
					}
					if (a[y][x] == 'v') {
						dy = 1;
						dx = 0;
					}
					if (test(y, x, dy, dx) == false) {
						bool found = false;
						for (int j = 0; j < 4; j++) {
							if (test(y, x, hy[j], hx[j])) {
								res++;
								found = true;
								break;
							}
						}
						if (found == false) {
							res = -1;
							break;
						}
					}
				}
			}
			if (res == -1) break;
		}
		if (res == -1) {
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		} else 
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
    fclose(stdin);
    fclose(stdout);
    return 0;
}