#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cc=0;cc<t;cc++)
    {
        int r,c;
        char g[111][111];
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",g[i]);
        int fail=0,ans=0;
        for(int i=0;i<r;i++)
            for(int j=0;j<c;j++)
            {
                if(g[i][j]!='.')
                {
                    int valid=0;
                    if(g[i][j]=='>')
                    {
                        for(int k=j+1;k<c;k++)
                            if(g[i][k]!='.')
                                valid=1;
                    }
                    if(g[i][j]=='<')
                    {
                        for(int k=j-1;k>=0;k--)
                            if(g[i][k]!='.')
                                valid=1;
                    }
                    if(g[i][j]=='v')
                    {
                        for(int k=i+1;k<r;k++)
                            if(g[k][j]!='.')
                                valid=1;
                    }
                    if(g[i][j]=='^')
                    {
                        for(int k=0;k<i;k++)
                            if(g[k][j]!='.')
                                valid=1;
                    }
                    if(valid) continue;

                    {
                        int isfail=1;
                        for(int k=j+1;k<c;k++)
                            if(g[i][k]!='.')
                                isfail=0;
                        for(int k=j-1;k>=0;k--)
                            if(g[i][k]!='.')
                                isfail=0;
                        for(int k=i+1;k<r;k++)
                            if(g[k][j]!='.')
                                isfail=0;
                        for(int k=0;k<i;k++)
                            if(g[k][j]!='.')
                                isfail=0;
                        if(isfail) fail=1;
                        ans++;
                    }

                }
            }
        if(fail)
            printf("Case #%d: IMPOSSIBLE\n",cc+1);
        else
            printf("Case #%d: %d\n",cc+1,ans);

    }
    return 0;
}
