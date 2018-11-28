#include <cstdio>
#include <algorithm>

using namespace std;

int a[10010];

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int T, N, M, cases = 1;

	scanf("%d", &T);
	while( T-- )
	{
		scanf("%d %d", &N, &M);
		for( int i = 0; i < N; ++i )
			scanf("%d", &a[i]);
		sort(a, a+N);
		int ans = 0;
		int i = 0, j = N-1; 
		while( i <= j )
		{
			if( i == j )
			{
				ans++;
				break;
			}
			else
			{
				ans++;
				if( a[i] + a[j] <= M )
				{
					i++, j--;
					continue;;
				}
				else
				{
					j--;
					continue;
				}
			}
		}
		printf("Case #%d: %d\n", cases++, ans);
	}

	return 0;
}