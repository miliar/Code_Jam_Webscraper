#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <ctime>
#include <vector>

using namespace std;

template <typename T> T sqr(T x) { return x * x; }
template <typename T> T abs(T x) { return x < 0? -x : x; }


vector <long long> x;
long long b;
long double ans = 0;

long double f(long long v)
{
	vector <long long> d;
	long long r = b;
	int c = 0;
	for (int i = 0; i < (int)x.size() && r >= 0; i++)
	{
		d.push_back(max(x[i], v));
		c += d[i] == v;
		r -= d[i] - x[i];
	}
	if (c == 0)
		return 0;

	if (r < 0)
		return -1;
		
	vector <long long> a;
	for (int i = 0; i < (int)x.size(); i++)
		if (d[i] == v)
			a.push_back(36 * (d[i] - x[i]));
	sort(a.rbegin(), a.rend());
	
	long double ans = 0;
	long long s = 0;
	for (int i = 0; i < (int)a.size(); i++)
	{
		s += a[i];
		if ((int)a.size() - i - 1 > r)
			continue;
		ans = max(s / (long double)(i + 1) + r - ((int)a.size() - i - 1), ans);
	}
	return ans - b;
}


void run(long long l, long long r)
{
	if (l > r)
		return;
	while (l < r)
	{
		long long c = (l + r) / 2;
		if (f(c) + 1e-7 > f(c + 1))
			r = c;
		else
			l = c + 1;
	}
	ans = max(ans, f(r));
}

int main()
{
	#ifdef MJUDGE
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif

	int T;
	scanf("%d", &T);
	cout.precision(10);
	for (int t = 1; t <= T; t++, printf("\n"))
	{
		printf("Case #%d: ", t);
		int n;
		cin >> b >> n;
		x.resize(37);
		for (int i = 0; i < (int)x.size(); i++)
			x[i] = 0;
		for (int i = 0; i < n; i++)
			cin >> x[i];
			
		ans = 0;
		sort(x.begin(), x.end());
		for (int i = 1; i < (int)x.size(); i++)
			run(x[i - 1], x[i] - 1);
		run(x[(int)x.size() - 1], (long long)1e+16);
		cout << fixed << ans;
	}
	fprintf(stderr, "Time execute: %.3lfs\n", clock() / (double)CLOCKS_PER_SEC);
	return 0;
}
