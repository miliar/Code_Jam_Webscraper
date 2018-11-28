#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char matrix[111][111];
int label[111][111],lt[111][111],rt[111][111],up[111][111],down[111][111],r,c,ans;
const int dir[4][2]={{0,1},{0,-1},{1,0},{-1,0}};

bool ck(int i,int j)
{
    if (i>=0&&i<r&&j>=0&&j<c) return 1;
    return 0;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&r,&c);
        for (int i=0;i<r;++i) scanf("%s",matrix[i]);
        ans=0;
        bool flag=1;
        for (int i=0;flag&&i<r;++i)
            for (int j=0;flag&&j<c;++j)
                if (matrix[i][j]!='.')
                {
                    flag=0;
                    for (int k=0;!flag&&k<4;++k)
                        for (int x=i+dir[k][0],y=j+dir[k][1];ck(x,y);x+=dir[k][0],y+=dir[k][1])
                            if (matrix[x][y]!='.')
                            {
                                flag=1;
                                break;
                            }
                }
        printf("Case #%d: ",cas);
        if (!flag)
        {
            puts("IMPOSSIBLE");
            continue;
        }
        for (int i=0;i<r;++i)
            for (int j=0;j<c;++j)
            {
                int k;
                if (matrix[i][j]=='>') k=0;
                else if (matrix[i][j]=='<') k=1;
                else if (matrix[i][j]=='v') k=2;
                else if (matrix[i][j]=='^') k=3;
                else continue;
                bool flag=0;
                for (int x=i+dir[k][0],y=j+dir[k][1];ck(x,y);x+=dir[k][0],y+=dir[k][1])
                    if (matrix[x][y]!='.')
                        {
                            flag=1;
                            break;
                        }
                if (!flag) ++ans;
            }
        printf("%d\n",ans);
    }
    return 0;
}
