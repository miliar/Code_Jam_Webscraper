#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
struct move
{
     int x,y;
}mv[4]={{0,1},{0,-1},{1,0},{-1,0}};
int a[101][101];
bool v[101][101],vx[101][101];
int n,m;
int ans;
inline void bfs(int x,int y,int dis,int s)
{
	 if(a[x][y]!=0&&v[x][y])
	      return ;
	 v[x][y]=true;
     int i;
     int xx,yy;
     if(dis==1)
     {
          xx=x-1;
          yy=y;
     }
     else if(dis==2)
     {
          xx=x;
          yy=y+1;
     }
     else if(dis==3)
     {
          xx=x+1;
          yy=y;
     }
     else if(dis==4)
     {
          xx=x;
          yy=y-1;
     }
     if(xx<=0||xx>n||yy<=0||yy>m)
     {
     	 // v[xx][yy]=true;
          ans++;
     }
     else if(a[xx][yy]==0)
          bfs(xx,yy,dis,s);
     else
          bfs(xx,yy,a[xx][yy],s+1);
}
int main()
{
//	 freopen("A-small-attempt1.in","r",stdin);
//	 freopen("A-small-attempt1.out","w",stdout);
	 freopen("A-large.in","r",stdin);
	 freopen("A-large.out","w",stdout);
     int T,k=0;
	 scanf("%d",&T);
	 while(T>0)
	 {
	      T--;
	      k++;
	      printf("Case #%d: ",k);
	      scanf("%d%d",&n,&m);
	      int i,j,kk;
	      string x;
	      for(i=1;i<=n;i++)
	      {
	           cin>>x;
	           for(j=1;j<=m;j++)
	           {
	                if(x[j-1]=='^')
	                     a[i][j]=1;
	                else if(x[j-1]=='>')
	                     a[i][j]=2;
	                else if(x[j-1]=='v')
	                     a[i][j]=3;
	                else if(x[j-1]=='<')
	                     a[i][j]=4;
	                else
	                     a[i][j]=0;
	           }
	      }
	      memset(v,false,sizeof(v));
	      memset(vx,false,sizeof(vx));
	      ans=0;
	      for(i=1;i<=n;i++)
	      {
	           for(j=1;j<=m;j++)
	           {
	                if(!v[i][j])
	                {
	                	 //v[i][j]=true;
	                     if(a[i][j]!=0)
	                     {
	                          bfs(i,j,a[i][j],1);
	                     }
	                }
	           }
	      }
	      bool flag=true;
	      for(i=1;i<=n;i++)
	      {
	           for(j=1;j<=m;j++)
	           {
	           	    if(a[i][j]==0)
	           	         continue;
	                bool flagx=false;
	                for(kk=1;kk<=n;kk++)
	                {
	                     if(a[kk][j]!=0&&kk!=i)
	                          flagx=true;
	                }
	                for(kk=1;kk<=m;kk++)
	                {
	                     if(a[i][kk]!=0&&kk!=j)
	                          flagx=true;
	                }
	                if(!flagx)
	                     flag=false;
	           }
	      }
	      if(flag)
	      {
	           printf("%d\n",ans);
	      }
	      else
	           printf("IMPOSSIBLE\n");
	 }
	 return 0;
}
