#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

const int MAXN = 1500;
const int IT = 100;

int n;
double s;
double x[MAXN], y[MAXN], z[MAXN];
double vx[MAXN], vy[MAXN], vz[MAXN];
double d[MAXN][MAXN];

double dist (double x1, double y1, double z1, double x2, double y2, double z2) {
	return sqrt(sqr(x1 - x2) + sqr(y1 - y2) + sqr(z1 - z2));
}

int p[MAXN], rk[MAXN];

int get_p (int x) {
	if (p[x] == x) {
		return x;
	}
	p[x] = get_p(p[x]);
	return p[x];
}

void unite (int x, int y) {
	x = get_p(x);
	y = get_p(y);

	if (x == y) {
		return;
	}

	if (rk[x] < rk[y]) {
		swap(x, y);
	}

	p[y] = x;
	if (rk[x] == rk[y]) {
		rk[x]++;
	}
}

bool check (double x) {
	for (int i = 0; i < n; ++i) {
		p[i] = i;
		rk[i] = 0;
	}

	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			if (d[i][j] < x) {
			 	unite(i, j);
			}
		}
	}

	return (get_p(0) == get_p(1));
}

int main () {
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;

	cout.precision(20);
	for (int ti = 0; ti < tc; ++ti) {
		cin >> n >> s;

		for (int i = 0; i < n; ++i) {
			cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
		}

		for (int i = 0; i < n; ++i) {
			d[i][i] = 0;
			for (int j = i + 1; j < n; ++j) {
				d[i][j] = d[j][i] = dist(x[i], y[i], z[i], x[j], y[j], z[j]);
			}
		}


		double l = 0;
		double r = d[0][1];

		for (int i = 0; i < IT; ++i) {
			double m = (l + r) / 2;
			if (check(m)) {
				r = m;
			} else {
				l = m;
			}
		}

		
        cout << "Case #" << ti + 1 << ": " << (l + r) / 2 << endl;
	}

	return 0;
}
