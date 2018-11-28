#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



long long X[105];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int n;
		long long b;
		int N = 37;
		scanf("%lld%d", &b, &n);
		long long maxX = 0;
		memset(X, 0, sizeof X);

		for (int i = 0; i < n; i++)
		{
			scanf("%lld", &X[i] );
			maxX = max(maxX, X[i] );
		}
		long long l = 0, r = maxX + 1;
		while (r - l > 1)
		{
			long long m = (l + r) / 2;
			long long need = 0;
			for (int i = 0; i < N; i++)
			{
				long long cur = m - X[i];
				if (cur > 0)
					need += cur;
			}
			if (need > b)
				r = m;
			else
				l = m;
		}
		
		double ans = 0;
		for (long long L = max(l - 100, 0LL); L <= l; L++)
		{		
			long long sum = 0;
			int count = 0;

			vector <long long> geted;

			for (int i = 0; i < N; i++)
			{
				if (X[i] <= L)
				{
					sum += L - X[i];
					geted.push_back(L - X[i] );
				}
			}
			sort(geted.begin(), geted.end() );
			reverse(geted.begin(), geted.end() );

			if (geted.size() != 0)
			{
				long long maxAddOne = min(b - sum, (long long) geted.size() );
				long long sumG = 0;
				int minCount = geted.size() - maxAddOne - 1;
				for (int i = 0; i < geted.size(); i++)
				{
					sumG += geted[i];
					long long pay = sum + (geted.size() - i - 1);
					if (pay > b && i >= minCount)
						throw 42;
					double curans = 36. * double(sumG) / double(i + 1) - (double)pay;
					if (curans > ans && i >= minCount)
						ans = curans;
				}
			}
		}
		printf("Case #%d: %.10lf\n", t, ans);
	}


	return 0;
}