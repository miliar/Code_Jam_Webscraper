//label : vector
//By myf
//#pragma comment(linker, "/STACK:16777216")  //C++
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <complex>
#include <list>
#include <iomanip>

#define rep(i, n) for(int i = 0; i < (n); i++)
#define REP(i, l, r) for(int i = (l) ; i < (r); i++)
#define MP make_pair
#define PB push_back
#define Cls(x) memset(x,0,sizeof x)
#define Print(n,x) for(int i=0;i<(n);i++) cout<<x<<" ";cout<<endl;
#define foreach(i,n) for(__typeof(n.begin()) i=n.begin();i!=n.end();i++) //G++
#define F first
#define S second
#define X real()
#define Y imag()
#define Sqr(x) (x)*(x)
#define sign(x) ((x < -EPS) ? -1 : x > EPS)

using namespace std;

typedef long long LL;
typedef complex<double> Point;
typedef Point Vec;
typedef pair<Point, Point> Line;
typedef pair<int, int> pii;
//typedef complex<double> Comp;

const int N = 2010;
const int MD = 1000000007;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
const double EPS = 1E-6;

int n, m, p;
int v[N][4];
int dist[N];
bool del[N];

int work(pii a, pii b, pii c){
	if (a.F == b.F){
		if ((a.S <= c.S && c.S <= b.S) || (a.S >= c.S && c.S >= b.S)){
			return abs(a.F - c.F) - 1;
		}
	}
	else if (a.S == b.S){
		if ((a.F <= c.F && c.F <= b.F) || (a.F >= c.F && c.F >= b.F)){
			return abs(a.S - c.S) - 1;
		}
	}
	return INF;
}

int work(pii a, int id){
	int ret = INF;
	ret = min(ret, work(MP(v[id][0], v[id][1]), MP(v[id][0], v[id][3]), a));
	ret = min(ret, work(MP(v[id][2], v[id][1]), MP(v[id][2], v[id][3]), a));
	ret = min(ret, work(MP(v[id][0], v[id][1]), MP(v[id][2], v[id][1]), a));
	ret = min(ret, work(MP(v[id][0], v[id][3]), MP(v[id][2], v[id][3]), a));
	return ret;
}

int calc(int x, int y){
	int ret = INF;
	rep(i, 2){
		rep(j, 2){
			rep(k, 2){
				rep(l, 2){
					pii a = MP(v[x][2 * i], v[x][2 * j + 1]);
					pii b = MP(v[y][2 * k], v[y][2 * l + 1]);
					ret = min(ret, max(abs(a.F - b.F) - 1, abs(a.S - b.S) - 1));
				}
			}
		}
	}
	rep(i, 2){
		rep(j, 2){
			pii a = MP(v[x][2 * i], v[x][2 * j + 1]);
			pii b = MP(v[y][2 * i], v[y][2 * j + 1]);
			ret = min(ret, work(a, y));
			ret = min(ret, work(b, x));
		}
	}
	return ret;
}

int main(){
	int T;
	scanf("%d", &T);
	rep(cas, T){
		scanf("%d%d%d", &n, &m, &p);
		rep(i, p){
			rep(j, 4){
				scanf("%d", &v[i][j]);
			}
		}
		rep(i, p){
			dist[i] = v[i][0];
			del[i] = false;
		}
		int ans = n;
		rep(i, p){
			int mi = -1;
			rep(j, p){
				if (del[j]) continue;
				if (mi == -1 || mi != -1 && dist[j] < dist[mi]){
					mi = j;
				}
			}
			del[mi] = true;
			rep(j, p){
				if (del[j]) continue;
				dist[j] = min(dist[j], dist[mi] + calc(mi, j));
			}
		}
		rep(i, p){
			ans = min(ans, dist[i] + n - 1 - v[i][2]);
		}
		printf("Case #%d: %d\n", cas + 1, ans);
	}
	return 0;
}
