#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        int n;
        cin >> n;
        vi a(n);
        int ma = 0;
        int pos = 0;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            if (ma < a[i]) {
                ma = a[i];
                pos = i;
            }
        }
        int res = 0;
        for (int i = 0; i < n; ++i) {
            int c1 = 0, c2 = 0;
            for (int j = 0; j < i; ++j) if (a[j] > a[i]) ++c1;
            for (int j = i+1; j < n; ++j) if (a[j] > a[i]) ++c2;
            res += min(c1, c2);
        }
        cout << res << endl;
    }
    return 0;
}
