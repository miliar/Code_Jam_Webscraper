#include<bits/stdc++.h>
using namespace std;
 
#define mod 1000000007
#define ll long long 
#define F first
#define S second
#define maxs 10045
#define INF INT_MAX
#define dbg(x) cout<<#x<<"="<<x<<endl
#define sc scanf
#define pb push_back
#define pf push_front
#define mp make_pair
#define pic pair<ll,char>
#define f(i,n) for(i=0;i<n;i++)
#define FOR(i,j,n) for(i=j;i<n;i++)

pic a[maxs];
bool rev(pic a,pic b)
{
  return (a.F>b.F);
}

int main()
{ 
  ll t,y,n,i,z=0,sum=0;
  char ch;
  cin>>t;
  f(z,t)
  {
    cout<<"Case #"<<z+1<<": ";
    cin>>n;
    ch='A';
    sum=0;
    y=1;
    f(i,n)
    {
    cin>>a[i].F;
    sum+=a[i].F;
    a[i].S=ch++;
    }
    while(1)
    {
    sort(a,a+n,rev);
    if(sum==0)break;
     
    if((sum-2)/2>=a[1].F && a[0].F>=2)
    {
      a[0].F=a[0].F-2;
      cout<<a[0].S<<a[0].S<<" ";
      sum-=2;

    }
    else if((sum-2)/2>=a[0].F-1  && a[1].F>=1 && (sum-2)/2>=a[2].F)
    {
     
      a[0].F--;
      a[1].F--;
       cout<<a[0].S<<a[1].S<<" ";
       sum-=2;

    }
    else 
    {
      if(a[0].F==1)
        {
    cout<<a[0].S<<" ";
    a[0].F--;
    sum--;
  }
      else if(a[0].F==0)
        {
    y=0;
  }


    }
  }
  cout<<endl;
  }

}
