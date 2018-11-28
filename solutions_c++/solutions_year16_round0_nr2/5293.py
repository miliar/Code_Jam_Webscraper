#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    scanf("%d\n", &T);
    for (int i = 0; i < T; ++i) {
        char s[200];
        gets(s);
        int len = strlen(s);
        s[len] = '+';
        int cnt = 0;
        for (int i = 0; i < len; ++i) {
            if (s[i] != s[i + 1])  {
                ++cnt;
            }
        }
        printf("Case #%d: %d\n", i + 1, cnt);
    }
}