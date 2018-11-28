#include<cstdio>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,a[4][4],b[4][4],ra,rb;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas)
    {
        scanf("%d",&ra);
        for(int i=0; i<4; ++i)
            for(int j=0; j<4; ++j)
                scanf("%d",&a[i][j]);
        scanf("%d",&rb);
        for(int i=0; i<4; ++i)
            for(int j=0; j<4; ++j)
                scanf("%d",&b[i][j]);
        int cnt=0,ans;
        for(int i=0; i<4; ++i)
            for(int j=0; j<4; ++j)
                if(a[ra-1][i]==b[rb-1][j])
                {
                    ++cnt;
                    ans=a[ra-1][i];
                }
        printf("Case #%d: ",cas);
        switch(cnt)
        {
        case 0:
            puts("Volunteer cheated!");
            break;
        case 1:
            printf("%d\n",ans);
            break;
        default:
            puts("Bad magician!");
        }
    }
}
