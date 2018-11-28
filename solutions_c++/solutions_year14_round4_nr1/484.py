using namespace std;

#include "iostream"
#include "algorithm"

int a[ 10004 ];

int main()
{
	int T;

	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int N, X;
		cin >> N >> X;
		for (int i = 0; i < N; i++) cin >> a[i];

		int ans = N;
		sort( a, a + N );

		int le = 0;
		int ri = N - 1;

		while ( le < ri )
		{
			if ( a[le] + a[ri] <= X )
			{
				ans--;
				le++;
				ri--;
			}
			else
			{
				ri--;
			}
		}

		cout << "Case #" << tc << ": " << ans << endl;
	}

	return 0;
}
