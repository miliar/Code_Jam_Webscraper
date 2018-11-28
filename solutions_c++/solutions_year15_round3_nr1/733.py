#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		int r, c, w;
		cin >> r >> c >> w;
		int i = w, ans = 0;
		while( i <= c )
			ans += r, i += w;
		i -= w;
		int L = i - max( 1, i-w+1 );
		int R = min( c, i+w-1 ) - i;
		ans += ( w - ( R ? 0 : 1 ) );
		cout << "Case #" << ++ cc << ": " << ans << endl;
	}
}
