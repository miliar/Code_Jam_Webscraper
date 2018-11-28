#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define mod 1000000007LL
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>

int dir[][2]={ {0,0},{0,1},{0,-1},{1,0},{-1,0} };     //dx dy stay up down right left
map< char,int > dr;
int grid[105][105],mark[5][105][105];
set< pair<int,int> > chg;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-out.txt","w",stdout);
    int T,t,n,m,i,j,ans,flag;
    char s[105];
    dr['.']=0;
    dr['^']=1;
    dr['v']=2;
    dr['>']=3;
    dr['<']=4;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d %d",&n,&m);
        ans=0;
        for(i=0;i<105;i++)
        {
            for(j=0;j<105;j++)
            {
                for(int k=0;k<5;k++)
                    mark[k][i][j]=0;
            }
        }
        for(i=0;i<n;i++)
        {
            scanf("%s",s);
            for(j=0;j<m;j++)
            {
                grid[i][j]=dr[s[j]];
            }
        }
        chg.clear();
        flag=0;
        for(i=0;i<n;i++)
        {
            j=0;
            while(grid[i][j]==0&&j<m)    j++;
            mark[ 4 ][i][j]=1;
            if(grid[i][j]==4&&j<m)
            {
                chg.insert( mp(i,j) );
                grid[i][j]--;
            }
            j=m-1;
            while(j>=0&&grid[i][j]==0)    j--;
            mark[ 3 ][i][j]=1;
            if(grid[i][j]==3&&j>=0)
            {
                chg.insert( mp(i,j) );
                if(mark[ grid[i][j]+1 ][i][j]==1)
                    grid[i][j]--;
                else
                    grid[i][j]++;
            }
        }
        for(j=0;j<m;j++)
        {
            i=0;
            while(grid[i][j]==0&&i<n)    i++;
            mark[ 1 ][i][j]=1;
            if(grid[i][j]==1&&i<n)
            {
                chg.insert( mp(i,j) );
                grid[i][j]++;
            }
            i=n-1;
            while(i>=0&&grid[i][j]==0)    i--;
            mark[ 2 ][i][j]=1;
            if(grid[i][j]==2&&i>=0)
            {
                chg.insert( mp(i,j) );
                if(mark[ 1 ][i][j]==0)
                    grid[i][j]=1;
                else
                {
                    if(mark[3][i][j]==0)
                        grid[i][j]=3;
                    else if(mark[4][i][j]==0)
                        grid[i][j]=4;
                    else
                    {
                        flag=1;
                        break;
                    }
                }
            }
        }
        if(flag)
        {
            printf("Case #%d: IMPOSSIBLE\n",t);
            continue;
        }
        ans=chg.size();
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
