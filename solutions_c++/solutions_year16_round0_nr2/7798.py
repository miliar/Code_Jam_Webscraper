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
  ll t,count,i,j,k;
  scanf("%lld",&t);
  char str[1000];
  rep(k,1,t+1)
    {
      scanf("%s",str);
      ll len=strlen(str);
      count=0;
      if (len > 1)
	{
	  rep(i,1,len)
	    {
	      if (str[i]!=str[i-1])
		count++;
	    }
	}
      if (str[len-1]=='-')
	count++;
      printf("Case #%lld: %lld\n",k,count);
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
