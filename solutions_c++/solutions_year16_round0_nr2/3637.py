#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;


int main() {
#ifdef LOCAL
    freopen("/Users/yew1eb/ClionProjects/CppGo/in.txt", "r", stdin);
    freopen("/Users/yew1eb/ClionProjects/CppGo/out.txt", "w", stdout);
#endif
    int T;
    char s[200];
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%s", s);
        int len = strlen(s);
        while (len > 0 && s[len - 1] == '+') len--;
        char ch;
        int ans = 0;
        for (int i = 0; i < len; ++i) {
            if (i == 0) {
                ch = s[i];
                ans++;
            } else if (s[i] != ch) {
                ch = s[i];
                ans++;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}