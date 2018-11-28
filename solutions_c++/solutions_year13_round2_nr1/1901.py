#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX_SIZE = 1100000;
const int MAXN = 110;

int dp[MAX_SIZE];
int dp2[MAX_SIZE];
int mose[MAXN];

int main() 
{
    int t;
    cin >> t;

    for (int test_case = 1; test_case <= t; test_case++) {
        int a, n;
        cin >> a >> n;
        int max_mose = a;
        for (int i = 0; i < n; i++) {
            cin >> mose[i];
            max_mose += mose[i];
        }
        sort(mose, mose + n);
        max_mose = min(max_mose, MAX_SIZE - 2);

        for (int i = a; i <= max_mose; i++) {
            dp[i] = n + 1;
        }
        dp[a] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = a; j <= max_mose; j++) {
                dp2[j] = n + 1;
            }
            for (int j = a; j <= max_mose; j++) {
                if (dp[j] <= n) {
                    if (j <= mose[i]) {
                        dp2[j] = min(dp2[j], dp[j] + 1);
                        if (j == 1) {
                            continue;
                        }
                        int num = 0;
                        int now = j;
                        while (now <= mose[i]) {
                            num++;
                            now += now - 1;
                        }
                        now = min(now + mose[i], max_mose);
                        dp2[now] = min(dp2[now], dp[j] + num);
                    } else {
                        int new_size = min(j + mose[i], max_mose);
                        dp2[new_size] = min(dp2[new_size], dp[j]);
                    }
                }
            }
            memcpy(dp, dp2, sizeof(dp));
        }

        int ans = n + 1;
        for (int i = a; i <= max_mose; i++) {
            ans = min(ans, dp[i]);
        }
        cout << "Case #" << test_case << ": " << ans << "\n";
    }
}
