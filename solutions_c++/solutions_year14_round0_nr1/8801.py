#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
 //   freopen("A-small-attempt3.in","r",stdin);
 //   freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int dex=1;dex<=T;dex++)
    {
        int n,m;
        int a[5][5],b[5][5];
        int x[17];
        scanf("%d",&n);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        memset(x,0,sizeof(x));
        for (int k=1;k<=4;k++)
            x[a[n][k]]=1;
        scanf("%d",&m);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        int ans=0,t;
        for (int k=1;k<=4;k++)
            if (x[b[m][k]])
                ans++,t=b[m][k];
        if (ans==1) printf("Case #%d: %d\n",dex,t);
        else if (ans==0) printf("Case #%d: Volunteer cheated!\n",dex);
        else printf("Case #%d: Bad magician!\n",dex);
    }
 //   system("pause");
    return 0;
}
