#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;
int n, s;
int a[10005];

int main() {
    int T;
    freopen("large.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> n>>s;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        sort(a, a + n);
        int st = 0, en = n - 1;
        int ans = 0;
        while (en >= st) {
            if (a[st] + a[en] <= s) {
                st++;
                en--;
            } else en--;
            ans++;
        }
        printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}