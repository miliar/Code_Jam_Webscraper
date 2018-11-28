#include <iostream>
#include <stdio.h>
using namespace std;

int t;
int n,m;
char grid[111][111];

int Dir(char ch)
{
    if (ch=='^')
    return 1;
    else if (ch=='>')
    return 2;
    else if (ch=='v')
    return 3;
    else
    return 4;
}

int ctr=0;

bool Death(int x,int y,int dir)
{
    if (x<1 || x>n || y<1 || y>m)
    return true;

    if (grid[x][y]!='.')
    ctr++;

    if (ctr>1)
    return false;

    if (dir==1)
    return Death(x-1,y,dir);
    else if (dir==2)
    return Death(x,y+1,dir);
    else if (dir==3)
    return Death(x+1,y,dir);
    else
    return Death(x,y-1,dir);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-output.txt","w",stdout);

    int test;
    int i,j;
    int ans;
    bool impossibru;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%d %d",&n,&m);

        for (i=1;i<=n;i++)
        {
            scanf("%s",grid[i]+1);
        }

        ans=0;
        impossibru=false;
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=m;j++)
            {
                if (grid[i][j]=='.')
                continue;

                ctr=0;
                if (Death(i,j,Dir(grid[i][j])))
                {
                    ans++;

                    ctr=0;
                    if ( Death(i,j,1) )
                    {
                        ctr=0;
                        if ( Death(i,j,2) )
                        {
                            ctr=0;
                            if ( Death(i,j,3) )
                            {
                                ctr=0;
                                if ( Death(i,j,4) )
                                {
                                    impossibru=true;
                                    break;
                                }
                            }
                        }
                    }
                }
            }

            if (impossibru)
            break;
        }

        printf("Case #%d: ",test);

        if (impossibru)
        printf("IMPOSSIBLE\n");
        else
        printf("%d\n",ans);
    }

    return 0;
}
