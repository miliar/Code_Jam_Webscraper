#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
using namespace std;

bool isok(const vector<int> &a, int t) {
    for (int et = 1; et <= t; ++et) {
        int mt = 0;
        for (int i = 0; i < a.size(); ++i) {
            if (a[i] >= et) {
                mt += a[i] / et - 1;
                if (a[i] % et != 0)  ++mt;
            }
        }
        if (mt + et <= t) {
            return true;
        }
    }
    return false;
}

int main () {
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        sort(a.begin(), a.end());

        int mint = 1, maxt = 2000;

        while (maxt - mint > 1) {
            int mt = (mint + maxt) / 2;
            if (isok(a, mt)) {
                maxt = mt;
            } else {
                mint = mt;
            }
        }

        if (isok(a, mint)) {
            maxt = mint;
        }

        printf("Case #%d: %d\n", tt, maxt);
    }

    return 0;
}
