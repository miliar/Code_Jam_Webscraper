#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <queue>
#include <set>


using namespace std;


struct data {
  int x,y,h;
};
typedef struct data tri;
typedef long long ll;
typedef long L;
typedef int I;
typedef double D;
typedef float F;

#define SL(s) strlen(s)
#define BUF 1024
#define pb(i) push_back(i)
#define it(x) vector<x>::iterator x
#define inf 2147483647

char ibuf[BUF];
int ipt = BUF;
int SI()
{
  while(ipt<BUF && ibuf[ipt]<'0')
    ipt++;
  if(ipt==BUF)
  {
      fread(ibuf,1,BUF,stdin);
      ipt=0;
      while(ipt<BUF && ibuf[ipt]<'0')
        ipt++;
  }
  int n=0;
  while(ipt<BUF && ibuf[ipt]>='0')
    n=(n*10)+(ibuf[ipt++]-'0');
  if (ipt==BUF)
  {
      fread(ibuf,1,BUF,stdin);
      ipt=0;
      while(ipt<BUF && ibuf[ipt]>='0')
        n=(n*10)+(ibuf[ipt++]-'0');
  }
  return n;
}

//ll mod=1000000007;

/* code starts here */
tri A[10000];
int M[100][100],m,n;
bool temp[100][100];

void f();
int check(tri a);
bool compare(tri , tri );
int check_row(int r, int h);
int check_col(int r, int h);
int main()
{
 int t,i,m,n;
 scanf("%d",&t);
 for(i=1;i<=t;i++)
  {
    printf("Case #%d: ",i);
    f();
  }
return 0;
}
void f()
{
  int i,j,w,k;
  
  scanf("%d%d",&n,&m);
  for(i=0,k=0;i<n;i++)
    for(j=0;j<m;j++)
    {
      scanf("%d",&M[i][j]);
      A[k].x=i;
      A[k].y=j;
      A[k].h=M[i][j];
      k++;
      temp[i][j]=0;
    }
    std::sort(A,A+n*m,compare);
    //printf("%d %d %d\n",A[i].x,A[i].y,A[i].h);
    int flag=0;
    for(i=0;i<m*n&&!flag;i++)
    {
      if(temp[A[i].x][A[i].y]) continue;
      w=check(A[i]);
      if(!w) flag=1;
    }
    if(flag) puts("NO");
    else puts("YES");
    return;

}
bool compare(tri a, tri b)
{
  if(a.h<b.h) return true;
  return false;
}
int check(tri a)
{
  return check_row(a.x,a.h)||check_col(a.y,a.h);
}
int check_row(int r, int h)
{
  int i;
  for(i=0;i<m;i++)
    if(M[r][i]>h)  return 0;
  for(i=0;i<m;i++)
     temp[r][i]=1;
   return 1;
}
int check_col(int r, int h)
{
  int i;
  for(i=0;i<n;i++)
    if(M[i][r]>h)  return 0;
  for(i=0;i<n;i++)
     temp[i][r]=1;
   return 1;
}