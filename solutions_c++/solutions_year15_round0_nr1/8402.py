#include <bits/stdc++.h>

using namespace std;

main ()
{
	int t, caso = 1;
	cin >> t;
	while ( t-- )
	{
		int n;
		cin >> n;
		char c;
		string shy;
		for ( int i = 0 ; i < n+1 ; i++ )
		{
			cin >> c;
			shy += c;
		}

		long long ans = 0LL;
		long long accum = 0LL;
		for ( int i = 0 ; i < n+1 ; i++ )
		{
			if ( accum >= i )
			{
				accum += shy[i] - '0';
			}
			else
			{
				ans += i - accum;
				accum += i - accum;
				accum += shy[i] - '0';
			}
		}
		cout << "Case #" << caso++ << ": " << ans << "\n";
	}
}
