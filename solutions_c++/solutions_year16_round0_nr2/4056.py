#include<bits\stdc++.h>
using namespace std;
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; c++) {
        char s[105];
        char lookup = '+';
        bool first = true;
        int ans = 0;
        scanf("%s", s);
        for (int i = strlen(s) - 1; i >= 0; ) {
            for (; i >= 0 && s[i] == lookup; i--);
            if (!first)
                ans++;
            first = false;
            lookup = lookup == '+' ? '-' : '+';
        }
        printf("Case #%d: %d\n", c, ans);
    }
    return 0;
}