#include<iostream>
#include<cstdio>
#include<vector>
#include<fstream>
using namespace std;
int z,x,y,t,n,m,layer,l0,l1,lo,hi,mid;
int a[2000];
vector<int> r;
void f(int lo,int hi,vector<int> v)
{
  if(lo==hi)
    a[lo]=v[0];
  else
  {
    int mid=(lo+hi)/2;
    vector<int> p,q;
    p.clear();
    q.clear();
    for(int i=0;i<v.size();i++)
      if(i%2==0)
        p.push_back(v[i]);
      else
        q.push_back(v[i]);
    f(lo,mid,p);
    f(mid+1,hi,q);
  }
}
int main()
{
  freopen("b1.in","r",stdin);
  freopen("b1.out","w",stdout);
  cin>>t;
  for(z=1;z<=t;z++)
  {
    cin>>n>>m;
    layer=n;
    n=(1<<n);
    r.clear();
    for(l0=0;l0<n;l0+=2)
      r.push_back(l0);
    f(1,n/2,r);
    for(l0=2;l0<=n/2;l0++)
    {
      if(a[l0-1]>a[l0])
        a[l0]=a[l0-1];
    }
    for(l1=n/2+1;l1<=n-1;l1++)
      a[l1]=n-2;
    a[n]=n-1;
    x=a[m];
    y=n-1-a[n-m]-1;
    if(m==n)
      y=n-1;
    printf("Case #%d: %d %d\n",z,y,x);
  }
  return 0;
}
