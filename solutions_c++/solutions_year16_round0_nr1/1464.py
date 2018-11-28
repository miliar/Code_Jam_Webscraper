#include <bits/stdc++.h>
using namespace std;

#define two(x) (1<<(x))

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		long long n, m = 0, i = 0, mask = 0;
		cin >> n;
		for( i = 1 ; n && (i+1) * n < 1000000000LL * 1000000000LL ; i ++ )
		{
			m = i * n;
			while( m > 0 )
				mask |= two( m%10 ), m /= 10;
			if( mask == two(10)-1 )
				break;
		}
		if( mask == two(10)-1 )
			cout << "Case #" << ++cc << ": " << i * n << endl;
		else
			cout << "Case #" << ++cc << ": " << "INSOMNIA" << endl;
	}
	return 0;
}
