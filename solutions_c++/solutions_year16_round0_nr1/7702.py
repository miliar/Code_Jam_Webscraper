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


int main()
{
  ll t,n,i,arr[10],count,x,y,z,k;
  scanf("%lld",&t);
  rep(k,1,t+1)
    {
      count=10;
      scanf("%lld",&n);
      if (n==0)
	{
	  printf("Case #%lld: INSOMNIA\n",k);
	  continue;
	}
      x=0;
      rep(i,0,10)
	arr[i]=0;
      while(count)
	{
	  x+=n;
	  y=x;
	  while(y)
	    {
	      z=y%10;
	      y=y/10;
	      if (arr[z]==0)
		{
		  arr[z]++;
		  count--;
		}
	    }
	}
      printf("Case #%lld: %lld\n",k,x);
    }
  return 0;
}

