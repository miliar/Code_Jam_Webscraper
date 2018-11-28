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
#pragma comment(linker, "/STACK:20000000")

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define mp make_pair
#define pb push_back
#define ll long long

using namespace std;

int ri(){int x;scanf("%d",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}

bool neg[10050];
char pre[10050];

char mul(char a,char b,bool &c)
{
	if (a == '1')
		return b;
	if (b == '1')
		return a;
	if (a == b)
	{
		c ^= 1;
		return '1';
	}
	if (a == 'i')
	{
		if (b == 'j')
			return 'k';
		c ^= 1;
		return 'j';
	}
	if (a == 'j')
	{
		if (b == 'k')
			return 'i';
		c ^= 1;
		return 'k';
	}
	if (a == 'k')
	{
		if (b == 'i')
			return 'j';
		c ^= 1;
		return 'i';
	}
}

string wtf = "1ijk";

char rev_mul(char a,bool ab,char b,bool bb,bool &ok)
{
	for(int j = 0;j < 4;j++)
	{
		for(int k = 0;k < 2;k++)
		{
			bool c = ab ^ (bool)k;
			char q = mul(a,wtf[j],c);
			if (q == b && c == bb)
			{
				ok = (bool)k;
				return wtf[j];
			}
		}
	}
}

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		int n = ri(),r = ri();
		string ss;
		cin >> ss;
		string s;
		while(r--)
			s += ss;
		memset(neg,false,sizeof(neg));
		bool res = false;
		pre[0] = s[0];
		for(int i = 1;i < s.length();i++)
		{
			pre[i] = mul(pre[i - 1],s[i],neg[i]);
			neg[i] ^= neg[i - 1];
		}
		for(int i = 0;i < s.length();i++)
		{
			if (pre[i] != 'i' || neg[i])
				continue;
			for(int j = i + 1;j < s.length();j++)
			{
				bool wt = false;
				char c = rev_mul('i',false,pre[j],neg[j],wt);
				if (c != 'j' || wt)
					continue;
				wt = false;
				c = rev_mul(pre[j],neg[j],pre[s.length() - 1],neg[s.length() - 1],wt);
				if (c == 'k' && wt == false)
				{
					res = true;
					goto mark;
				}
			}
		}
		mark:res = res;
		printf("Case #%d: %s\n",testing,res ? "YES" : "NO");
	}
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/input.txt","rt",stdin);
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif

	solve();

	#ifndef ONLINE_JUDGE
		printf("\n\ntime-%.3lf",clock()*1e-3);
	#endif

	return 0;
}