#include <queue>
#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int t, d, res, a[1005];

    cin >> t;
    for(int k = 1; k <= t; k ++) {
        res = 0;
        cin >> d;
        for(int i = 0; i < d; i ++) {
            cin >> a[i];
            res = max(res, a[i]);
        }

        for(int i = res; i >= 1; i --) {
            int tmp = i;
            for(int j = 0; j < d; j ++) {
                if(a[j] > i) {
                    tmp += a[j] / i + (a[j] % i ? 1 : 0) - 1;
                }
            }
            res = min(res, tmp);
        }
        cout << "Case #" << k << ": " << res << endl;
    }

    return 0;
}
