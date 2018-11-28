#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

int n, ans, m;
string st;

int main() {
    freopen("a.in","r", stdin);
    freopen("ans.txt","w", stdout);
    int cas; scanf("%d", &cas);
    for (int t = 1; t <= cas; t++) {
        cin >> n; cin >> st; ans = 0;
        m = st[0] - '0';
        for (int i = 1; i <= n; i++) {
            if (m == 0) ++ans; else --m;
            m += st[i] -'0';
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
