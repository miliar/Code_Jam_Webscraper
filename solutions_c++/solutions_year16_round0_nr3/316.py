#include <set>
#include <queue>
#include <cassert>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <utility>
#include <algorithm>
#include <iterator>
#include <numeric>
using namespace std;

typedef long long ll;

ll getDivisor(ll x)
{
	for(ll i=2;i*i<=x;i++)
		if(x%i==0)
			return i;
	return -1;
}

ll parse(const string& x, int base)
{
	ll res=0;
	for(int i=0;i<x.size();i++)
		res=res*base+x[i]-'0';
	return res;
}

ll gcd(ll a, ll b)
{
	return b? gcd(b,a%b):a;
}

int main()
{
	int n,j;
	n=16;
	j=500;
	vector<string> last;
	vector<string> res;
	vector<vector<ll> > proof;
	for(int i=0;i<(1<<(n-2)) && res.size()<j;i++)
	{
		string cur="1";
		for(int j=0;j<n-2;j++)
			cur+=((i>>j)&1)+'0';
		cur+="1";
		if(parse(cur,1)%6!=0) continue;
		vector<ll> cp;
		for(int b=2;b<=10;b++)
		{
			ll x=parse(cur, b);
			ll d=getDivisor(x);
			if(d==-1)
			{
				cp.clear();
				break;
			}
			cp.push_back(d);
		}
		if(!cp.empty())
		{
			last.push_back(cur);
			for(int i=0;i<last.size();i++)
			{
				cp.clear();
				for(int b=2;b<=10;b++)
				{
					ll g=gcd(parse(cur,b), parse(last[i],b));
					if(g==1)
					{
						cp.clear();
						break;
					}
					cp.push_back(g);
				}
				if(!cp.empty())
				{
					res.push_back(cur+last[i]);
					proof.push_back(cp);
					if(i!=last.size()-1)
					{
						res.push_back(last[i]+cur);
						proof.push_back(cp);
					}
				}
			}
		}
	}
	printf("Case #%d:\n",1);
	for(int i=0;i<j;i++)
	{
		printf("%s",res[i].c_str());
		for(int j=0;j<proof[i].size();j++)
			printf(" %lld",proof[i][j]);
		puts("");
	}
}
