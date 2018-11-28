#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int a[6][6],b[6][6];
int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int n,cas,i,j,m,d=1;
    scanf("%d",&cas);
    while(cas--)
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            scanf("%d",&a[i][j]);
        }
        scanf("%d",&m);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            scanf("%d",&b[i][j]);
        }
        int ct=0,flag,ok=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[n][i] == b[m][j])
                {
                    ct++;
                    if(ok==0)
                    flag=a[n][i];
                }
            }
        }
        if(ct==0 )
        printf("Case #%d: Volunteer cheated!\n",d++);
        else if(ct==1)
        printf("Case #%d: %d\n",d++,flag);
        else
        printf("Case #%d: Bad magician!\n",d++);
    }
return 0;
}
