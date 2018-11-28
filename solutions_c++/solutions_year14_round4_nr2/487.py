using namespace std;

#include "iostream"
#include "algorithm"

int a[ 1003 ];
int b[ 1003 ];

int main()
{
	int T;

	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int N;
		cin >> N;
		for (int i = 0; i < N; i++) cin >> a[ i ];

		for (int i = 0; i < N; i++) b[i] = a[i];

		int ans = 0;
		sort( b, b + N );

		int le = 0, ri = N - 1;
		for (int i = 0; i < N; i++)
		{
			int x = le;
			while ( x <= ri && a[x] != b[i] ) x++;

			if ( x - le <= ri - x )
			{
				ans += x - le;
				for (int y = x; y > le; y--) swap( a[y], a[y - 1] );
				le++;
			}
			else
			{
				ans += ri - x;
				for (int y = x; y < ri; y++) swap( a[y], a[y + 1]  );
				ri--;
			}
		}

		cout << "Case #" << tc << ": " << ans << endl;
	}

	return 0;
}
