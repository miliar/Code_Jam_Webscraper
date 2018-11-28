#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;


char s[100];


void solve() {
    int n = strlen(s);
    char now = s[0];
    int ans = 0;
    for (int i = 1; i < n; i++) {
        if (s[i] != now) {
            ans++;
            now = s[i];
        }
    }
    if (now == '-')
        ans++;
    printf("%d\n", ans);
}

int main() {
    int t;
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca++) {
        scanf("%s", s);
        printf("Case #%d: ", ca);
        solve();


    }
}
