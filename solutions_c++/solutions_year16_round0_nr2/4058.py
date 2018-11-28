#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int ans = 0;
		char pancake[100 + 1] = {};
		cin >> pancake;
		int S = strlen(pancake);

		for (int i = 0; i < S; i++)
		{
			if (pancake[i] == '-')
			{
				char side = pancake[i + 1];

				if (side == '\0' || side == '+')
				{
					ans++;
				}
			}
			else
			{
				char side = pancake[i + 1];

				if (side == '-')
				{
					ans++;
				}
			}
		}

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
