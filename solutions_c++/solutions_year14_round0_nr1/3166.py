#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
int f[5][5],g[5][5],a[10];
map<int,int>ff;
int main()
{
    int ncase,n,m,tt=0,i,j;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&ncase);
    while(ncase--)
    {
        scanf("%d",&n);
        ff.clear();
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                scanf("%d",&g[i][j]);
                if(i==n)ff[g[i][j]]=1;
            }
        scanf("%d",&m);
        int tmp=0,id;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                scanf("%d",&f[i][j]);
                if(i==m&&ff.count(f[i][j]))
                    tmp++,id=f[i][j];
            }
        if(tmp==1)
            printf("Case #%d: %d\n",++tt,id);
        else if(tmp>1)
            printf("Case #%d: Bad magician!\n",++tt);
        else
            printf("Case #%d: Volunteer cheated!\n",++tt);
    }
    return 0;
}
