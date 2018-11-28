#include<cstdio>
#include<algorithm>
using namespace std;
int x[1005];
int main()
{
    freopen("2015_Q_B_l.in","r",stdin);
    freopen("2015_Q_B_l.out","w",stdout);
    int T,n,mn=1000,cp;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&x[i]);
        mn=1000;
        for(int i=1;i<=1000;i++)
        {
            cp=i;
            for(int j=0;j<n;j++)
                cp+=(x[j]-1)/i;
            mn=min(mn,cp);
        }
        printf("Case #%d: %d\n",I,mn);
    }
}
