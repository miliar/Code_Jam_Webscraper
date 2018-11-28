#include <bits/stdc++.h>

#define For(i, a, b) for(int i=(a); i<(b); ++i)
#define INF 1000000000
#define MP make_pair

using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

char pancake[105], aux[105];

int main()
{
	//std::ios_base::sync_with_stdio(false);

	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--)
	{
		scanf("%s", pancake);

		int ans = 0;
		int n = strlen(pancake);

		for (int i = n-1; i >= 0; --i)
		{
			if (pancake[i] == '+')
				continue;
			else
			{
				
				if (pancake[0] == '+')
				{
					int k = 0;
					while (pancake[k] == '+')
					{
						pancake[k] = '-';
						++k;
					}

					++ans;
				}

				++ans;

				For(j, 0, i+1)
					aux[j] = pancake[j];

				For(j, 0, i+1)
					pancake[j] = aux[i-j] == '+' ? '-' : '+';
			}
		}

		printf("Case #%d: %d\n", caso++, ans);
	}

	return 0;
}