#include <bits/stdc++.h>

using namespace std;

constexpr int LIMIT = 1000000;

int main()
{
	int T, N;
	string current;
	bool d[10];

	scanf("%d", &T);

	for(int i=1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		scanf("%d", &N);

		if (N == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}

		for(int j=0; j < 10; j++)
			d[j] = false;

		for(int j=1;;j++)
		{
			bool ok = true;

			if (j*N > LIMIT)
			{
				printf("INSOMNIA\n");
				break;
			}

			current = to_string(j*N);
			for(auto &c : current)
			{
				d[c - '0'] = true;
			}

			for(int k=0; k < 10; k++)
			{
				if (!d[k])
				{
					ok = false;
					break;
				}
			}

			if (ok)
			{
				printf("%d\n", j*N);
				break;
			}
		}
	}

	return EXIT_SUCCESS;
}