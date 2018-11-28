#include <iostream>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("Text.txt","w",stdout);
	int tc;
	cin >> tc;
	int n,m;
	for ( int i = 1 ; i <= tc ; i++ )
	{
		cin >> n >> m;
		int ar[105][105];
		for ( int p = 0 ; p < n ; p++ )
		{
			for ( int o = 0 ; o < m ; o++ )
			{
				cin >> ar[p][o];
			}
		}
		bool res=true;
		for ( int p = 0 ; p < n ; p++ )
		{
			for ( int o = 0 ; o < m ; o++ )
			{
				bool flagv = true;
				bool flagh = true;
				res = true;
				for ( int y = 0 ; y < n ; y++ )
				{
					if ( ar[p][o] < ar[y][o] )
					{
						flagv = false;
						break;
					}
				}
			    if ( !flagv )
				for ( int y = 0 ; y < m ; y++ )
				{
					if ( ar[p][o] < ar[p][y] )
					{
						flagh = false;
						break;
					}
				}
				if ( !flagv && !flagh ) // if vertical & horizontal both closed.
				{
					res = false;
					break;
				}
			}
			if ( !res ) break;
		}
		cout<<"Case #"<<i<<": ";
		if ( res ) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}

	return 0;
}