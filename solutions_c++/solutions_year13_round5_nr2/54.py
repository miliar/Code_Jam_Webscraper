#include <sstream>
#include <iomanip>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair

#define DEBUG(x) cout << #x << " = "; cout << x << endl;
#define PR(a,n) cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl;
#define PR0(a,n) cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl;
using namespace std;

//Buffer reading
int INP,AM,REACHEOF;
#define BUFSIZE (1<<12)
char BUF[BUFSIZE+1], *inp=BUF;
#define GETCHAR(INP) { \
    if(!*inp) { \
        if (REACHEOF) return 0;\
        memset(BUF,0,sizeof BUF);\
        int inpzzz = fread(BUF,1,BUFSIZE,stdin);\
        if (inpzzz != BUFSIZE) REACHEOF = true;\
        inp=BUF; \
    } \
    INP=*inp++; \
}
#define DIG(a) (((a)>='0')&&((a)<='9'))
#define GN(j) { \
    AM=0;\
    GETCHAR(INP); while(!DIG(INP) && INP!='-') GETCHAR(INP);\
    if (INP=='-') {AM=1;GETCHAR(INP);} \
    j=INP-'0'; GETCHAR(INP); \
    while(DIG(INP)){j=10*j+(INP-'0');GETCHAR(INP);} \
    if (AM) j=-j;\
}
//End of buffer reading

struct Point {
	long long x, y;
	int id;
	Point() { x = y = 0; }
	Point(ll x, ll y) : x(x), y(y) {}
	
	Point operator - (Point a) { return Point(x-a.x, y-a.y); }
	long long operator % (Point a) { return x*a.y - y*a.x; } // cross product
	
	long double sqlen() { return sqrt(x*x + y*y); }
};
int n;

typedef vector< Point > Polygon;
Polygon cur, all, save;
long long best;

long long ab(long long x) {
	if (x < 0) return -x;
	else return x;
}

long long area(Polygon &p) {
   long long s = 0;
   FOR(i,1,(int)p.size()-1) s+= (p[i]-p[0])%(p[(i+1)%p.size()]-p[0]);
   return ab(s);
}

int ccw(Point a, Point b, Point c) {
	long long t = (b-a)%(c-a);
	if (t == 0) return 0;
	else if (t < 0) return -1;
	else return 1;
}

bool good() {
	REP(i,cur.size()) {
		int j = i + 1; if (j == cur.size()) j = 0;
		FOR(u,i+1,cur.size()-1) {
			int v = u + 1; if (v == cur.size()) v = 0;
			
			if (ccw(cur[i], cur[j], cur[u]) * ccw(cur[i], cur[j], cur[v]) < 0
					&& ccw(cur[u], cur[v], cur[i]) * ccw(cur[u], cur[v], cur[j]) < 0)
				return false;
		}
		
		REP(u,n) if (u != i && u != j) {
			if (ccw(cur[i], cur[j], cur[u]) == 0 && (cur[u] - cur[i]).sqlen() + (cur[u] - cur[j]).sqlen() < (cur[i] - cur[j]).sqlen() + 0.5)
				return false;
		}
	}
	return true;
}

bool used[11];
void attempt(int turn) {
	if (turn > n) {
		if (area(cur) > best && good()) {
			save = cur;
			best = area(cur);
		}
		return ;
	}
	
	REP(i,n) if (!used[i]) {
		used[i] = true; cur.PB(all[i]);
		
		attempt(turn+1);
		
		cur.pop_back();
		used[i] = false;
	}
}

int main() {
    // freopen("input.txt", "r", stdin);
	int ntest; cin >> ntest;
	FOR(test,1,ntest) {
		cerr << test << endl;
		cin >> n;
		all.clear();
		FOR(i,1,n) {
			Point P; cin >> P.x >> P.y;
			P.id = i-1;
			all.PB(P);
		}
		
		memset(used, false, sizeof used);
		best = -1;
		cur.clear();
		cur.push_back(all[0]);
		used[0] = true;
		attempt(2);
		
		cout << "Case #" << test << ":";
		REP(i,save.size()) cout << ' ' << save[i].id;
		cout << endl;
	}
    return 0;
}
