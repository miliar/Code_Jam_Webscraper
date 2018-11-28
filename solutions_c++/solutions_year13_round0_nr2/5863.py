#include<iostream>
#include<stdio.h>
#define N 105
using namespace std;
int main()
{
int a[N][N];
int t,m,n,flag1,flag2,flag3,flag4,flag5;
freopen ("in2large.txt","r",stdin);
freopen ("out2large.txt","w",stdout);
scanf("%d",&t);
int z=1;
while(t--)
{
scanf("%d%d",&n,&m);
for(int i=0;i<n;i++)
for(int j=0;j<m;j++)
scanf("%d",&a[i][j]);

for(int i=0;i<n;i++)
{for(int j=0;j<m;j++)
{flag5=0;
flag1=flag2=flag3=flag4=1;
  for(int k=0;k<n;k++)
  if(a[i][j]<a[k][j])
  flag1=0;

  for(int k=0;k<m;k++)
  if(a[i][j]<a[i][k])
  flag2=0;


  if(flag1 || flag2)
  flag5=1;


  if(!flag5)
  break;
 }
if(!flag5)
  break;
}
  if(flag5)
  printf("Case #%d: YES\n",z++);
  else
  printf("Case #%d: NO\n",z++);
  }
  return 0;
}

