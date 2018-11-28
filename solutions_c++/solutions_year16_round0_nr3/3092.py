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
#include <memory.h>

#include <time.h>
#pragma comment(linker, "/STACK:100000000")
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(x) (int)(x).size()
#define ll long long
#define fr(i,a,b) for(int i = (a);i <= (b);i++)
#define fd(i,a,b) for(int i = (a);i >= (b);i--)

int ri(){int x;scanf("%d",&x);return x;}

vector<pair<string,vector<ll> > > path;
int n,j;
string s;

#define lnum vector<ll>

const ll MOD = 1e9;

void add(lnum &a,ll k)
{
	a[0] += k;
	int pos = 0;
	while(a[pos] >= MOD)
	{
		ll ost = a[pos] / MOD;
		a[pos] %= MOD;
		if (pos + 1 > a.size())
			a.pb(0);
		a[pos + 1] += ost;
		pos++;
	}
}

void mul(lnum &a,ll k)
{
	ll ost = 0;
	for(int i = 0;i < a.size() || ost;i++)
	{
		if (i == a.size())
			a.pb(0);
		ll tmp = ost + a[i] * k;
		a[i] = tmp % MOD;
		ost = tmp / MOD;
	}
}

bool isDeleted(lnum &a,ll k)
{
	ll ost = 0;
	for(int i = a.size() - 1;i >= 0;i--)
	{
		ost *= MOD;
		ost += a[i];
		ost %= k;
	}
	return ost == 0;
}

void check()
{
	vector<ll> ok;
	for(ll k = 2;k <= 10;k++)
	{
		//ll x = 0;
		//for(int i = n - 1;i >= 0;i--)
		//	x *= k,x += s[i] - '0';

		lnum x(1);
		for(int i = n - 1;i >= 0;i--)
		{
			mul(x,(ll)k);
			add(x,s[i] - '0');
		}

		bool flag = false;
		for(ll i = 2;i <= 1000;i++)
		{
			if (isDeleted(x,i))
			{
				flag = true;
				ok.pb(i);
				break;
			}
			/*if (x % i == 0)
			{
				flag = true;
				ok.pb(i);
				break;
			}*/
		}
		if (!flag)
			return;
	}
	path.pb(mp(s,ok));
}

void go()
{
	if (path.size() == j)
		return;
	if (s.length() + 1 == n)
	{
		s += '1';
		check();
		s.pop_back();
		return;
	}
	s += '0';
	go();
	s.pop_back();
	s += '1';
	go();
	s.pop_back();
}

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		n = ri(),j = ri();
		s += '1';
		go();
		cout << "Case #1: " << endl;
		for(int i = 0;i < j;i++)
		{
			reverse(path[i].first.begin(),path[i].first.end());
			cout << path[i].first;
			for(int k = 0;k < path[i].second.size();k++)
				cout << " " << path[i].second[k];
			cout << endl;
		}
	}
}

int main()
{
    #ifndef ONLINE_JUDGE
			freopen("C:/Users/WhiteDevil/Desktop/input.txt","rt",stdin);
			freopen("C:/Users/WhiteDevil/Desktop/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif
	
	solve();

    return 0;
}