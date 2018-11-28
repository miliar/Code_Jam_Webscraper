#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<queue>
#include<algorithm>
#include<vector>
using namespace std;
int n;
int a[1111];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int tot;
    scanf("%d",&tot);
    for(int tit=1;tit<=tot;tit++)
    {
        scanf("%d",&n);
        int m=0,ans=100000000;
        for(int i=1,j;i<=n;i++)
            scanf("%d",&a[i]),m=max(m,a[i]);
        for(int h=1;h<=m;h++)
        {
            int d=0;
            for(int i=1;i<=n;i++)
                if(a[i])
                    d+=a[i]/h-!(a[i]%h);
            ans=min(ans,d+h);
        }
        printf("Case #%d: %d\n",tit,ans);
    }
}
