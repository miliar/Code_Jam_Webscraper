#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
using namespace std;
const int maxn = 110;
char s[maxn];
int T, tt, n;
int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%s", s);
        n = strlen(s);
        int ans = 0;
        while (true) {
            int l = 0, r = n - 1;
            while (r >= 0 && s[r] == '+') --r;
            if (r == -1) break;
            if (s[l] == '+') {
                while (l < n && s[l] == '+') {
                    s[l] = '-';
                    ++l;
                }
            }
            else {
                while (l <= r) {
                    char a = s[l];
                    char b = s[r];
                    s[r] = a == '-' ? '+' : '-';
                    s[l] = b == '-' ? '+' : '-';
                    ++l;
                    --r;
                }
            }
            ++ans;
        }
        printf("Case #%d: %d\n", ++tt, ans);
    }
    return 0;
}
