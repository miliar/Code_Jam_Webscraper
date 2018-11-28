#if 0==0

#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>

using std::vector;
using std::string;

int main()
{
	vector<int> p;

	freopen("C-large.in", "r", stdin);
	freopen("C-large_mine.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i_case = 1 ; i_case <= n ; i_case++)
	{	
		//printf("d=%d\n",d);
		int N, J;
		scanf("%d%d", &N, &J);

		printf("Case #%d:\n", i_case);

		unsigned long long d = 1;
		
		for (int i = 0 ; i < N - 2 ; i++) d <<= 1;

		for (unsigned long long i = 0 ; i < d ; i++)
		{
			unsigned long long dd = ((d + i) << 1) + 1;
			bool ok = true;
			vector<unsigned long long> ans;
			for (int base = 2 ; base <= 10 ; base++)
			{
				unsigned long long ddd = dd;
				unsigned long long t = 0;
				while (ddd)
				{
					t *= base;
					t += ddd & 1;
					ddd >>= 1;
				}

				//if (dd == 27) printf("[%d, %d]", base, t);

				bool isPrime = true;
				unsigned long long sq = sqrt((double)t + 1);
				unsigned long long k;
				for (k = 2 ; k <= sq ; k++)
					if (t % k == 0)
					{
						isPrime = false;
						break;
					}

				if (isPrime) { ok = false; break; } else ans.push_back(k);
			}

			if (ok)
			{
				//printf("(%d)", dd);
				for (unsigned long long i = 0 ; i < N ; i++)
					printf("%d", (dd & (1 << i)) ? 1 : 0);
				
				for (int i = 0 ; i < ans.size() ; i++)
					printf(" %u", ans[i]);
				printf("\n");
				J--;
				if (J == 0) break;
			}
		}
	}

	return 0;
}

#endif