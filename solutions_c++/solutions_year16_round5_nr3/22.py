#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define fill(x,y) memset(x,y,sizeof(x))
#define prev PREV
                         
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef long double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { re x > 0 ? x : -x; }

const D eps = 1e-10;

int n;
int m;

int x[1000];
int y[1000];
int z[1000];
int vx[1000];
int vy[1000];
int vz[1000];
int mark[1000][1000];
D d[1000][1000];
pair<D, D> seg[1000][1000];
int can[1000][1000];
vector<pair<D, D> > w[1000];
vector<pair<D, D> > u[1000];
priority_queue<pair<D, ii> > all;

pair<D, D> cross (int x, int y, int z, int vx, int vy, int vz, D h) {
	if (vx == 0 && vy == 0 && vz == 0) {
		if (x * x + y * y + z * z < h * h + eps) re mp (-1e50, 1e50);
		re mp (1e50, -1e50);
	}
	D a = vx * vx + vy * vy + vz * vz;
	D b = 2 * (x * vx + y * vy + z * vz);
	D c = x * x + y * y + z * z - h * h;
	D d = b * b - 4 * a * c;
//	printf ("%.10f %.10f %.10f %.10f\n", a, b, c, d);
	if (d < -eps) re mp (1e50, -1e50);
	d = sqrt (d);
	D t1 = (-b - d) / (2 * a);
	D t2 = (-b + d) / (2 * a);
	assert (t1 < t2 + eps);
	re mp (t1, t2);
}

void add (int i, D t1, D t2) {
	for (int l = 0; l < sz (u[i]); l++)
		if (u[i][l].se + eps > t1 && u[i][l].fi < t2 + eps && d[i][l] > max (t1, u[i][l].fi) + eps) {
			d[i][l] = max (t1, u[i][l].fi);
			all.push (mp (-d[i][l], mp (i, l)));
		}
}	

int go (D h) {
//	printf ("%.10f:\n", h);
	for (int i = 0; i < n; i++) w[i].clear ();
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++) {
			pair<D, D> tmp = cross (x[j] - x[i], y[j] - y[i], z[j] - z[i], vx[j] - vx[i], vy[j] - vy[i], vz[j] - vz[i], h);
//			printf ("%d %d = %.10f %.10f\n", i, j, tmp.fi, tmp.se);
			can[i][j] = can[j][i] = 0;
			if (tmp.fi > tmp.se + 1) continue;
			can[i][j] = can[j][i] = 1;
			seg[i][j] = seg[j][i] = tmp;
			w[i].pb (mp (tmp.fi - m, tmp.se));
			w[j].pb (mp (tmp.fi - m, tmp.se));
		}
	for (int i = 0; i < n; i++) {
		sort (all (w[i]));
		u[i].clear ();
		for (int j = 0; j < sz (w[i]);) {
			D a = w[i][j].fi;
			D b = w[i][j].se;
			int k = j;
			while (k < sz (w[i]) && w[i][k].fi < b + eps) {
				b = max (b, w[i][k].se);
				k++;
			}
			u[i].pb (mp (a, b));
			j = k;
		}
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < sz (u[i]); j++) {
			d[i][j] = 1e50;
			mark[i][j] = 0;
		}
	while (!all.empty ()) all.pop ();
	add (0, 0, 0);
	int ok = 0;
	while (!all.empty ()) {
		pair<D, ii> cur = all.top ();
		int x = cur.se.fi;
		int y = cur.se.se;
//		cerr << x << " " << y << " " << d[x][y] << endl;
//		printf ("%d %d = %.10f\n", x, y, d[x][y]);
		if (x == 1) {
			ok = 1;
			break;
		}
		D ct = d[x][y];
		D nt = u[x][y].se + m;
		all.pop ();
		if (mark[x][y]) continue;
		mark[x][y] = 1;
		for (int i = 0; i < n; i++)
			if (can[x][i]) {
				D a = max (ct, seg[x][i].fi);
				D b = min (nt, seg[x][i].se);
				if (a < b + eps) add (i, a, b);
			}
	}
	re ok;	
}

int main () {
	int tt;
	cin >> tt;
	for (int it = 1; it <= tt; it++) {
		scanf ("%d%d", &n, &m);
		for (int i = 0; i < n; i++) scanf ("%d%d%d%d%d%d", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
		D l = 0, r = 1e5;
		for (int it = 0; it < 60; it++) {
			D s = (l + r) / 2;
			if (go (s)) r = s; else l = s;
		}
		cout.precision (15);
		cout << "Case #" << it << ": " << (double)l;
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", it, tt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / it * tt) / CLOCKS_PER_SEC);
	}
	return 0;
}