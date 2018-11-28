#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("test.txt","w",stdout);
    int t,n,i,a,ans,p;
    scanf("%d",&t);
    for(int j=1;j<=t;j++)
    {
        ans=0,p=0;
        scanf("%d",&n);
        for(i=0;i<=n;i++)
        {
            scanf("%1d",&a);
            if(p>=i)
            {
                p+=a;
            }
            else
            {
                ans+=(i-p);
                p+=a+(i-p);
            }
        }
        printf("Case #%d: %d\n",j,ans);
    }
}
