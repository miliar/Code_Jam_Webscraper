#include <bits/stdc++.h>

using namespace std;

#define mi 1000000007
#define rep(i,a,b) for(i=a;i<b;i++)
#define repd(i,a,b,d) for (i=a;i<b;i+=d)
#define repv(i,a,b) for(i=b-1;i>=a;i--)
#define vi vector<int>
#define vl vector<long long int>
#define vvi vector <vector <int> >
#define ll long long int

ll maxa(ll a,ll b);
ll mina(ll a,ll b);
ll paw(ll a,ll b);



int main()
{
  int t,i,m,ma,mb,si,arr[100],j,n;
  cin>>t;
  rep(j,1,t+1)
    {
      cout<<"Case #"<<j<<": ";
      cin>>n;
      si=0;
      rep(i,0,n)
	{
	  cin>>arr[i];
	  si+=arr[i];
	}
      m=-1;
      ma=-1;
      mb=-1;
      while(si)
	{
	  if (si==3)
	    {
	      break;
	    }
	  m=-1;
	  rep(i,0,n)
	    {
	      if (arr[i]>m)
		{
		  ma=i;
		  m=arr[i];
		}
	    }
	  si--;
	  arr[ma]--;
	  if (si==0)
	    {
	      cout<<(char)(ma+(int)'A');
	      break;
	    }
	  m=-1;
	  rep(i,0,n)
	    {
	      if (arr[i]>m)
		{
		  mb=i;
		  m=arr[i];
		}
	    }
	  si--;
	  arr[mb]--;
	  if (m>0)
	    cout<<(char)(ma+(int)'A')<<char(mb+(int)'A')<<" ";
	  else if (arr[ma]>0)
	    cout<<(char)(ma+(int)'A')<<" ";
	}
      if (si==3)
	{
	  int x=0;
	  rep(i,0,n)
	    {
	      if (arr[i]>0)
		x++;
	    }
	  if (x==3)
	    {
	      rep(i,0,n)
		{
		  if (arr[i]>0)
		    {
		      cout<<(char)(i+(int)'A')<<" ";
		      arr[i]--;
		      break;
		    }
		}
	      rep(i,0,n)
		{
		  if (arr[i]>0)
		    {
		      cout<<(char)(i+(int)'A');
		      arr[i]--;
		    }
		}
	      cout<<"\n";
	    }
	  else if (x==2)
	    {
	      rep(i,0,n)
		{
		  if (arr[i]>0)
		    {
		      cout<<(char)(i+(int)'A')<<" ";
		      arr[i]--;
		      break;
		    }
		}
	      rep(i,0,n)
		{
		  if (arr[i]>0)
		    {
		      cout<<(char)(i+(int)'A');
		      arr[i]--;
		    }
		}
	      cout<<"\n";
	    }
	}
      else
	{
	  cout<<"\n";
	}
    }

  return 0;
}



ll maxa(ll a,ll b)
{
  if (a>b)
    return a;
  return b;
}

ll mina(ll a,ll b)
{
  if (a<b)
    return a;
  return b;
}

ll paw(ll a, ll b)
{
  ll x=((a)%mi),ans=1;
  while(b>0)
    {
      if (b&1)
	ans=(ans*x)%mi;
      x=(x*x)%mi;
      b>>=1;
    }
  return ans;
}
