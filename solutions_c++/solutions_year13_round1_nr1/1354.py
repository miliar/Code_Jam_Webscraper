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
bool check(UL num,UL area,UL r)
{
  if(2*num*r-num>area)
    return false;
  if(2*num*num>area)
    return false;
  if(2*num*num+2*num*r-num>area)
    return false;
  return true;

}
int get(UL are)
{
  int count=0;
  while(are)
  {
    count++;
    are=are/10;
  }
  return count-1;
}
long long getan(UL area,UL r)
{
  UL sr=1000000000;
 UL sl=0;
  int count=get(r);
UL newr=2;
 while(count<18)
 {
   newr*=10;
   count++;
 }
 if(newr<sr)
   sr=newr;
 while(sl<=sr)
 {
   UL mid=(sr+sl)/2;
   if(check(mid,area,r))
   {
     sl=mid+1;
   }
   else
     sr=mid-1;
 }
 return sr;
}
int main()
{
  //freopen("A-small-attempt2.in","r",stdin);
 // freopen("out.txt","w",stdout);
  int t;
  cin>>t;
  for(int k=1;k<=t;k++)
  {
    UL area;
    UL r;
    cin>>r>>area;
    UL res=getan(area,r);
    cout<<"Case #"<<k<<": "<<res<<"\n";
  }
  return 0;
}