#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int m = 1000;
int dp[m+1];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int d = 0;
        cin >> d;

        int m = 0;
        vector<int> q(d, 0);
        for(int i = 0; i < d; i++) {
            cin >> q[i];
            m = max(m, q[i]);
        }

        int ans = m*d;
        for(int i = 1; i <= m; i++) {
            int left = 0, split = 0;
            for(int j = 0; j < q.size(); j++) {
                split += (q[j]+i-1)/i-1;
                left = max(left, min(i, q[j]));
            }

            ans = min(ans, left+split);
        }

        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}


