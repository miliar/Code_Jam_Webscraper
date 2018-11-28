#include <bits/stdc++.h>
using namespace std;

#define two(x) (1<<(x))

string a[16], b[16];

int main()
{
	int t, tc = 0, n;
	cin >> t;
	while( t -- )
	{
		cin >> n;
		for( int i = 0 ; i < n ; i ++ )
			cin >> a[i] >> b[i];
		int ans = 0;
		for( int i = 0 ; i < two(n) ; i ++ )
		{
			int cnt = 0, bad = 0;
			for( int j = 0 ; j < n ; j ++ )
				if( i & two(j) )
				{
					int ga = 0, gb = 0;
					cnt ++;
					for( int k = 0 ; k < n ; k ++ )
					{
						if( !( i & two(k) ) && a[k] == a[j] )
							ga = 1;
						if( !( i & two(k) ) && b[k] == b[j] )
							gb = 1;
					}
					if( !ga || !gb )
					{
						bad = 1;
						break;
					}
				}
			if( !bad )
				ans = max( ans, cnt );
		}
		cout << "Case #" << ++tc << ": " << ans << endl;
	}
	return 0;
}
