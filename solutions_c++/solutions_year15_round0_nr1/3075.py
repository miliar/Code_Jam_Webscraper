#include<bits/stdc++.h>

const int maxn = 1010;
int n;
char s[maxn];

int main() {
    int Test,T,i,j,k,t,ans;
    scanf("%d",&Test);
    for (T=1; T<=Test; ++T) {
        scanf("%d",&n); ++n;
        scanf("%s",s);
        t = 0; ans = 0;
        for (i=0; i<=n; ++i) {
            if (t<=i) ans += i-t,t = i;
            t += (int)s[i]-'0';
        }
        printf("Case #%d: %d\n",T,ans);
    }
    return 0;
}
