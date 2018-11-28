// In the name of Allah

#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for ( int i = 0; i < n; i ++ )

int main()
{
	int T;
	cin >> T;
	rep (t, T)
	{
		int n;
		string s;
		cin >> n >> s;
		int ans = 0, cnt = 0;
		rep (i, n+1)
			if ( s[i] > '0' )
			{
				if ( cnt < i )
				{
					ans += i-cnt;
					cnt = i;
				}
				cnt += s[i]-'0';
			}
		printf ("Case #%d: %d\n", t+1, ans);
	}
	
	return 0;
}
