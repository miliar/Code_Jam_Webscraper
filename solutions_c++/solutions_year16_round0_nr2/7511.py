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
  int t,i,j,count=0;
  cin>>t;
  while(t--)
    {
      count++;
      string s;
      cin>>s;
      int l=s.size();
      i=l-1;
      ll ans=0;
      //cout<<l<<" "<<s<<endl;
      while(i>=0)
	{
	  if(s[i]=='-')
	    {
	      rep(j,0,i+1)
		{
		  if(s[j]=='-')
		    s[j]='+';
		  else
		    s[j]='-';
		}
	      ans++;
	    }
	  i--;
	}
      cout<<"Case #"<<count<<": "<<ans<<endl;
    }
  return 0;
}
