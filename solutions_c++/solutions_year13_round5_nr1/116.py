#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

long long vx[40];

double Work()
{
	long long B, lx;
	int n, ln = 0;
	cin >> B >> n;
	for (int i = 0; i < n; i ++)
		cin >> vx[i];
	sort(vx, vx + n);
	lx = vx[0];
	for (int i = 0; i < n; i ++)
		ln += vx[i] == lx;
	double ans = 0.0;


	for (int k = 0; k <= n; k ++)
	{
		long long ll = 0, rr = 1LL << 40, lt;
		while (ll < rr)
		{
			lt = (ll + rr + 1) >> 1;
			{
				long long sum = 0, num = 0;
				double prof = 0.0;

				for (int i = 0; i < n; i ++)
					if (vx[i] <= lt)
					{
						sum += lt - vx[i] + (i >= k);
						num += i < k;
					}

				sum += (37 - n) * lt;
				num += 37 - n;

				if (sum > B)
				{
					rr = lt - 1;
				}
				else 
				{
					ll = lt;
					for (int i = 0; i < k; i ++)
						if (vx[i] <= lt)
							prof += lt - vx[i];

					prof += (37 - n) * lt;
					prof *= 36.0 / num;

					ans = max(ans, prof - sum);
				}
			}
		}
	}

	return ans;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-output.txt", "w", stdout);

	int T;
	cin >> T;
	cout.precision(10);
	for (int tt = 1; tt <= T; tt ++)
	{
		cout << "Case #" << tt << ": ";
		printf("%.10f\n", Work());
	}

	return 0;
}