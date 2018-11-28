#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int s[1005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        int n;
        scanf("%d", &n);
        for (int i=0; i<=n; i++) {
            scanf("%1d",s+i);
        }
        int ans = 0,cnt=0;
        for(int i=0; i<=n; i++) {
            if (cnt < i) {
                ans += (i-cnt);
                cnt += (i-cnt);
            }
            cnt+=s[i];
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
