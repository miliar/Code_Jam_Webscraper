#include<cstdio>
#include<algorithm>
using namespace std;
int x[10005];
int main()
{
    freopen("2015_1A_A_l.in","r",stdin);
    freopen("2015_1A_A_l.out","w",stdout);
    int T,n,ans1,ans2;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        ans1=0; ans2=1000000000;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&x[i]);
        for(int i=1;i<n;i++)
            if(x[i-1]>x[i])
                ans1+=x[i-1]-x[i];
        for(int i=0,j,nw,cmp;i<=10000;i++)
        {
            nw=0;
            cmp=0;
            for(j=0;j<n;j++)
            {
                cmp+=min(i,nw);
                nw-=min(i,nw);
                if(nw>x[j])
                    break;
                else
                    nw=x[j];
            }
            if(j>=n)
                ans2=min(cmp,ans2);
        }
        printf("Case #%d: %d %d\n",I,ans1,ans2);
    }
}
