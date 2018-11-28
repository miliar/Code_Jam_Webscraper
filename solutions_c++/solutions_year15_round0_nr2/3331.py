//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)



//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

// my own
#define sl(a) scanf("%lld",&a)
#define sll(a,b) scanf("%lld%lld",&a,&b)
#define slll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sllll(a,b,c,d) scanf("%lld%lld%lld%lld",&a,&b,&c,&d)


ll D;

ll P[1111];
ll Q[1111];

pair<ll,ll> getmx()
{
	ll mx = -1;
	ll idx = -1;
	for(int i = 0; i<D; i++)
	{
		ll val = (P[i]-1)/(1+Q[i])+1;// + Q[i];
		if(mx < val)
		{
			mx = val;
			idx = i;
		}
	}
	return make_pair(idx,mx);
}


bool check(ll t)
{
	//bool debug = t==7;
	repi(i,0,1111) Q[i] = 0;
	do
	{
		if(t<0) return false;
		pll maxo = getmx();
		ll mx = maxo.second;
		ll idx = maxo.first;
		//cout<<"max aaya "<<mx<<endl;
		if(t >= mx)
		{
			//if(debug) cout<<"truee"<<endl;
			return true;
		}
		else
		{
			//if(debug) cout<<"inc "<<idx<<endl;
			Q[idx]++;
			t--;			
		}
		
	}
	while(1);
}

ll bin()
{
	ll hi = 1111;
	ll best = hi;
	ll lo = 0;
	ll mid;
	while(hi-lo>1)
	{
		mid = (hi+lo)/2;
		if(check(mid))
		{
			best = min(best,mid);
			hi = mid;
		}
		else
		{
			lo = mid;
		}
	}
	if(check(hi))
		best = min(best,hi);
	if(check(lo))
		best = min(best,lo);
	return best;
}


int main()
{
	ll test;
	sl(test);
	repii(tt,1,test)
	{
		printf("Case #%lld: ", tt);
		
		cin>>D;
		repi(i,0,D)
		{
			cin>>P[i];
		}
		ll ans = bin();
		printf("%lld\n",ans );
	}
	return 0;
}