#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main() {
    freopen("A-Large.in","r",stdin);
    freopen("A-Large.out","w",stdout);
    int T, t, cur, ans, len, i;
    char str[1005];
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; t ++ ) {
        ans = cur = 0;
        scanf("%d %s",&len,&str);
        len ++;
        for ( i = 0 ; i < len ; i ++ ) {
            if ( cur < i && str[i] != '0' ) {
                ans += (i-cur);
                cur = i;
            }
            cur += str[i]-'0';
        }

        printf("Case #%d: %d\n",t,ans);
    }
}
