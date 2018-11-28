#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <cctype>
#include <cstdio>
#include <memory>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>

#define sqr(x) ((x) * (x))
#define minn(x,y) (x=(y)<(x)?(y):(x))
#define maxx(x,y) (x=(y)>(x)?(y):(x))
#define pluss(x,y) (x+=(y),x%=mod)
#define random(x) ((((rand()%32767)*(rand()%32767)*(rand()%32767)%(x))+(x))%(x))

using namespace std;

typedef	long long	int64;

const	int	mod = 1000002013;


vector<int64>	x;
int64	s[2222], t[2222], p[2222], u[2222], d[2222], f[2222], N, M;


int64	calcCost(int64 len)
{
	return (N + N - len + 1) * len / 2 % mod;
}

int	main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int	Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; ++ test)
	{
		x.clear();
		
		int64	ans0 = 0;
		scanf("%I64d%I64d", &N, &M);
		for (int i = 1; i <= M; ++ i)
		{
			scanf("%I64d%I64d%I64d", &s[i], &t[i], &p[i]);
			x.push_back(s[i]);
			x.push_back(t[i]);
			ans0 = (ans0 + calcCost(t[i] - s[i]) * p[i]) % mod;
		}
		
		sort(x.begin(), x.end());
		x.resize( unique(x.begin(), x.end()) - x.begin() );
		
		memset(u, 0, sizeof(u));
		memset(d, 0, sizeof(d));
		for (int i = 1; i <= M; ++ i)
		{
			s[i] = lower_bound(x.begin(), x.end(), s[i]) - x.begin();
			t[i] = lower_bound(x.begin(), x.end(), t[i]) - x.begin();
			u[s[i]] += p[i];
			d[t[i]] += p[i];
		}
		
		int64	ans1 = 0;
		memset(f, 0, sizeof(f));
		for (int i = 0; i < x.size(); ++ i)
		{
			f[i] += u[i];
			
			for (int j = i; j >= 0 && d[i]; -- j)
			{
				int64	C = min(f[j], d[i]);
				ans1 = (ans1 + C * calcCost(x[i] - x[j])) % mod;
				d[i] -= C;
				f[j] -= C;
			}
		}
		
		printf("Case #%d: %I64d\n", test, (ans0 - ans1 + mod) % mod);
	}
	
	return 0;
}
