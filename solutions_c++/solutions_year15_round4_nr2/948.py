#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cassert>
#include <unordered_map>

using namespace std;
typedef long long ll;
#define MODD(a,b) (((a)%(b)+(b))%(b))
#define EPS 1E-9
#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

unordered_map < string, int> m;

inline bool getbit(int x, int p)
{
	return (bool)(x & (1 << p));
}

int readint()
{
	char c;
	int ans=0;
	while (1)
	{
		cin >> c;
		if (c == '.') break;
		ans = ans * 10 + c - '0';
	}
	for (int i = 0; i < 4; i++)
	{
		cin >> c;
		ans = ans * 10 + c - '0';
	}
	return ans;
}

int main()
{
	int __t;
	cin >> __t;

	for (int cs = 1; cs <= __t; cs++)
	{
		printf("Case #%d: ", cs);
		
		int n; cin >> n;
		int v, x;
		v = readint();
		x = readint();
		vector<int> r;
		vector<int> c;
		r.resize(n);
		c.resize(n);
		for (int i = 0; i < n; i++)
		{
			r[i] = readint();
			c[i] = readint();
		}

		double ans=0;
		if (n == 1)
		{
			if (x == c[0]) ans = (double)v / r[0];
			else ans = -1;
		}
		else
		{
			if (c[0]>c[1])
			{
				swap(c[0], c[1]);
				swap(r[0], r[1]);
			}

			if (c[0] == c[1])
			{
				if (x == c[0]) ans = (double)v / (r[0]+r[1]);
				else ans = -1;
			}
			else
			{
				if (x >= c[0] && x <= c[1])
				{
					double p0, p1;
					p0 = (double)(c[1] - x) / (c[1] - c[0]);
					p1 = (double)(x - c[0]) / (c[1] - c[0]);
					ans = max((double)v*p0 / r[0], (double)v*p1 / r[1]);
				}
				else ans = -1;
			}
		}


		cerr<<"Case "<<cs<<" :";
		cerr << ans << endl;
		if (ans <0) puts("IMPOSSIBLE");
		else printf("%.9f\n", ans);
	}

	
	return 0;
}