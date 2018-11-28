#include <cstdio>
#include <algorithm>

using namespace std;

int a[10000], f1[10000], f2[10000];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T, N, cases = 1;

	scanf("%d", &T);
	while( T-- )
	{
		int ans = 0;
		scanf("%d", &N);
		for( int i = 0; i < N; ++i )
			scanf("%d", &a[i]);

		int s = 0, e = N-1;
		for( int i = 0; i < N; ++i )
		{
			int pos = s;
			for( int j = s; j <= e; ++j )	if( a[j] < a[pos] )
				pos = j;
			
			if( abs(pos-s) < abs(pos-e) )
			{
				while( pos != s )
				{
					swap(a[pos], a[pos-1]);
					pos--;
					ans++;
				}
				s++;
			}
			else
			{
				while( pos != e )
				{
					swap(a[pos], a[pos+1]);
					pos++;
					ans++;
				}
				e--;
			}
		}

		/*
		if( N == 1 )
		{
			printf("Case #%d: %d\n", cases++, 0);
			continue;
		}

		f1[0] = 0;
		for( int i = 1; i < N; ++i )
		{
			f1[i] = f1[i-1];
			for( int j = 0; j < i; ++j )	if( a[j] > a[i] )
				f1[i]++;
		}

		f2[N] = 0;
		for( int i = N-1; i >= 0; --i )
		{
			f2[i] = f2[i+1];
			for( int j = i+1; j < N; ++j )	if( a[j] > a[i] )
				f2[i]++;
		}

		for( int i = 0; i+1 < N; ++i )
		{
			int cnt = f1[i] + f2[i+1];
			ans = min(ans, cnt);
		}
		*/
		printf("Case #%d: %d\n", cases++, ans);
	}

	return 0;
}