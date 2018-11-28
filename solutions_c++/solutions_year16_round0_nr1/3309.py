#include <iostream>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000
#define pdd pair<double, double>

int t, n;

inline int solve(int n) {
    int u[10]; for(int i = 0; i < 10; ++i) u[i] = 0;
        int cnt = 0, ans = 0;
        for(int iter = 0; iter < 1000; ++iter) {
            int x = n * (iter + 1);
            ans = x;
            while(x) {
                if (!u[x % 10]) ++cnt;
                u[x % 10] = 1;
                x /= 10;
            }
            if (cnt == 10) {
                break;
            }
        }
    if (cnt == 10) return ans; else return -1;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int tc = 1; tc <= t; ++tc) {
        cerr << tc << endl;
        cin >> n;
        int ans = solve(n);
        cout << "Case #" << tc << ": ";
        if (ans > 0) {
            cout << ans << endl;
        } else {
            cout << "INSOMNIA\n";
        }

    }
}
