#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int n,m;
int a[5][5],b[5][5];
int vis[20];

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int ca=1;ca<=cas;ca++)
    {
        scanf("%d",&n);
        memset(vis,0,sizeof(vis));
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&m);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        for (int i=1;i<=4;i++)
            vis[a[n][i]]++,vis[b[m][i]]++;
        int num=0;
        for (int i=1;i<=16;i++)
            if (vis[i]==2) num++;
        printf("Case #%d: ",ca);
        if (num>1) printf("Bad magician!\n");
        else if (num==0) printf("Volunteer cheated!\n");
        else
        {
            for (int i=1;i<=16;i++)
                if (vis[i]==2) printf("%d\n",i);
        }
    }
    return 0;
}
