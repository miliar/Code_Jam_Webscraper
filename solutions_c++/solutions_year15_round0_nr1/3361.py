#include <stdio.h>
#include <string.h>
#include <stdlib.h>
const int maxn = 1e3 + 5;
char s[maxn];
int a[maxn];
int solve()
{
    int sz = strlen(s);
    a[0] = s[0]-'0';
    int ans = 0;
    for(int i = 1; i < sz; i++) {
        a[i] = a[i-1];
        int c = s[i] - '0';
        if(c&&a[i]<i){
            ans += (i - a[i]);
            a[i] = i;
        }
        a[i] += c;
    }
    return ans;
}
int main(int argc, char const *argv[])
{
    int T;
    scanf("%d",&T);
    for(int i = 1; i <= T; ++i) {
        int n;
        scanf("%d%s",&n,s);
        printf("Case #%d: %d\n",i,solve());
    }
    return 0;
}