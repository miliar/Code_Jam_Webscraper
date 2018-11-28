#include<bits/stdc++.h>
#define ll long long int
#define pf printf
#define sc scanf
using namespace std;

/* Function to calculate x raised to the power y in O(logn)*/
ll power(ll x, ll y)
{
    ll temp;
    if(y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
       {
       	  return x*temp*temp;
       }
}
ll k,c,s;
ll t;
int main()
{
	sc("%lld", &t);
	static int chk=1;
	while(t--)
	{
	
		sc("%lld%lld%lld", &k,&c,&s);
		ll ans = power(k,c-1);
	    pf("Case #%d: ", chk);chk++;
		ll tile = 1;
		for(int i=0;i<s;i++)
		{
			pf("%lld ", tile);
			tile = tile+ans;
		}
		pf("\n");
	}
}
