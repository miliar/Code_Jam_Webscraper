#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N;
		cin >> N;

		if (N == 0)
		{
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}

		int ans = -1;
		bool digit[10] = {};
		for (int i = 0; i < 100; i++)
		{
			for (int n = (i + 1) * N; n > 0; n /= 10)
			{
				int k = n % 10;
				digit[k] = true;
			}

			bool found = true;
			for (int k = 0; k < 10; k++)
				found &= digit[k];

			if (found)
			{
				ans = (i + 1) * N;
				break;
			}
		}

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
