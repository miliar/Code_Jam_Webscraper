#include<cstdio>
#include<bitset>

using namespace std;

int T;
int r,c;
int p[1000][1000];
int a[1000],b[1000];
// 1
//4 2
// 3
inline int change(int x,int y,int pos) 
{
  return ((x-1) *c+y-1) *4+pos;
}

inline bool dfs(int S,int T) 
{
  if (S==T) return true;
  int temp=(S-1) /4;
  int x0=temp/c+1;
  int y0=temp%c+1;
  int pos=S%4;
  if (pos==0) pos=4;

  if (p[x0][y0]==0) 
  {
    pos=5-pos;
  }
  else
  {
    if (pos==1||pos==3) 
      pos=pos+1;
    else
      pos=pos-1;
  }

  if (x0==1&&pos==1||x0==r&&pos==3||y0==1&&pos==4||y0==c&&pos==2) 
    if (change(x0,y0,pos) !=T) 
      return false;
    else
      return true;
  if (pos==1) pos=3,x0--;
  else
    if (pos==3) pos=1,x0++;
    else
      if (pos==2) pos=4,y0++;
      else
        pos=2,y0--;
  dfs(change(x0,y0,pos) ,T) ;
}
inline bool tri(int x) 
{
  for(int i=1;i<=r;i++) 
  {
    for(int j=1;j<=c;j++) 
    {
      p[i][j]=x&1;
      x>>=1;
    }
  }
  for(int i=1;i<=r+c;i++) 
  {
    if (!dfs(a[i],b[i]) ) 
      return false;
  }
  return true;
}
int main() 
{
  freopen("C-small-attempt4.in","r",stdin) ;
  freopen("C-small-attempt4.out","w",stdout) ;
  scanf("%d",&T) ;
  for(int t=1;t<=T;t++) 
  {
    scanf("%d%d",&r,&c) ;
    for(int i=1;i<=r+c;i++) 
    {
      scanf("%d%d",a+i,b+i) ;
      if (a[i]<=c) a[i]=change(1,a[i],1) ;
      else
      {
        a[i]-=c;
        if (a[i]<=r) a[i]=change(a[i],c,2) ;
        else
        {
          a[i]-=r;
          if (a[i]<=c) a[i]=change(r,c-a[i]+1,3) ;
          else
          {
            a[i]-=c;
            a[i]=change(r-a[i]+1,1,4) ;
          }
        }
      }
      if (b[i]<=c) b[i]=change(1,b[i],1) ;
      else
      {
        b[i]-=c;
        if (b[i]<=r) b[i]=change(b[i],c,2) ;
        else
        {
          b[i]-=r;
          if (b[i]<=c) b[i]=change(r,c-b[i]+1,3) ;
          else
          {
            b[i]-=c;
            b[i]=change(r-b[i]+1,1,4) ;
          }
        }
      }
    }
    bool flag=false;
    printf("Case #%d:\n",t) ;
    for(int i=0;i<(1<<r*c) ;i++) 
    {
      if (tri(i) ) 
      {
        for(int i0=1;i0<=r;i0++) 
        {
          for(int j0=1;j0<=c;j0++) 
            if (p[i0][j0]==0) 
              printf("/") ;
            else
              printf("\\") ;
          printf("\n") ;
        }
        flag=true;
        break;
      }
    }
    if (!flag) printf("IMPOSSIBLE\n") ;
  }
}
