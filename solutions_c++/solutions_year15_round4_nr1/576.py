#include <bits/stdc++.h>

using namespace std;

const int _dx[4]={-1, 1, 0, 0};
const int _dy[4]={0, 0, -1, 1};
int N, M;
char grid[200][200];
bool bad[200][200];
bool hit[200][200];

void _main()
{
    memset(bad, 0, sizeof bad);
    memset(hit, 0, sizeof hit);
    scanf("%d%d", &N, &M);
    for(int i=0; i<N; i++)
        scanf("%s", grid[i]);
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++) if(grid[i][j]!='.')
        {
            int x=i, y=j;
            int dx, dy;
            if(grid[i][j]=='^')
                dx=-1, dy=0;
            else if(grid[i][j]=='v')
                dx=1, dy=0;
            else if(grid[i][j]=='<')
                dx=0, dy=-1;
            else
                dx=0, dy=1;
            x+=dx, y+=dy;
            while(0<=x && x<N && 0<=y && y<M && grid[x][y]=='.')
                x+=dx, y+=dy;
            if(x<0 || x>=N || y<0 || y>=M)
                bad[i][j]=true;
            else
                hit[x][y]=true;
        }
    int ans=0;
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++)
        {
            if(bad[i][j])
            {
                if(hit[i][j])
                    ans++;
                else
                {
                    bool found=false;
                    bool seen=false;
                    for(int k=0; k<4; k++)
                    {
                        int x=i, y=j;
                        int dx=_dx[k], dy=_dy[k];
                        x+=dx, y+=dy;
                        while(0<=x && x<N && 0<=y && y<M && grid[x][y]=='.')
                            x+=dx, y+=dy;
                        if(x<0 || x>=N || y<0 || y>=M)
                            continue;
                        if(bad[x][y] && !hit[x][y])
                        {
                            bad[x][y]=false;
                            found=true;
                            ans+=2;
                            break;
                        }
                        seen=true;
                    }
                    if(found)
                        continue;
                    if(seen)
                        ans++;
                    else
                    {
                        printf("IMPOSSIBLE\n");
                        return;
                    }
                }
            }
        }
    printf("%d\n", ans);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        _main();
    }
    return 0;
}
