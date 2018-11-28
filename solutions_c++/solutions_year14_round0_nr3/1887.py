using namespace std;
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#include<cassert>
#define read(x) scanf("%d",&x)
#define read2(x,y) scanf("%d%d",&x,&y)
#define read3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define rep(i,n) for(i=1;i<=n;++i)
#define max(a,b) ((a)>(b))?(a):(b)
typedef  long long int ull;
typedef pair<int,int> pr;
#define mx 7

int plot[mx][mx]={0},r,c,visited[mx][mx]={0};
queue < pr > q;

int check(int i,int j)
{
    if(i<0 || i>=r)return 1;
    if(j<0 || j>=c)return 1;
    return plot[i][j]==0;
}

int check2(int i,int j)
{
    if(i<0 || i>=r)return 0;
    if(j<0 || j>=c)return 0;
    if(visited[i][j])return 0;
    visited[i][j]=1;
    q.push(make_pair(i,j));
}


int bfs(int i,int j)
{
    memset(visited,0,sizeof(visited));
    while(!q.empty())q.pop();
    visited[i][j]=1;
    q.push(make_pair(i,j));
    int dx[8]={1,-1,0,0,1,-1,1,-1};
    int dy[8]={0,0,1,-1,1,1,-1,-1};
    int ans=0;
    
    while(!q.empty())
    {
                     ans++;
                     int x=q.front().first;
                     int y=q.front().second;
                     q.pop();
                     int dir,sum=0;
                     for(dir=0;dir<8;dir++)
                     sum+=check(x+dx[dir],y+dy[dir]);
                     
                     if(sum!=8)continue;
                     for(dir=0;dir<8;dir++)
                     check2(x+dx[dir],y+dy[dir]);
    }
    return ans;
}
                     
         
int ones(ull num)
{
    if(!num)return 0;
    return 1+ones(num&(num-1));
}         
                         

int main()
{
   // freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int t,m,i,j,k,tt=1;
    read(t);
    ull total,grid;
    while(t--)
    {
              read3(r,c,m);
              printf("Case #%d:\n",tt++);
              total=1<<(r*c);
              int found=0;
              
              for(grid=0;grid<total;grid++)
              if(ones(grid)==m)
              {
                             
                             memset(plot,0,sizeof(plot));
                             
                             for(i=0;i<r*c;i++)
                             if(grid& (1ll<<i))
                             plot[i/c][i%c]=1; //bomb
                             
                             int posx,posy;
                             
                             for(i=0;i<r && !found;i++)
                             for(j=0;j<c;j++)
                             if(plot[i][j]==0)
                             {
                                              if(bfs(i,j)==r*c-m)
                                              {
                                                                 
                                                 posx=i;
                                                 posy=j;
                                                 found=1;
                                                 break;
                                              }
                             }
                             
                             if(found)
                             {
                                for(i=0;i<r;printf("\n"),i++)
                                for(j=0;j<c;j++)
                                {
                                                if(plot[i][j]==0)
                                                {
                                                                 if(i==posx && j==posy)printf("c");
                                                                 else printf(".");
                                                }
                                                else printf("*");
                                }
                                break;
                             }
              }
              
              if(!found)printf("Impossible\n");
    }
}
