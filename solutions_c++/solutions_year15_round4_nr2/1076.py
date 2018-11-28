#include <bits/stdc++.h>

using namespace std;

#define FOR(i, a, b) for(int i = a; i <= b; i++)
#define REP(i, a, b) for(int i = a; i >= b; i--)
#define sz(x) (int)x.size()
#define pb push_back
#define mp make_pair

typedef pair<int, int> II;
typedef long long ll;

const int inf = (int)(1e8);
const double e = (1e-9);
const int Nmax = 110;

long long r[Nmax], c[Nmax], X, V;
int n;

void solve() {
    if (n == 1) {
        if (c[1] == X) {
            printf("%.10lf\n", (double)V/r[1]);
        } else cout << "IMPOSSIBLE" << endl;
        return;
    }

    if (c[1] == c[2]) {
        if (c[1] == X) {
            printf("%.10lf\n", (double)V/(r[1] + r[2]));
        } else cout << "IMPOSSIBLE" << endl;
        return;
    }
    long long a1 = r[1], b1 = r[2], c1 = V,
           a2 = c[1] * r[1], b2 = c[2] * r[2], c2 = V * X;
   // cout << a1 << ' ' << b1 << ' ' << c1 << endl;
   // cout << a2 << ' ' << b2 << ' ' << c2 << endl;

    double y = (double)(c2 * a1 - a2 * c1)/(b2 * a1 - a2 * b1),
           //x = (double)(c2 * b1 - b2 * c1)/(a2 * b1 - b2 * a1);
            x = (c1 - b1 * y)/a1;
    //printf("%.5lf %.5lf\n", x, y);
   // printf("%.9lf %.9lf\n", x, y);
    if (x < -e || y < -e) cout << "IMPOSSIBLE" << endl;
    else printf("%.10lf\n", max(x, y));
}

int convert(string s) {
    int res = 0;
    FOR(i, 0, sz(s) - 1) if (s[i] != '.') res = res * 10 + s[i] - '0';
    return res;
}

int main() {
    //freopen("B-small-attempt7.in", "r", stdin);
    //freopen("ans.out", "w", stdout);
    int test;
    cin >> test;
    string s1, s2;
    FOR(t, 1, test) {
        cin >> n >> s1 >> s2;
        V = convert(s1); X = convert(s2);
        //cout << V << ' ' << X << endl;
        FOR(i, 1, n) {
            cin >> s1 >> s2;
            r[i] = convert(s1);
            c[i] = convert(s2);
        }
        cout << "Case #" << t << ": ";
        if (n <= 2) solve();
    }
    return 0;
}
