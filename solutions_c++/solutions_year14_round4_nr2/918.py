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
        int n;
        cin >> n;
        int d[1010];
        for (int i = 0; i < n; i++) {
            cin >> d[i];
        }
        int l[1010] = {}, r[1010] = {};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (d[j] > d[i]) l[i]++;
            }
            for (int j = i+1; j < n; j++) {
                if (d[j] > d[i]) r[i]++;
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            res += min(l[i], r[i]);
        }
        printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
