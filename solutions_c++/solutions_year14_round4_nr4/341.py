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
const int mod = 1000000007;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        int m,n;
        cin >> m >> n;
        vector<string> s(m);
        for (int i = 0; i < m; ++i) cin >> s[i];
        vl cnt(10000000);
        int MAX = 1;
        for (int i = 0; i < m; ++i) MAX *= n;
        for (int mask0 = 0; mask0 < MAX; ++mask0) {
            vector<vs> v(n);
            int mask = mask0;
            for (int i = 0; i < m; ++i) {
                int j = mask % n;
                mask /= n;
                string cur = "";
                v[j].push_back(cur);
                for (int l = 0; l < s[i].size(); ++l) {
                    cur += s[i][l];
                    v[j].push_back(cur);
                }
            }
            int sum = 0;
            for (int i = 0; i < n; ++i) {
                sort(v[i].begin(), v[i].end());
                sum += unique(v[i].begin(), v[i].end()) - v[i].begin();
            }
            assert(sum < cnt.size());
            cnt[sum]++;
        }
        for (int i = cnt.size() - 1; i >= 0; --i) {
            if (cnt[i]) {
                cout << i << ' ' << cnt[i] % mod << endl;
                break;
            }
        }
    }
    return 0;
}
