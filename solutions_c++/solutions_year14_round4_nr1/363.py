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
        int n,x;
        cin >> n >> x;
        vi v(n);
        for (int i = 0; i < n; ++i)
            cin >> v[i];
        sort(v.begin(), v.end());
        vi was(n);
        int res = 0;
        for (int i = n-1; i >= 0; --i) if (!was[i]) {
            int it = i-1;
            while (it >= 0 && (v[it] + v[i] > x || was[it]))
                --it;
            ++res;
            was[i] = 1;
            if (it >= 0) was[it] = 1;
//            cerr << i << ' ' << it << endl;
        }
        cout << res << endl;
    }
    return 0;
}
