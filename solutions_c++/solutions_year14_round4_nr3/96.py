#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int MAXN = 1005;
const int INF = 1e9;

struct Point {
    int x, y;
    Point() {}
    Point(int x, int y) : x(x), y(y) {}
};

Point p[MAXN][4];
int n;

void addRect(int x0, int y0, int x1, int y1) {
    p[n][0] = Point(x0, y0);    
    p[n][1] = Point(x1, y0);    
    p[n][2] = Point(x1, y1);    
    p[n][3] = Point(x0, y1);
    n++;   
}

int dist(Point& a, Point &b) {
	return max(abs(a.x - b.x), abs(a.y - b.y));
}

int dist(Point& p, Point& a, Point& b) {
	if (a.x == b.x) {
		if (p.y >= min(a.y, b.y) && p.y <= max(a.y, b.y)) return abs(p.x - a.x);
		return min(dist(a, p), dist(b, p));
	}
	if (p.x >= min(a.x, b.x) && p.x <= max(a.x, b.x)) return abs(p.y - a.y);
		return min(dist(a, p), dist(b, p));
}

int calcDist(int u, int v) {
    int ret = INF;
	forn(i, 4) {
		forn(j, 4) {
			ret = min(ret, dist(p[u][i], p[v][j], p[v][(j + 1) % 4]));
			ret = min(ret, dist(p[v][i], p[u][j], p[u][(j + 1) % 4]));
			ret = min(ret, dist(p[u][i], p[v][j]));
		}
	}
	return ret;
}

int d[MAXN];
bool used[MAXN];

void solve(int tc) {
    cerr << "Case #" << tc << ", " << clock() << " ms.\n";
    cout << "Case #" << tc << ": ";
    int w, h, b;
    cin >> w >> h >> b;
    n = 0;
    addRect(0, 0, 0, h);
    forn(i, b) {
        int x0, y0, x1, y1;
		cin >> x0 >> y0 >> x1 >> y1;
        addRect(x0, y0, x1 + 1, y1 + 1);
    }
    addRect(w, 0, w, h);
    memset(used, 0, sizeof(used));
    fill(d, d + n, INF);
    d[0] = 0;
    forn(it, n) {
        int m = -1;
        forn(i, n) {
            if (!used[i] && (m == -1 || d[m] > d[i])) m = i;
        }
        used[m] = true;
        forn(i, n) {
            if (!used[i] && d[i] > d[m] + calcDist(m, i)) {
                d[i] = d[m] + calcDist(m, i);
            }
        }
    }
    cout << d[n - 1] << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
