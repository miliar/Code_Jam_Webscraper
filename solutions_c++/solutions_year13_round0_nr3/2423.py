#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>

#include <time.h>
#pragma comment(linker, "/STACK:20000000")

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define mp make_pair
#define pb push_back
#define ll long long

using namespace std;

int ri(){int x;scanf("%d",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}

bool palindrome(ll x)
{
	vector<int> st;
	while(x)
		st.pb(x%10),x/=10;
	fr(i,0,st.size()/2)
		if (st[i]!=st[st.size()-1-i])
			return false;
	return true;
}

void solve()
{
	int test = ri();
	vector<ll> st;
	st.pb(1);
	st.pb(4);
	st.pb(9);
	st.pb(121);
	st.pb(484);
	st.pb(10201);
	st.pb(12321);
	st.pb(14641);
	st.pb(40804);
	st.pb(44944);
	st.pb(1002001);
	st.pb(1234321);
	st.pb(4008004);
	st.pb(100020001);
	st.pb(102030201);
	st.pb(104060401);
	st.pb(121242121);
	st.pb(123454321);
	st.pb(125686521);
	st.pb(400080004);
	st.pb(404090404);
	st.pb(10000200001);
	st.pb(10221412201);
	st.pb(12102420121);
	st.pb(12345654321);
	st.pb(40000800004);
	st.pb(1000002000001);
	st.pb(1002003002001);
	st.pb(1004006004001);
	st.pb(1020304030201);
	st.pb(1022325232201);
	st.pb(1024348434201);
	st.pb(1210024200121);
	st.pb(1212225222121);
	st.pb(1214428244121);
	st.pb(1232346432321);
	st.pb(1234567654321);
	st.pb(4000008000004);
	st.pb(4004009004004);
	fr(testing,1,test)
	{
		ll l = rll(), r = rll();
		ll res = 0;
		/*for(ll i = 1;i<=10000000;i++)
			if (i*i>=l && i*i<=r && palindrome(i) && palindrome(i*i))
				st.pb(i*i);
		fr(i,0,(int)st.size()-1)
		{
			printf("st.pb(%lld);\n",st[i]);
		}*/
		fr(i,0,st.size()-1)
			if (st[i]>=l && st[i]<=r)
				res++;
		printf("Case #%d: %lld\n",testing,res);
	}
}

int main()
{
	/*#ifndef ONLINE_JUDGE
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/input.txt","rt",stdin);
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif*/

	solve();

	/*#ifndef ONLINE_JUDGE
		printf("\n\ntime-%.3lf",clock()*1e-3);
	#endif*/
	return 0;
}