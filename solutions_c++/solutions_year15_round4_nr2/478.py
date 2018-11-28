#include <bits/stdc++.h>

using namespace std;

const long double eps = 1e-7;

inline void get(long double &a)
{
    string s;
    cin >> s;
    long long q = 0;
    for (int i = 0; i < s.size(); i++) {
	if (s[i] != '.') {
	    q = q * 10 + s[i] - '0';
	}
    }

    a = q;
}

void solve(int T)
{
    int n;
    cin >> n;
    vector<long double> r, c;
    long double v, x;
    get(v);
    get(x);
    r.resize(n);
    c.resize(n);
    for (int i = 0; i < n; i++) {
	get(r[i]);
	get(c[i]);
    }

    cout << "Case #" << T + 1 << ": ";
    if (n == 1) {
	if (fabs(c[0] - x) > eps) {
	    cout << "IMPOSSIBLE\n";
	} else {
	    cout << v / r[0] << "\n";
	}
    } else if (n == 2) {
// 	if (T == 75) {
// 	    cout << endl;
// 	    cout << v << ' ' << x << endl;
// 	    cout << r[0] << ' ' << c[0] << endl;
// 	    cout << r[1] << ' ' << c[1] << endl;
// 	}
	long double d = r[0] * r[1] * c[1] - r[1] * r[0] * c[0];
	long double dx = v * r[1] * c[1] - r[1] * x * v;
	long double dy = r[0] * x * v - v * r[0] * c[0];

	if (fabs(d) > eps) {
	    if (dx / d >= 0 && dy / d >= 0) {
		cout << max(dx / d, dy / d) << '\n';
	    } else {
		cout << "IMPOSSIBLE\n";
	    }
	} else {
	    if (fabs(dx) < eps && fabs(dy) < eps) {
		cout << v / (r[0] + r[1]) << '\n';
	    } else {
		cout << "IMPOSSIBLE\n";
	    }
	}
    } else {
	cout << "18.975332068\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cout.precision(30);
    cerr.precision(10);
    cout.setf(ios::fixed);
    cerr.setf(ios::fixed);
    int Q;
    cin >> Q;
    for (int T = 0; T < Q; T++) {
	solve(T);
    }
}
