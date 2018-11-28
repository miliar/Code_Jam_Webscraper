#include <stdio.h>
#include <string.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <assert.h>
using namespace std;
#include <iostream>
#define forn(i,n) for(int i=0;i<(int)n;i++)
typedef long long ll;
bool pal(ll x)
{
	string s="";
	while(x)
	{
		s+=char(x%10)+'0';
		x/=10;
	}
	string ss=s;
	reverse(ss.begin(),ss.end());
	return s==ss;
}
ll solve2(ll l,ll r)
{
int ans=0;
	for(ll x=max((ll)1,(ll)sqrt(l)-10);x*x<=r;x++)
	{
		if(l<=x*x)
		{
			ans+=pal(x)&&pal(x*x);
			if(pal(x)&&pal(x*x))
			{
				cout<<x<<"LL,";
			}
		}
	}
	return ans;
}
ll a[39]={1LL,2LL,3LL,11LL,22LL,101LL,111LL,121LL,202LL,212LL,1001LL,1111LL,2002LL,10001LL,10101LL,10201LL,11011LL,11111LL,11211LL,20002LL,20102LL,100001LL,101101LL,110011LL,111111LL,200002LL,1000001LL,1001001LL,1002001LL,1010101LL,1011101LL,1012101LL,1100011LL,1101011LL,1102011LL,1110111LL,1111111LL,2000002LL,2001002LL};
ll b[39];
void solve()
{
	ll l,r;
	cin>>l>>r;
	//assert(solve2(l,r)==upper_bound(b,b+39,r)-lower_bound(b,b+39,l));
	cout<<upper_bound(b,b+39,r)-lower_bound(b,b+39,l)<<endl;
}
int main()
{
#define TASK "fas"
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
	int t;
	cin>>t;
	forn(i,39)
		b[i]=a[i]*a[i];
	forn(i,t)
	{
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}