//#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <cassert>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <bitset>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>
#include <complex>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<ll> vint;
typedef vector<vint> vvint;
typedef pair<ll, ll> pii;

#define FOR(i,a,b) for(int i=a; i < b; ++i)
#define RFOR(i,a,b) for(int i=a; i >= b;--i)
#define REP(i, n) FOR(i, 0, n)
#define FILL(A,value) memset(A,value,sizeof(A))
#define pb push_back
#define mp make_pair
#define sz(x) ((ll)(x).size())
#define all(x) (x).begin(), (x).end()

#define eps 1.0E-6
#define PI acos(-1.0)
#define MOD 1000000007
#define maxn 100012

ll calc(ll n, ll i)
{
	set<int> d;
	while(d.size()<10)
	{
		ll num=n*i;
		while(num>0)
		{
			int d1=num%10;
			num/=10;
			d.insert(d1);
			
		}
		if (d.size()>=10)return n*i;
		else i++;
	}
}
int main()
{
#ifdef LOCAL_HOST
	assert(freopen("A-large.in","r",stdin));
	
	assert(freopen("output.txt","w",stdout));
#endif
	ll n,t;
	cin >> t;
	REP(t1,t)
	{
		cin >> n;
		printf("Case #%d: ", t1+1);
		if(n==0) 
		{
			printf("%s\n","INSOMNIA");
			continue;
		}
		else
		{
			printf("%lld\n", calc(n,1));
		}
	}
	return 0;
}