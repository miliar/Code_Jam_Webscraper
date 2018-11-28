#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

typedef long long lld;

int main() {
    cout.setf(ios_base::fixed);
    cout.precision(7);
    int T;
    cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        cout << "Case #" << ti << ": ";
        int n, x;
        cin >> n >> x;
        multiset< int > as;
        for (int i = 0; i < n; ++i) {
            int t;
            cin >> t;
            as.insert(t);
        }
        int ans = 0;
        while (!as.empty()) {
            ans += 1;
            auto a = as.begin();
            as.erase(a);
            auto b = as.upper_bound(x - *a);
            if (b != as.begin()) {
                --b;
                as.erase(b);
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
