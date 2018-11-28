#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>


double tieProb(const std::vector<double> & p)
{
	std::vector<double> f(p.size() + 1, 0.0);
	f[0] = 1.0;

	for(int i = 0; i < (int)p.size(); i++)
	{
		for(int j = (int)f.size() - 1; j > 0; j--)
			f[j] = f[j] * (1.0 - p[i]) + f[j - 1] * p[i];
		f[0] = (1.0 - p[i]) * f[0];
	}

	return f[p.size() / 2];
}

double naive(const int k, std::vector<double> p)
{
	double res = 0.0;
	const int n = (int)p.size();
	const int border = 1 << n;
	for(int mask = 1; mask < border; mask++)
	{
		std::vector<double> tmp;
		for(int i = 0; i < n; i++)
			if(mask & (1 << i))
				tmp.push_back(p[i]);

		if(k == (int)tmp.size())
			res = std::max(res, tieProb(tmp));
	}
	return res;
}

double solve(const int k, std::vector<double> p)
{
	std::sort(p.begin(), p.end());

	double res = 0.0;
	for(int i = 0; i <= k; i++)
	{
		std::vector<double> tmp;
		for(int j = 0; j < i; j++)
			tmp.push_back(p[j]);
		for(int j = 0; j < k - i; j++)
			tmp.push_back(p[p.size() - 1 - j]);

		assert((int)tmp.size() == k);
		res = std::max(res, tieProb(tmp));
	}

	return res;
}

int main()
{
	int tests;
	scanf("%i\n", &tests);

	for(int test = 1; test <= tests; test++)
	{
		printf("Case #%i: ", test);

		int n, k;
		scanf("%i %i\n", &n, &k);

		std::vector<double> p;
		for(int i = 0; i < n; i++)
		{
			double tmp;
			scanf("%lf", &tmp);
			p.push_back(tmp);
		}

		printf("%0.8lf\n", solve(k, p));
	}

	return 0;
}

