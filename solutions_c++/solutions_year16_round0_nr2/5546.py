#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef long long ll;

const int INF = 0x3c3c3c3c;

int used[10];

int main() {
    #define task "t"//"eulertour"
    freopen(task".in", "r", stdin);
    freopen(task".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        string s;
        cin >> s;
        int add = 0;
        int ans = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            int a = (s[i] == '-');
            if (a ^ add) {
                add ^= 1;
                ans++;
            }
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
