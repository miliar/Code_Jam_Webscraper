#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <set>
#include <queue>
#include <map>

#define pb push_back
#define mp make_pair
#define F first
#define S second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long double ld;

const int INF = int(1e9);
const int MOD = int(1e9) + 7;
const ll INFll = 1ll * INF * INF;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    #ifdef LOCAL
        freopen("input.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int t;
    cin >> t;
    cout << fixed << setprecision(8);
    for (int o = 1; o <= t; ++o) {
        cout << "Case #" << o << ": ";
        double ans = INF, c, x, f, cur = 2, time = 0;;
        cin >> c >> f >> x;
        for (int i = 0; i < 100005; ++i) {
            ans = min(ans, time + x / cur);
            time += c / cur;
            cur += f;
        }
        cout << ans << endl;
    }
    return 0;
}

