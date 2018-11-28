#include<stdio.h>
#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>

#define MOD 1000000007
#define INF 2000000000

using namespace std;

int dir_x[]={0,1,-1};
int dir_y[]={0,1,-1};
int vis[20][20];
int grid[10][10];

bool bfs(int n,int m,int sx,int sy)
{
     int i,j;
     queue<int> q_x,q_y;
     memset(vis,0,sizeof(vis));
     
     vis[sx][sy]=1;
     q_x.push(sx);
     q_y.push(sy);
     
     while(!q_x.empty())
     {
                      int u=q_x.front();
                      int v=q_y.front();
                      q_x.pop();
                      q_y.pop();
                      
                      for(i=0;i<3;i++)
                      {
                                      for(j=((i==0)?1:0);j<3;j++)
                                      {
                                                                int x=u+dir_x[i];
                                                                int y=v+dir_y[j];
                                                                
                                                                if(x>=0 && x<n && y>=0 && y<m && !vis[x][y])
                                                                {
                                                                        vis[x][y]=1;
                                                                        if(grid[x][y]==0)
                                                                        {
                                                                                         q_x.push(x);
                                                                                         q_y.push(y);
                                                                        }
                                                                }
                                      }
                      }
     }
     for(i=0;i<n;i++)
     {
                     for(j=0;j<m;j++)
                     {
                                     if(vis[i][j]==0 && grid[i][j]!=2)
                                      return false;
                     }
     }
     
     return true;
                      
}     

void gen_grid(int n,int m,int x)
{
     int i,j;
     int tmp=1;
     
     memset(grid,0,sizeof(grid));
     
     for(i=0;i<n;i++)
     {
                     for(j=0;j<m;j++)
                     {
                                     if((x&tmp)==tmp)
                                     {
                                                     grid[i][j]=2;
                                     }
                                     tmp*=2;
                     }
     }
     
     int k,l;
     
     for(i=0;i<n;i++)
     {
                     for(j=0;j<m;j++)
                     {
                                     if(grid[i][j]==2)
                                     {
                                                      for(k=0;k<3;k++)
                                                      {
                                                                      for(l=((k==0)?1:0);l<3;l++)
                                                                      {
                                                                                                 int u=i+dir_x[k];
                                                                                                 int v=j+dir_y[l];
                                                                                                 
                                                                                                 if(u>=0 && u<n && v>=0 && v<m && grid[u][v]!=2)
                                                                                                 {
                                                                                                         grid[u][v]=1;
                                                                                                 }
                                                                      }
                                                      }
                                     }
                     }
     }
     
     return;
}

bool test(int r,int c,int m)
{
     int i,j,k;
     
     for(i=0;i<1<<(r*c);i++)
     {
                             if(__builtin_popcount(i)==m)
                             {
                                                         gen_grid(r,c,i);
                             }
                             else
                             {
                                 continue;
                             }
                             
                             int f=0;
                             
                             for(j=0;j<r;j++)
                             {
                                             for(k=0;k<c;k++)
                                             {
                                                             if(grid[j][k]==0)
                                                             {
                                                                              f=1;
                                                                              break;
                                                             }
                                             }
                                             if(f)
                                              break;
                             }
                             
                             if(!f && m==(r*c-1))
                             {
                                   grid[j-1][k-1]=3;
                                   return true;
                             }
                             if(bfs(r,c,j,k))
                             {
                                                  grid[j][k]=3;
                                                  return true;
                             }
     }
     
     return false;
}

int main()
{
    int r,c,m,t,i,j;
    
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&t);
    int save=t;
    
    while(t--)
    {
              scanf("%d %d %d",&r,&c,&m);
              
              printf("Case #%d: \n",save-t);
              
              if(test(r,c,m))
              {
                             for(i=0;i<r;i++)
                             {
                                             for(j=0;j<c;j++)
                                             {
                                              if(grid[i][j]==2)
                                               printf("*");
                                              else if(grid[i][j]==3)
                                               printf("c");
                                              else
                                               printf(".");
                                             }
                                             printf("\n");
                             }
                             
              }
              else
              {
                  printf("Impossible\n");
              }
                             
    }
    
    return 0;
}
