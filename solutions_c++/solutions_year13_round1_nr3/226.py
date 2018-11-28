#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<fstream>
using namespace std;
int gar;
int r,n,m,k;
int l0,l1,a[20],big,lft;
int c[20],t[20],add[20];
int main()
{
  freopen("csmall.in","r",stdin);
  freopen("c.out","w",stdout);
  cin>>gar;
  cout<<"Case #1:\n";
  cin>>r>>n>>m>>k;
  while(r--)
  {
    memset(c,0,sizeof(c));
    lft=n;
    for(l0=1;l0<=k;l0++)
    {
      cin>>a[l0];
      big=max(big,a[l0]);
    }
    for(l0=m;l0>=2;l0--)
    {
      while(big%l0==0)
      {
        big/=l0;
        c[l0]++;
        lft--;
      }
    }
    for(l0=1;l0<=k;l0++)
    {
      if(a[l0]==1)
        continue;
      memcpy(t,c,sizeof(c));
      memset(add,0,sizeof(add));
      for(l1=m;l1>=2;l1--)
        while(big%l1==0&&t[l1]>=0)
        {
          t[l1]--;
          big/=l1;
        }
      for(l1=m;l1>=2;l1--)
        while(big%l1==0)
        {
          add[l1]++;
          big/=l1;
          lft--;
        }
      for(l1=2;l1<=m;l1++)
          c[l1]+=add[l1];
    }
    if(lft>0)
      c[2]+=lft;
    for(l0=2;l0<=m;l0++)
      for(l1=1;l1<=c[l0];l1++)
        cout<<l0;
    cout<<endl;
  }
  return 0;
}
