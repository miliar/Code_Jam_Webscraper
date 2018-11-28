#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#include<cctype>
#include<string>
#include<algorithm>
#include<iostream>
using namespace std;
typedef long long LL;
const int NN=105;
int mat[NN][NN];

bool check(int n,int j,int p)
{
    int i;
    for(i=1;i<=n;i++)
        if(mat[i][j]>p)
            return false;
    return true;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int ncase,ee=0;
    int n,m,i,j,mm;
    bool fg;
    scanf("%d",&ncase);
    while(ncase--)
    {
        fg=true;
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                scanf("%d",&mat[i][j]);
        for(i=1;i<=n;i++)
        {
            mm=-1;
            for(j=1;j<=m;j++)
                if(mat[i][j]>mm)
                    mm=mat[i][j];
            for(j=1;j<=m;j++)
            {
                if(mat[i][j]<mm)
                    fg=check(n,j,mat[i][j]);
                if(!fg)
                    break;
            }
            if(!fg)
                break;
        }
        printf("Case #%d: ",++ee);
        if(fg)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
