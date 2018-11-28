#include <iostream>
using namespace std;
const int maxn = 52;
int m,n,p,flag;
int dx[9]={-1,-1,-1,0,0,0,1,1,1},dy[9]={-1,0,1,-1,0,1,-1,0,1};
char str[3]={'.','*','c'};
int set(int x,int y,int map[][maxn])
{
    int i,s=0;
    for(i=0;i<9;i++){
                     if(map[x+dx[i]][y+dy[i]]!=0){map[x+dx[i]][y+dy[i]]=0;++s;}
                     map[x+dx[i]][y+dy[i]]=0;
                     }
    return s;
}
bool find_c(int x,int y,int map[][maxn])
{
     int i,s=0;
     for(i=0;i<9;i++)if(map[x+dx[i]][y+dy[i]]!=0)return false;
     return true;
}
void renew(int map[][maxn])
{
     int i,j;
     for(i=1;i<=m;i++)
     for(j=1;j<=n;j++)
     {
     if(map[i][j])continue;
     if(find_c(i,j,map)){map[i][j]=2;return;}
     }
}
void output(int map[][maxn])
{
     int i,j;
     for(i=1;i<=m;i++,printf("\n"))
     for(j=1;j<=n;j++)
     printf("%c",str[map[i][j]]);
}
void dfs(int x,int s,int map[][maxn])
{    
     if(flag)return ;
     if(s == p){renew(map);output(map);flag = 1;return ;}
     if(x>m)return ;
     if(s + (m-x+1)*n < p)return ;
     int i,k;
     int c[maxn][maxn];
     memcpy(c,map,sizeof(c));
     k = s;
     for(i = 1;i <=n ;i++)
     {
           k = k+set(x,i,map);
           if(k>p)break;
           dfs(x+1,k,map);
     }
     memcpy(map,c,sizeof(c));
     dfs(x+1,s,map);
     memcpy(map,c,sizeof(c));
}
int main(void)
{
    int tc,i,j,k,map[maxn][maxn],rp;
    scanf("%d",&tc);
    for(i=1;i<=tc;i++)
    {
    printf("Case #%d:\n",i);
    memset(map,0,sizeof(map));
    scanf("%d%d%d",&m,&n,&p);
    for(j=1;j<=m;j++)
    for(k=1;k<=n;k++)
    map[j][k]=1;
    p = m*n-p;
    if(p==1){map[1][1]=2;output(map);continue;}
    flag=0;
    dfs(1,0,map);
    if(!flag){printf("Impossible\n");continue;}
    }
    return 0;
}
                       
