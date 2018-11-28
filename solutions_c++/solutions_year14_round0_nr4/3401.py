#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define For(i, a, b) for(int i=a; i<b; ++i)
#define MP make_pair
#define INF (1<<30)

using namespace std;

typedef pair <int, int> ii;

double Naomi[1005], Ken[1005];

int main()
{
	int T;
	scanf("%d", &T);

	For(caso, 1, T+1)
	{
		int N;
		scanf("%d", &N);
	
		For(i, 0, N)
			scanf("%lf", &Naomi[i]);
		For(i ,0, N)
			scanf("%lf", &Ken[i]);

		sort(Naomi, Naomi+N);
		sort(Ken, Ken+N);

		int d = 0, h = 0;

		int n = 0, k = 0;
		while (n < N and k < N)
		{
			if (Naomi[n] > Ken[k])
			{
				d++;
				n++;
				k++;
			}
			else
				n++;
		}

		n = N-1, k = N-1;
		while (n >= 0 and k >= 0)
		{
			if (Naomi[n] < Ken[k])
			{
				h++;
				n--;
				k--;
			}
			else
				n--;
		}

		printf("Case #%d: %d %d\n", caso, d, N-h);
	}
	return 0;
}