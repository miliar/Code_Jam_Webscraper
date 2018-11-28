#include<cstdio>
#include<bits/stdc++.h>
int a[1024];
void solve() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n;i++)
        scanf("%d", a+i);
    int opt = 0x7fffFFFF;
    for(int maxp = 1; maxp <= 1000; maxp++) {
        int t = 0;
        for(int i = 0; i < n; i++) {
            int k = (a[i] + maxp - 1)/ maxp;
            t += k - 1;
        }
        if(t + maxp < opt)
            opt = t + maxp;
    }
    printf("%d", opt);
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

