#include<cstdio>
using namespace std;
int t,n,cnt,i,j,a[25][25],c[25],d[25],sol[25];
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&t);
    for(int I=1;I<=t;I++)
    {
        scanf("%d",&n); cnt=0;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        for(i=1;i<=4;i++) c[++cnt]=a[n][i];

        scanf("%d",&n); cnt=0;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        for(i=1;i<=4;i++) d[++cnt]=a[n][i];

        cnt=0;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                if(c[i]==d[j])
                    sol[++cnt]=c[i];

        printf("Case #%d: ",I);
        if(cnt==0) printf("Volunteer cheated!\n");
        else if(cnt==1) printf("%d\n",sol[1]);
        else printf("Bad magician!\n");
    }
    return 0;
}
