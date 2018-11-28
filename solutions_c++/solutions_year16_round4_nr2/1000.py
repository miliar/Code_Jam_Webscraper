#include<cstdio>
#include <cstring>
#include<string>
#include<algorithm>
using namespace std;
int k;
int ps[222];
double ans[222];
double p[222];
double calc()
{
	memset(ans, 0, sizeof ans);
	ans[0] = 1.0;
	for (int i = 0; i < k; ++i)
	{
		for (int j = i+1; j >= 0; --j)
			ans[j] = ans[j]*(1-p[ps[i]]) + ((j)?(ans[j-1]*p[ps[i]]):0.0);
	}
	return ans[k/2];
}
double get_ans(int num, int ls)
{
	if (num == 0)
	{
		if (ls)
			ps[0] = 0;
		return calc();
	}
	double ret = 0;
	if (ls <= num)
		ret = get_ans(num-1, ls);
	if (ls)
	{
		ps[ls-1] = num;
		double ret2 = get_ans(num-1, ls-1);
		if (ret2 > ret) ret = ret2;
	}
	return ret;
}
int main(int argc, char** argv)
{
	if (argc > 2)
	{
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}
	int T, n;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i)
			scanf("%lf", p+i);
		printf("Case #%d: %lf\n", t, get_ans(n-1,k));
	}
	return 0;
}