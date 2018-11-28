#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <functional>

#define rep(i,n) for(int i=0;i<(n);++i)
#define foreach(i,v) for(__typeof(v.begin()) i=v.begin();i!=v.end();++i)
#define ass(v) (v)||++*(int*)0;

using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<double> VD;
typedef long long LL;

LL B, X[100];
int N;

double solve_old()
{
	double ans = 0.0;
	LL c = 0;
	while (true)
	{
		sort(X, X + 37);
		LL min1 = X[0], min2 = X[1];
		for (int i = 1; i < 37; ++i)
		{
			if (X[i] != min1)
			{
				min2 = X[i];
				break;
			}
		}

		if (min1 == min2)
		{
			LL h = (B - c) / 37;
			c += h * 37;
			double win = c * (36.0 / 37.0 - 1.0);
//			printf("h=%I64d win=%f\n", h, win);
			ans = max(ans, win);
			break;
		}

		int d1 = 0;
		for (int i = 0; i < 37; ++i)
		{
			if (X[i] == min1) ++d1;
		}
		LL h1 = min((B - c) / d1, min2 - min1 - 1);
		//if (h1 == 0) break;
		c += h1 * d1;
		double win1 = c * (36.0 / d1 - 1.0);
		ans = max(ans, win1);
//		printf("min1=%I64d min2=%I64d\n", min1, min2);
//		printf("c=%I64d d1=%d win1=%f\n", c, d1, win1);
		for (int i = 0; i < 37; ++i)
		{
			if (X[i] == min1) X[i] += h1;
		}
		if (h1 != min2 - min1 - 1) break;

		int d2 = 0, e2 = 0;
		for (int i = 0; i < 37; ++i)
		{
			if (X[i] <= min2) ++d2;
			if (X[i] == min2 - 1) ++e2;
		}
		if (e2 > B - c) break;
		c += e2;
		double win2 = c * (36.0 / d2 - 1.0);
//		printf("c=%I64d d2=%d e2=%d win2=%f\n", c, d2, e2, win2);
		ans = max(ans, win2);
		for (int i = 0; i < 37; ++i)
		{
			if (X[i] == min2 - 1) ++X[i];
		}
	}
	return ans;
}

LL fit1(LL h, int d)
{
	LL sum = 0;
	for (int i = 0; i < d; ++i) sum += h - X[i];
	return sum;
}

LL fit2(LL h, int d)
{
	LL sum = 0;
	for (int i = d; i < 37; ++i) sum += max(0LL, h + 1 - X[i]);
	return sum;
}

LL hei(int d)
{
	LL st = X[d - 1], ed = 1000000000000000LL;
	while (st <= ed)
	{
		LL md = (st + ed) / 2;
		LL sum = fit1(md, d) + fit2(md, d);
//		printf("st=%I64d ed=%I64d md=%I64d sum=%I64d\n", st, ed, md, sum);
		if (sum <= B)
		{
			st = md + 1;
		}
		else
		{
			ed = md - 1;
		}
	}
	return ed;
}

double solve()
{
	double ans = 0.0;
	for (int d = 1; d <= 35; ++d)
	{
		vector<LL> hs;
		hs.push_back(X[d - 1]);
		for (int i = d; i < 37; ++i)
		{
			hs.push_back(max(X[i] - 1, 0LL));
			hs.push_back(X[i]);
		}
		hs.push_back(hei(d));
		//sort(hs.begin(), hs.end());
//		printf("d=%d\n", d);
		foreach(it, hs)
		{
			LL h = *it;
			LL c1 = fit1(h, d);
			LL c2 = fit2(h, d);
			if (c1 + c2 > B) continue;
			double win = c1 * (36.0 / d - 1.0) - c2;
			ans = max(win, ans);
//			printf("h=%I64d win=%f\n", h, win);
		}
	}
//	printf("!! %I64d %I64d\n", fit1(390, 35), fit2(390, 35));
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs)
	{
		scanf("%I64d%d", &B, &N);
		memset(X, 0, sizeof(X));
		for (int i = 0; i < N; ++i) scanf("%I64d", &X[i]);
		sort(X, X + 37);
//	printf("%I64d\n", hei(35));
		double ans = solve();
		printf("Case #%d: %.14f\n", cs, ans);
	}
	return 0;
}
