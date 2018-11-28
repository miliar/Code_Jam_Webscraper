#include<bits/stdc++.h>

using namespace std;

char s[101];

int f() {
    int len = strlen(s);
    int groups = 0;
    for (int i = 1; i < len; i++) {
        if (s[i] != s[i-1]) {
            groups++;
        }
    }

    if (s[0] == '+' && groups % 2 == 1) {
        groups++;
    } else if (s[0] == '-' && groups % 2 == 0) {
        groups++;
    }

    return groups;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d\n", &t);
    for (int i=1; i<=t; i++) {
        gets(s);
        printf("Case #%d: %d\n", i, f());
    }

    return 0;
}

