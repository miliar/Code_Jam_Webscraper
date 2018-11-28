#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

#define mp(a,b) make_pair(a,b)

long double b[105];
long double a[105];
double r[105];
double c[105];

long double x[105];

// max{cx | Ax <= b, x >= 0}
const long double kEps = 1e-14;
vector<long double> SimplexMethod(vector<vector<long double>> A, vector<long double> b, vector<long double> c) {
               int n = A.size(), m = A[0].size() + 1, r = n, s = m - 1;
    vector<vector<long double>> D = vector<vector<long double>>(n + 2, vector<long double>(m + 1));
    vector<int> ix(n + m);
    for (int i = 0; i < n + m; i++) ix[i] = i;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m - 1; j++) D[i][j] = -A[i][j];
        D[i][m - 1] = 1;
        D[i][m] = b[i];
        if (D[r][m] > D[i][m]) r = i;
    }
    for (int j = 0; j < m - 1; j++) D[n][j] = c[j];
    D[n + 1][m - 1] = -1;
    for (long double d;;) {
        if (r < n) {
            int t = ix[s]; ix[s] = ix[r + m]; ix[r + m] = t;
            D[r][s] = 1.0 / D[r][s];
            for (int j = 0; j <= m; j++) if (j != s) D[r][j] *= -D[r][s];
            for (int i = 0; i <= n + 1; i++) if (i != r) {
                for (int j = 0; j <= m; j++) if (j != s) D[i][j] += D[r][j] * D[i][s];
                D[i][s] *= D[r][s];
            }
        }
        r = -1; s = -1;
        for (int j = 0; j < m; j++) if (s < 0 || ix[s] > ix[j]) {
            if (D[n + 1][j] > kEps || D[n + 1][j] > -kEps && D[n][j] > kEps) s = j;
        }
        if (s < 0) break;
        for (int i = 0; i < n; i++) if (D[i][s] < -kEps) {
            if (r < 0 || (d = D[r][m] / D[r][s] - D[i][m] / D[i][s]) < -kEps
                || d < kEps && ix[r + m] > ix[i + m]) r = i;
        }
        if (r < 0) return vector<long double>();
    }
    if (D[n + 1][m] < -kEps) return vector<long double>();
    vector<long double> x = vector<long double>(m - 1);
    for (int i = m; i < n + m; i++) if (ix[i] < m - 1) x[ix[i]] = D[i - m][m];
    return x;
}

vector<long double> Solve(long double x, int n) {
	vector<vector<long double>> A;
	vector<long double> b;
	vector<long double> c;
	for (int i = 0; i < n; ++i) {
		c.push_back(0);
	}
		vector<long double> v;
		for (int i = 0; i < n; ++i) {
			v.push_back(::b[i]);
		}
		A.push_back(v);
		b.push_back(0);
		for (int i = 0; i < n; ++i) {
			v[i] = -v[i];
		}
		A.push_back(v);
		b.push_back(0);

		for (int i = 0; i < n; ++i) {
			v[i] = a[i];
		}
		A.push_back(v);
		b.push_back(1);
		for (int i = 0; i < n; ++i) {
			v[i] = -v[i];
		}
		A.push_back(v);
		b.push_back(-1);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				v[j] = (i == j);
			}
			A.push_back(v);
			b.push_back(x);
		}
	vector<long double> ret = SimplexMethod(A, b, c);
	long double xx = 0, yy = 0;
	for (int i = 0; i < ret.size(); ++i) {
		xx += ret[i] * ::b[i];
		yy += ret[i] * ::a[i];
	}
	return ret;
}

void Solve() {
	int n;
	double v, x;
	cin >> n >> v >> x;
	for (int i = 0; i < n; ++i) {
		cin >> r[i] >> c[i];
		b[i] = x * r[i] - c[i] * r[i];
		a[i] = r[i] / v;
	}
	bool can = false;
	bool l = false, g = false, eq = false;
	for (int i = 0; i < n; ++i) {
		if (c[i] + kEps < x) {
			l = true;
		} else if (x + kEps < c[i]) {
			g = true;
		} else {
			eq = true;
		}
	}
	long double lb = 0, ub = 1000000001;
	bool fail = Solve(ub, n).empty();
	if (!fail) {
		for (int i = 0; i < 64; ++i) {
			long double mb = (ub + lb) / 2.0;
			if (Solve(mb, n).empty()) {
				lb = mb;
			} else {
				ub = mb;
			}
		}
		printf("%.10lf\n", (double)ub);
	} else {
		if (eq || g && l) {
			cerr << "Fail!" << eq << g << l;
		}
		printf("IMPOSSIBLE\n");
	}
}

int main() {
	freopen("b_large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}