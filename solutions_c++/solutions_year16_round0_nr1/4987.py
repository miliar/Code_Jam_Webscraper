#include <iostream>
#include <stdio.h>
#include <cstring>

using namespace std;

int N;
long long arr[11];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);
	int ts = 1;
	while (T--)
	{
		memset(arr, 0, sizeof(arr));
		scanf("%d", &N);
		if (N == 0)
		{
			printf("Case #%d: INSOMNIA\n", ts++);
		}
		else
		{
			long long i = 1;
			while (1)
			{
				long long cand = (long long) N * i;
				long long ans = cand;
				while (cand != 0)
				{
					int s = cand - (cand / 10 * 10);
					arr[s] = 1;
					cand /= 10;
				}
				bool b = false;
				for (int j = 0; j < 10; ++j)
				{
					if (arr[j] == 0)
					{
						b = true;
						break;
					}
				}
				if (!b)
				{
					printf("Case #%d: %lld\n", ts++,ans);
					break;
				}
				++i;
			}
		}

	}


}