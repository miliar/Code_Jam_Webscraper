#include <iostream>

using namespace std;

int t;
long long n;
string s;
int cas = 1;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(false);
    freopen("dat.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    while (t--) {
        cin >> n >> s;
        long long cur = s[0] - '0';
        long long ans = 0;
        for (int i = 1; i <= n; i++) {
            //cout << cur << "\n";
            if (cur < i) {
                ans += i - cur;
                cur += i - cur;
            }
            cur += s[i] - '0';
        }
        cout << "Case #" << cas++ << ": " << ans << "\n";
    }
}
