#include <bits/stdc++.h>
using namespace std;
int T;
long double ans, C, F, X, H, CPS, t;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cin >> C >> F >> X;
        ans = 1000 * 1000;
        CPS = 2;
        H = 0;
        t = 0;
        while (true) {
            ans = min(ans, t + 1.0 * (X - H) / CPS);
            if (t > ans)
                break;
            t += C / CPS;
            H = 0;
            CPS += F;
        }
        cout << "Case #" << testcase << ": " << setprecision(9) << fixed << ans << endl;;

    }
    return 0;
}
