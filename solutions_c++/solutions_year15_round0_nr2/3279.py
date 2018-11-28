#include <algorithm>
#include <climits>
#include <iostream>

using namespace std;

int main() {
        int T;
        cin >> T;
        for (int casenum = 1; casenum <= T; ++casenum) {
                int d, p[1000], maxp = 0;
                cin >> d;
                for (int i = 0; i < d; ++i) {
                        cin >> p[i];
                        maxp = max(maxp, p[i]);
                }
                int ans = maxp;
                for (int t = 1; t < maxp; ++t) {
                        int tmp = t;
                        for (int i = 0; i < d; ++i) {
                                if (p[i] <= t) continue;
                                tmp += p[i] / t - (p[i] % t == 0 ? 1 : 0);
                        }
                        ans = min(ans, tmp);
                }
                cout << "Case #" << casenum << ": " << ans << endl;
        }
        return 0;
}
