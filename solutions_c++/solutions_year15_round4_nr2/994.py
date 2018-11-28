#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100000 + 10;
const int INF = (int)(1e9);
const int MOD = (int)(1e9) + 7;
const double eps = 1e-9;

double r[MAXN], c[MAXN];
double v, x;
int n;

bool equals(double a, double b) {
    return (abs(a - b) <= eps);
}

double readReal() {
    string s;
    cin >> s;
    int p = -1;
    for(int i = 0; i < s.length(); i++) {
        if (s[i] == '.') {
            p = i;
            break;
        }
    }
    double res = 0.0;
    for(int i = 0; i < p; i++) res = res * 10 + (s[i] - '0');
    double x = 0;
    for(int i = p + 1; i < s.length(); i++) x = x * 10 + (s[i] - '0');
    res = res + x / 10000;
    return res;
}

double solve() {
    cin >> n;
    v = readReal(); x = readReal();
    for(int i = 1; i <= n; i++) {
        r[i] = readReal(); c[i] = readReal();
    }

    if (n == 1) {
        if (!equals(x, c[1])) return -1;
        return v / r[1];
    }


    double res = 1e18;
    for(int i = 1; i <= 2; i++) {
        if (equals(x, c[i])) {
            res = min(res, v / r[i]);
        }
    }

    if (!equals(c[1], c[2])) {
        double v1 = (x * v - v * c[2]) / (c[1] - c[2]);
        if (v1 >= 0) {
            double v2 = v - v1;
            if (v2 >= 0) res = min(res, max(v1 / r[1], v2 / r[2]));
        }
    }
    else if (equals(c[1], x)){
        double v1 = (v * r[1]) / (r[1] + r[2]);
        res = v1 / r[1];
    }

    if (equals(res, 1e18)) res = -1;
    return res;
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("vuong.out", "w", stdout);
    //freopen("vuong2.out", "w", stdout);

    int test;
    cin >> test;
    for(int tc = 1; tc <= test; tc++) {
        printf("Case #%d: ", tc);
        double res = solve();
        if (equals(res, -1)) cout << "IMPOSSIBLE\n";
        else printf("%.07lf\n", res);
    }
}
