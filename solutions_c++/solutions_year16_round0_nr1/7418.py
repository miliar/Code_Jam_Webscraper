#include <bits/stdc++.h>
using namespace std;

#define mi 1000000007
#define ll long long int
#define rep(i,a,b) for(i=a;i<b;i++)
#define repv(i,a,b) for(i=b-1;i>=a;i--)
#define inf INT_MAX

int gcd(int a,int b) { return b==0 ? a : gcd (b,a%b);}
int lcm(int a,int b) { return a*(b/gcd(a,b));}

ll pow1(ll a,ll b)
{
  ll ans=1;
  while(b>0)
    {
      if(b&1)
	{
	  ans=((ans%mi)*(a%mi))%mi;
	}	
      a=((a%mi)*(a%mi))%mi;
      b>>=1;
    }	
  return ans;
}
ll mina(ll arr[],int n)
{
  ll x=arr[0],i;
  int pos=0;
  rep(i,1,n)
    if(arr[i]<x)
      {
	x=arr[i];
	pos=i;
      }
  return x;
}
ll maxa(ll arr[],int n)
{
  ll x=arr[0],i;
  int pos=0;
  rep(i,1,n)
    if(arr[i]>x)
      {
	x=arr[i];
	pos=i;
      }
  return x;
}
int main()
{
  int t,count=0;
  cin>>t;
  while(t--)
    {
      count++;
      ll n;
      cin>>n;
      ll x=0;
      int f[10],c=0;
      memset(f,0,sizeof(f));
      if(n==0)
	{
	  cout<<"Case #"<<count<<": "<<"INSOMNIA"<<endl;
	  continue;
	}
      else
	{
	  ll i=1;
	  while(1)
	    {
	      x=i*n;
	      ll y=x;
	      while(y>0)
		{
		  int l=y%10;
		  if(f[l]==0)
		    {
		      f[l]=1;
		      c++;
		    }
		  y/=10;
		}
	      if(c==10)
		break;
	      i++;
	    }
	}
      cout<<"Case #"<<count<<": "<<x<<endl;
    }
  return 0;
}
