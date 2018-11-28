#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("C:\\codejam15\\A-large.in","r",stdin);
    freopen("C:\\codejam15\\A-large.out","w",stdout);
    int T,cas=1;
    int n,m;
    int R,C,W;
    scanf("%d",&T);
    while(T--)
    {
        int ans = 0;
        scanf("%d %d %d",&R,&C,&W);
        int cnt1 = C/W;
        ans += cnt1 * (R-1);
        ans += (C+W-1)/W + W-1;
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
