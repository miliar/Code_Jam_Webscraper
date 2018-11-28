#pragma comment(linker, "/STACK:1000000000")

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void Solve() {
    int n;
    vector<int> plates;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        plates.push_back(x);
    }

    int ma = 0;
    for (int i = 0; i < plates.size(); ++i)
        ma = max(ma, plates[i]);

    int ans = 100500;
    for (int k = 1; k <= ma; ++k) {
        int curBest = k;
        for (int i = 0; i < plates.size(); ++i) {
            if (plates[i] <= k)
                continue;
            curBest += plates[i] / k;
            if (plates[i] % k == 0)
                --curBest;
        }
        ans = min(ans, curBest);
    }

    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        Solve();
    }
    return 0;
}
