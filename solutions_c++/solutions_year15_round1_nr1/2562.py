#include <bits/stdc++.h>
using namespace std;

int m[1001];

int main() {
	int t, n;
	long long sum1, sum2, maxr;

	scanf("%d",&t);

	for (int j = 0; j < t; ++j) {
		scanf("%d", &n);

		sum1 = sum2 = maxr = 0;

		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &m[i]);

			if(i != 0) {
				sum1 += (m[i] - m[i-1] < 0) ? m[i-1] - m[i] : 0;

				maxr = (m[i-1] - m[i] > maxr) ? m[i-1] - m[i] : maxr;
			}

		}

		for (int i = 0; i < n-1; ++i)
		{
			if(m[i] <= maxr) sum2 += m[i];
			else sum2 += maxr;
		}

		printf("Case #%d: %lld %lld\n", j+1, sum1, sum2);
	}


	return 0;
}