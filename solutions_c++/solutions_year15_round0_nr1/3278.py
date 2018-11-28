#include <cstdio>
#include <iostream>
using namespace std;

const int maxn = 1005;
int T;
int n, s[maxn], ans;
char str[maxn];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for (int cas=1;cas<=T;cas++) {
        cin >> n >> str;
        for (int i=0;i<=n;i++) s[i] = str[i]-'0';
        ans = 0;
        int cur = 0;
        for (int i=0;i<=n;i++) {
            if (cur < i) {
                ans += i - cur;
                cur = i + s[i];
            } else {
                cur += s[i];
            }
        }
        cout << "Case #" << cas << ": " << ans << endl;
    }
    return 0;
}
