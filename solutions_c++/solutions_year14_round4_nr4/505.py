#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>
#include <numeric>
#include <ctime>
#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <stack>
#include <string>
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
char nextchar(){char a[8];scanf("%s",a);return a[0];}
int nextint(){int a;scanf("%d",&a);return a;}
ll nextll(){ll a;scanf("%lld",&a);return a;}
double nextdouble(){double a;scanf("%lf",&a);return a;}

int cpow(int a, int p)
{
	int res = 1;
	while(p--)
		res *= a;
	return res;
}

vector<int> v;
vector<string> vs;
int base;

void add()
{
	int add = 1;
	for(int i = 0; i < v.size(); i++)
	{
		v[i] += add;
		add = v[i] / base;
		v[i] %= base;
	}
}

int asz;
class trie
{
public:
	map<char, int> mp;

	void add(string &s, int i)
	{
		if(i == s.size()) return;
		if(mp.count(s[i]) == 0)
		{
			mp[s[i]] = asz;
			a[asz].mp.clear();
			asz++;
		}
		a[mp[s[i]]].add(s, i+1);
	}

	int size()
	{
		int res = 1;
		for(map<char, int>::iterator it = mp.begin(); it != mp.end(); it++)
			res += a[it->second].size();
		return res;
	}

} a[1<<10];
int root;

int solve(int c)
{
	asz = 1;
	a[root].mp.clear();

	int cc = 0;
	for(int i = 0; i < v.size(); i++)
	{
		if(v[i] == c)
		{
			cc++;
			a[root].add(vs[i], 0);
		}
	}

	if(cc == 0) return 0;

	return a[root].size();
}

int cnt[8];

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t = nextint();
	for(int test = 1; test <= t; test++)
	{
		int m = nextint();
		int n = nextint();
		vs = vector<string> (m);

		for(int i = 0; i < m; i++)
			cin >> vs[i];

		v = vector<int> (m);
		base = n;
		

		int c = cpow(n, m);

		int res = -1;
		int resc = 0;
		while(c--)
		{
			int cur = 0;
			for(int i = 0; i < n; i++)
			{
				cur += solve(i);
			}

			if(cur > res)
			{
				res = cur;
				resc = 1;
			}
			else if(cur == res)
				resc++;

			add();
		}


		printf("Case #%d: %d %d\n", test, res, resc);
	}

	return 0;
}