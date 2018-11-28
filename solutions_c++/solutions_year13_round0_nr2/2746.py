#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int grass[15][15];
int n,m;
bool judge(int x,int y)
{
    bool ok=true;
    for(int i=0;i<m;i++)
        if(grass[x][i]==2)
        {
            ok=false;
            break;
        }
    if(ok)
        return true;
    ok=true;
    for(int j=0;j<n;j++)
        if(grass[j][y]==2)
        {
            ok=false;
            break;
        }
    return ok;
}
bool solve()
{
    for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(grass[i][j]==1)
                {
                    if(!judge(i,j))
                        return false;
                }
    return true;
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        printf("Case #%d: ",cas);
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&grass[i][j]);
        if(solve())
            printf("YES\n");
        else printf("NO\n");
    }
}
