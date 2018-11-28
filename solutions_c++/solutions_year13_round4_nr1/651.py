#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <stack>

using namespace std;

struct pt
{
	long long x, end, cnt;

	bool operator < (const pt& p) const 
	{
		if(x != p.x)
			return x < p.x;
		return end < p.end;
	}
};

pt p [1000000];
int sz = 0;

long long mod = 1000002013;

long long f(long long l, long long r)
{
	return (((1ll * (r - l - 1)) % mod) * (r - l) / 2) % mod;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; tt++)
	{
		sz = 0;
		int n, m;
		scanf("%d%d", &n, &m);
		long long init = 0;
		for(int i = 0; i < m; i++)
		{
			long long x, y, cnt;
			scanf("%lld%lld%lld", &x, &y, &cnt);
			init = (init + (f(x, y) * cnt) % mod) % mod;
			
			p[sz].x = x, p[sz].end = 0, p[sz++].cnt = cnt;
			p[sz].x = y, p[sz].end = 1, p[sz++].cnt = cnt;
		}
		sort(p, p + sz);
		long long ans = 0;
		stack<pair<long long, long long> > st;
		for(int i = 0; i < sz; i++)
		{
			if(!p[i].end)
				st.push(make_pair(p[i].x, p[i].cnt));
			else
			{
				long long cnt = p[i].cnt;
				while(cnt > 0)
				{
					long long cn = min(cnt, st.top().second);
					ans = ((cn * f(st.top().first, p[i].x)) % mod + ans) % mod; 
					st.top().second -= cn;
					if(st.top().second == 0)
						st.pop();
					cnt -= cn;
				}
			}
		}
		printf("Case #%d: %lld\n", tt + 1, (ans - init + mod) % mod);
	}

	return 0;
}