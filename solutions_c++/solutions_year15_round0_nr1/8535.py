#include<bits/stdc++.h>
using namespace std;

int main ()
{
	int n;
	cin >> n;
	for ( int i = 1; i <= n; i++ )
	{
		int s;
		cin >> s;
		string pe;
		cin >> pe;
		long long l = 0, ans = 0;
		for ( int j = 0; j < pe.size(); j++ )
		{
			if ( l < j )
			{	
				ans += j-l;
				l += j-l;
			}
			l += pe[j]-48;
		}
		cout << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}
