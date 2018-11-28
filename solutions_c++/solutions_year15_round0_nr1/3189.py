#include<cstdio>
#include<bits/stdc++.h>
char s[1024];
void solve() {
    int smax;
    scanf("%d %s", &smax, s);
    int res = 0;
    int standing = 0;
    for(int i = 0; s[i]; i++) {
        if(standing < i && s[i] > '0') {
            res += i - standing;
            standing = i;
        }
        standing += s[i] - '0';
    }
    printf("%d", res);
}
int main() {
    int T;
    scanf("%d", &T);
    for(int i = 1; i<=T;i++) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    return 0;
}
