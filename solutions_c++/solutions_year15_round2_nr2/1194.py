#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <map>
#include <sstream>
#include <string.h>

using namespace std;
int mat[16][16];
int ans;
int r,c,n;
void dfs(int t,int cnt)
{
    if(t == 0)
    {
        ans = min(ans,cnt);
    }
    if(cnt>ans)
        return;
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
        {
        if(mat[i][j] == 0)
            {
                mat[i][j] = 1;
                int cur = 0;
                if(i>0 && mat[i-1][j]==1)
                    cur++;
                if(j>0 && mat[i][j-1]==1)
                    cur++;
                if(i<r-1 && mat[i+1][j]==1)
                    cur++;
                if(j<c-1 &&mat[i][j+1]==1)
                    cur++;
                dfs(t-1,cur+cnt);
                mat[i][j] = 0;
            }
        }
}

void dfs2(int t,int cnt)
{
    if(t == 0)
    {
        ans = min(ans,cnt);
    }
    if(cnt - 4*t >ans)
        return;
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
        {
        if(mat[i][j] == 0)
            {
                mat[i][j] = 1;
                int cur = 0;
                if(i>0 && mat[i-1][j]==0)
                    cur++;
                if(j>0 && mat[i][j-1]==0)
                    cur++;
                if(i<r-1 && mat[i+1][j]==0)
                    cur++;
                if(j<c-1 &&mat[i][j+1]==0)
                    cur++;
                dfs2(t-1,cnt - cur);
                mat[i][j] = 0;
            }
        }

}

int main()
{
    int T,cas = 1;

    freopen("d:\\codejam\\B-small-attempt0.in","r",stdin);
    freopen("d:\\codejam\\B-small-attempt0.our","w",stdout);

    scanf("%d",&T);
    while(T--)
    {
        memset(mat,0,sizeof(mat));
        ans = 1000000000;
        scanf("%d %d %d",&r,&c,&n);
        if(n<=r*c/2)
            dfs(n,0);
        else
            dfs2(r*c-n,(r-1)*c + (c-1)*r);
        printf("Case #%d: %d\n",cas++,ans);
    }

    return 0;
}
