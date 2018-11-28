#include <bits/stdc++.h>

#define For(i, a, b) for(int i=(a); i<(b); ++i)
#define INF 1000000000
#define MP make_pair

using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

bool digit[10];

int main()
{
	//std::ios_base::sync_with_stdio(false);

	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--)
	{
		int n;
		scanf("%d", &n);

		printf("Case #%d: ", caso++);
		if (n == 0)
			printf("INSOMNIA\n");
		else
		{
			memset(digit, 0, sizeof digit);
			int d = 0, N = n;

			while (d < 10)
			{
				int aux = N;
				while (aux and d < 10)
				{
					int k = aux % 10;
					if (!digit[k])
						digit[k] = 1, ++d;
					aux /= 10;
				}
				N += n;
			}

			printf("%d\n", N-n);
		}
	}

	return 0;
}