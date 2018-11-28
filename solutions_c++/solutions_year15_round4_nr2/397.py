#include <bits/stdc++.h>

using namespace std;

#define lol long long
#define fi first
#define se second
#define pb push_back
#define sz(s) (lol)s.size()
#define must ios_base::sync_with_stdio(0)

#define inp(s) freopen(s, "r", stdin)
#define out(s) freopen(s, "w", stdout)

double c[110];
double r[110];
const double eps = 1e-6;

int main() {
    inp("input.txt");
    out("output.txt");
    int tt, t;
    cin >> t;
    for(tt = 1; tt <= t; tt++) {
        int n, i;
        double v, x;
        cin >> n >> v >> x;
        cout << "Case #" << tt << ": ";
        if(n > 2) {
            cout << "BAD N\n";
            continue;

        }
        for(i = 1; i <= n; i++)
            cin >> r[i] >> c[i];
        if(n == 1) {
            if(abs(c[1] - x) <= eps)
                printf("%.6f\n", v / r[1]);
            else
                cout << "IMPOSSIBLE\n";
            continue;
        }
        if(c[1] > c[2])
            swap(c[1], c[2]), swap(r[1], r[2]);

        if(c[1] > x || c[2] < x) {
            cout << "IMPOSSIBLE\n";
        } else if(abs(c[1] - x) <= eps && abs(c[2] - x) <= eps) {
            printf("%.10f\n", v / (r[1] + r[2]));
        } else if(abs(c[1] - x) <= eps) {
            printf("%.10f\n", v / r[1]);
        } else if(abs(c[2] - x) <= eps) {
            printf("%.10f\n", v / r[2]);
        } else {
            double v1 = (x - c[2]) * v / (c[1] - c[2]);
            double v2 = v - v1;
            printf("%.10f\n", max(v1 / r[1], v2 / r[2]));
        }
    }
}

