#include <iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int A[1010];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Qdata.out","w",stdout);
    int T,n,mx,x;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        mx=0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++) scanf("%d",&A[i]),mx=max(mx,A[i]);
        int res=999999999,tp;
        for(int div=1;div<=mx;div++)
        {
            tp=0;
            for(int i=1;i<=n;i++)
            {
                if(A[i]<=div) continue;
                tp+=(A[i]/div+(A[i]%div==0?0:1)-1);
            }
            res=min(res,div+tp);
        }
        printf("Case #%d: %d\n",kase,res);
    }
    return 0;
}
