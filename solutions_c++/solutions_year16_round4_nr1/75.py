
#include <bits/stdc++.h>
#define int long long
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i < _a; ++i)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR(A,n)  { cout << #A << " = "; FOR(_,1,n) cout << A[_] << ' '; cout << endl; }
#define PR0(A,n) { cout << #A << " = "; REP(_,n) cout << A[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
#define ll long long
#define __builtin_popcount __builtin_popcountll
#define SZ(x) ((int) (x).size())
using namespace std;

double safe_sqrt(double x) {
    return sqrt(max((double)0.0,x));
}
int GI(ll& x) {
    return scanf("%lld", &x);
}

int n, p, r, s;

#define TWO(X) (1<<(X))

string expand(char c, int n) {
    if (n == 0) {
        string res = "";
        res += c;
        return res;
    }

    string a, b;
    if (c == 'P') {
        a = expand('P', n-1);
        b = expand('R', n-1);
    }
    else if (c == 'R') {
        a = expand('R', n-1);
        b = expand('S', n-1);
    }
    else if (c == 'S') {
        a = expand('S', n-1);
        b = expand('P', n-1);
    }
    else assert(0);

    if (a > b) swap(a, b);

    return a + b;
}

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
	int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n >> r >> p >> s;

        cout << "Case #" << test << ": ";

        try {
            int saven = n;
            while (n > 0) {
                int sp = TWO(n-1) - r;
                int pr = TWO(n-1) - s;
                int rs = TWO(n-1) - p;

                s = sp;
                p = pr;
                r = rs;
                --n;

                if (s < 0 || p < 0 || r < 0) throw 1;
            }
            assert(s + p + r == 1);

            if (s) cout << expand('S', saven);
            if (p) cout << expand('P', saven);
            if (r) cout << expand('R', saven);
            cout << endl;
        } catch (...) {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}
