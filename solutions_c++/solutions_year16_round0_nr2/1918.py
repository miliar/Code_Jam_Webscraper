#include <bits/stdc++.h>

using namespace std;

int t;
char s[102];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &t);
    for (int tp=1; tp<=t; tp++) {
        scanf("%s", s);
        int l = strlen(s);
        int num = 0;
        bool rot = 0;
        for (int i=l-1; i>=0; i--) {
            if (rot ^ (s[i] == '-')) {
                rot = !rot;
                num++;
            }
        }
        printf("Case #%d: %d\n", tp, num);
    }

    return 0;
}
