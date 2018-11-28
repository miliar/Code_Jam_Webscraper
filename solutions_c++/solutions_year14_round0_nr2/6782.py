#include <bits/stdc++.h>

#define ll long long
#define eps 0.0000001

using namespace std;

const int INF = 1e9 + 7;
const int MXN = 1e5 + 7;

int t;

double ans, c, f, x;

int main()
{
    //freopen("ss.in", "r", stdin);
    //freopen("ss.out", "w", stdout);

    scanf("%d", &t);

    for (int it = 0; it < t; it++) {
        double cur = 0;

        cin >> c >> f >> x;

        ans = x / 2.0;
        for (int cnt = 0; cnt < MXN; cnt++) {
            cur += c / (2.0 + f * cnt);
            double tmp = cur + (x / (2.0 + f * cnt + f));
            if (ans - tmp > eps)
                ans = tmp;
        }
        printf("Case #%d: ", it + 1);
        cout << fixed << setprecision(7) << ans << "\n";
    }
    return 0;
}
