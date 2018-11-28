#include <stdio.h>
#include <algorithm>
#include <functional>
#include <cmath>
using namespace std;

long long b;
long long x[38];
int n;
int m=37;

int main()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);
	while (t--) {
		for (int i=0; i<m; i++) x[i]=0;

		scanf("%lld%d", &b, &n);
		for (int i=0; i<n; i++)
			scanf ("%lld", &x[i]);

		sort(x, x+m, greater<int>());
		double ans=0;
		
		for (int i=0; i<m; i++) {
			if (i && x[i] == x[i-1]) continue;

			long long s = 0;
			for (int j=i; j<m; j++) s += x[i] - x[j];
			if (s <= b) {
				long long t = (b-s) / (m-i);
				long long r;
				if (i && t + x[i] >= x[i-1]) t = x[i-1] - x[i] - 1, r = m-i-1;
				else r = b - s - t*(m-i);

				for (int k=0; k<=r; k++) {
					double profit = 0;
					long long loss = 0;
					for (int l=i; l<i+k; l++)
						loss += t + x[i]-x[l] + 1;
					for (int l=i+k; l<m; l++)
						loss += t + x[i]-x[l], profit += x[i]+t - x[l];
					profit *= 36.0 / (m-i-k);
					if (profit - loss >= ans)
						ans = profit - loss;
				}
				
				t = (b-s) / (m-i) - 1;
				if (i && t + x[i] >= x[i-1]) t = x[i-1] - x[i] - 1, r = m-i-1;
				else r = min (b - s - t*(m-i), (long long)m-i-1);

				if (t) {
					for (int k=0; k<=r; k++) {
						double profit = 0;
						long long loss = 0;
						for (int l=i; l<i+k; l++)
							loss += t + x[i]-x[l] + 1;
						for (int l=i+k; l<m; l++)
							loss += t + x[i]-x[l], profit += x[i]+t - x[l];
						profit *= 36.0 / (m-i-k);
						if (profit - loss >= ans)
							ans = profit - loss;
					}
				}

				t=0, r = min (b - s, (long long)m-i-1);

				for (int k=0; k<=r; k++) {
					double profit = 0;
					long long loss = 0;
					for (int l=i; l<i+k; l++)
						loss += t + x[i]-x[l] + 1;
					for (int l=i+k; l<m; l++)
						loss += t + x[i]-x[l], profit += x[i]+t - x[l];
					profit *= 36.0 / (m-i-k);
					if (profit - loss >= ans)
						ans = profit - loss;
				}
			}
		}

		printf ("Case #%d: %.10lf\n", ++tt, ans);
	}

	return 0;
}
