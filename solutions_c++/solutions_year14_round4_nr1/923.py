#include <vector>
#include <iostream>
#include <set>
#include <cstdio>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cmath>
#include <complex>
#include <algorithm>
#include <tuple>
#include <algorithm>
#include <limits>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef tuple<int, int, int> T;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, x;
        cin >> n >> x;
        multiset<int, greater<int>> s;
        for (int i = 0; i < n; i++) {
            int d;
            cin >> d;
            s.insert(d);
        }
        int r = 0;
        while (s.size()) {
            int u = *s.begin();
            s.erase(s.begin());
            auto it = s.lower_bound(x-u);
            if (it != s.end()) {
                s.erase(it);
            }
            r++;
        }
        printf("Case #%d: %d\n", t, r);
    }
    return 0;
}
