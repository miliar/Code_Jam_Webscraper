#include <bits/stdc++.h>
using namespace std;

#define INF 2000000000
#define maxN 1005
#define ll long long

int TC, n;
ll a[maxN];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-large (1).in", "r", stdin);
    freopen("test.out", "w", stdout);
    #endif // ONLINE_JUDGE

    cin >> TC;
    for (int cs = 0; cs < TC; cs++) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        ll maxSpeed = -INF;
        for (int i = 0; i < n - 1; i++) {
            maxSpeed = max(maxSpeed, a[i] - a[i + 1]);
        }
        //cout << maxSpeed << endl;
        ll res1 = 0;
        ll res2 = 0;
        for (int i = 0; i < n - 1; i++) {
            if (a[i] - a[i + 1] > 0) {
                res1 += a[i] - a[i + 1];
            }
            if (a[i] > maxSpeed) {
                res2 += maxSpeed;
            } else {
                res2 += a[i];
            }
        }

        cout << "Case #" << cs + 1 << ": " << res1 << " " << res2 << endl;
    }

    return 0;
}
