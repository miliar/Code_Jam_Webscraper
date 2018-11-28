#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int map[105][105];

int main()
{
    //freopen("in.txt","r",stdin);
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int cases,id=1;
    scanf("%d",&cases);
    while(cases--)
    {
        int n,m;
        printf("Case #%d: ",id++);
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                scanf("%d",map[i]+j);
        int f=1;
        for(int i=1;f&&i<=n;i++)
        {
            int ma=101,k,j;
            for(j=1;j<=m;j++)
            {
                if(map[i][j]<ma)
                {
                    ma=map[i][j];
                }
            }
            for(j=1;j<=m;j++)
                if(map[i][j]!=ma)
                    break;
            if(j==m+1)
                continue;
            for(j=1;f&&j<=m;j++)
            {
                if(map[i][j]==ma)
                {
                    for(k=1;k<=n;k++)
                    {
                        if(map[k][j]>ma)
                            break;
                    }
                    if(k==n+1)
                        continue;
                    else
                        f=0;
                }
            }
        }
        if(f)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
