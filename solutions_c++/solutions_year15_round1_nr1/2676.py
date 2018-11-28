#include <iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
int T,n,A[1010];
int main()
{
    freopen("data.out","w",stdout);
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;i++) scanf("%d",&A[i]);
        int res1=0;
        for(int i=2;i<=n;i++)
        {
            if(A[i]<A[i-1])
                res1+=A[i-1]-A[i];
        }
        int mx=0;
        for(int i=1;i<=n-1;i++)
            mx=max(mx,A[i]-A[i+1]);
        int res2=0;
        for(int i=2;i<=n;i++)
        {
            res2+=min(A[i-1],mx);
        }
        printf("Case #%d: %d %d\n",kase,res1,res2);
    }
    return 0;
}
