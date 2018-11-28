#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int a[10000];
char s[10000];
int T;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int Case = 1; Case <= T; ++Case) {
        int smax;
        scanf("%d ", &smax);
        gets(s);
        for (int i = 0; i <= smax; ++i)
            a[i] = s[i] - '0';
        int ans = 0, aud = 0;
        for (int i = 0; i <= smax; ++i) {
            if (aud + ans < i && a[i] > 0)
                ans = i - aud;
            aud += a[i];
        }
        printf("Case #%d: %d\n", Case, ans);
    }
    return 0;
}
