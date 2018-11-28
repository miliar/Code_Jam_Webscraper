#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int t, rest;
bool u[10];
long long n, ans, tmp;

int main() {
    freopen("a.in","r", stdin);
    freopen("ans.out","w", stdout);
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n;
        printf("Case #%d: ", i);
        if (n == 0) {
            puts("INSOMNIA");
            continue;
        }
        memset(u, 0, sizeof(u));
        rest = 10; ans = 0;
        while (rest) {
            ans += n; tmp = ans;
            while (tmp) {
                if (!u[tmp % 10]) --rest;
                u[tmp % 10] = true;
                tmp /= 10;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
