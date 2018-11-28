#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;



int hid = 1;
struct H
{
	int id;
	int s, t;
	int curf;
	H() : id(), s(), t(), curf() {}
	H(int _s, int _t) : id(hid++), s(_s), t(_t), curf(0) {}
	
	long long getNextT() const
	{
		return getFinT() + curf * 360LL * t;
	}
	long long getFinT() const
	{
		return (360LL - s) * 1LL * t;
	}
	bool operator < (const H &A) const
	{
		long long a = getNextT();
		long long b = A.getNextT();
		if (a != b)
			return a < b;
		if (curf != A.curf)
			return curf > A.curf;
		return id < A.id;
	}
};

set <H> hs;


void solve()
{
	int n;
	scanf("%d", &n);
	hs.clear();

	int all = 0;
	for (int i = 0; i < n; i++)
	{
		int d, h, m;
		scanf("%d%d%d", &d, &h, &m);
		all += h;
		for (int j = 0; j < h; j++)
		{
			hs.insert(H(d, m + j) );
		}
	}

	int ans = all;
	int one = 0;
	int cnt = 0;
	while (cnt < ans)
	{
		H cur = *hs.begin();
		hs.erase(*hs.begin() );
		long long curt = cur.getNextT();
		if (cur.curf == 0)
		{
			one++;
			cur.curf++;
			hs.insert(cur);
			if (hs.begin()->getNextT() > curt)
				ans = min(ans, all - one + cnt);
		}
		else
		{
			cur.curf++;
			hs.insert(cur);
			cnt++;
		}
	}
	printf("%d\n", ans);
/*
	long long ans = (int) hs.size();
	sort(hs.begin(), hs.end() );
	for (int i = 0; i < (int) hs.size(); i++)
	{
		double t = hs[i].getFinT();
		long long cur = 0;
		for (int j = 0; j < (int) hs.size(); j++)
		{
			if (Gr(hs[j].getFinT(), t) )
				cur++;
			else
				cur += hs[j].cnt(t) - 1;
		}
//		eprintf("i = %d, cur = %lld, t = %.5lf\n", i, cur, t);
		ans = min(ans, cur);
	}
	printf("%lld\n", ans);
*/
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		eprintf("Case %d .. %d\n", i, t);
		printf("Case #%d: ", i);
		solve();
	}
	

	return 0;
}
