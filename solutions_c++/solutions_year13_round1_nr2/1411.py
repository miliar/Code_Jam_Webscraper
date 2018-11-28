#include<vector>
#include<queue>
#include<assert.h>
#include<string>
#include<map>
#include<iomanip>
#include<iostream>
#include<cstring>
#include<list>
#include<set>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#define INF 1000000
#define M 201
#define ML (1000000007)
#define maxn 10000
#define UL unsigned long long
using namespace std;

int min(int a,int b)
{
  return a>b ? b:a;
}

int max(int a,int b)
{
  return a>b ? a:b;
}
template<typename T>
T abs(T a)
{
  return a>=0 ? a:-a;
}

long long sum=0;
int data[10000];
int dis[10000];
int base[10000];
int main()
{
  freopen("B-small-attempt0.in","r",stdin);
  freopen("out.txt","w",stdout);
  int t;
  cin>>t;
  for(int k=1;k<=t;k++)
  {
    sum=0;
    int e,r,n;
    cin>>e>>r>>n;
    for(int i=0;i<n;i++)
      cin>>data[i];
    for(int i=0;i<n;i++)
    {
      int j=i+1;
      for(;j<n;j++)
      {
        if(data[j]>data[i])
          break;

      }
      if(j==n)
        base[i]=0;
      else
      {
         base[i]=e-r*(j-i);
        if(base[i]<0)
          base[i]=0;
      }
    }
    int ne=e;
    for(int i=0;i<n;i++)
    {
      if(ne>base[i])
      {
        sum+=(long long)(ne-base[i])*data[i];
        ne=base[i];
      }
      ne+=r;
      if(ne>e)
        ne=e;
    }
    cout<<"Case #"<<k<<": "<<sum<<"\n";
  }
  return 0;
}