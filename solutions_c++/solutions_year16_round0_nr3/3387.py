#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;
typedef long long ll;

ll prime(ll num) {
    for (ll i = 2; i <= sqrt(num); i++)
        if (num % i == 0) return i;
    return -1;
}

bool valid(ll nums[]) {
    for (int i = 1; i <= 10; i++)
        if (nums[i] == 0) return false;
    return true;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, N, J;
    cin >> T;
    int caseNum = T;
    while (T--) {
        cin >> N >> J;
        cout << "Case #" << caseNum - T << ":\n";
        ll ans[J][11];
        for (int i = 0; i < J; i++)
            for (int j = 0; j < 11; j++)
                ans[i][j] = 0;
        int now = 0;
        for (ll i = (1 << (N - 1)) + 1; i < (1 << N); i += 2) {
            for (ll b = 2; b <= 10; b++) {
                ll num = 0;
                ll base = 1;
                for (int j = 0; j < N; j++) {
                    if (i & (1 << j)) num += base;
                    base *= b;
                }
                if (prime(num) == -1) break;
                ans[now][b] = prime(num);
                if (b == 10) ans[now][1] = num;
            }
            if (valid(ans[now])) {
                now++;
            } else {
                for (int c = 1; c <= 10; c++) ans[now][c] = 0;
            }
            if (now == J) break;
        }
        for (int i = 0; i < J; i++) {
            for (int j = 1; j <= 10; j++) {
                cout << ans[i][j];
                if (j < 10) cout << " ";
                if (j == 10) cout << endl;
            }
        }
    }
    return 0;
}