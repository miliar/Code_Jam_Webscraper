#include <bits/stdc++.h>

#define reset(a, b) memset(a, b, sizeof(a))
#define REP(i, a) for (int i = 0; i < a.size(); i++)

using namespace std;

const int N = 100100;
const int INF = 1000000007;

int digit[10], cnt;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long long n;
        cin >> n;

        cout << "Case #" << t << ": ";

        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }

        reset(digit, 0);
        cnt = 10;
        for (int ans = 1; ; ans++) {
            long long nw = n * ans;
            while (nw > 0) {
                if (digit[nw % 10] == 0)
                    cnt--;
                digit[nw % 10]++;
                nw /= 10;
            }
            if (cnt == 0) {
                cout << ans * n << endl;
                break;
            }
        }
    }
}
