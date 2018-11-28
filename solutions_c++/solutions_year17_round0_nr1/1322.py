#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

int k, ans, blad, t;
string s;
int main()
{
	ios_base::sync_with_stdio( 0 );
	cin.tie( 0 );
	cin>>t;
	for( int tt = 1; tt <= t; tt++ )
	{
		cin>>s>>k;
		ans = 0;
		blad = 0;
		for( int a = 0; a < s.size(); a++ )
		{
			if( s[a] == '-' )
			{
				ans++;
				if( s.size() - a < k )blad = 1;
				else
				{
					for( int b = a; b <= a+k-1; b++ )
					{
						if( s[b] == '+' )s[b] = '-';
						else s[b] = '+';
					}
				}
			}
		}
		if( !blad )cout<<"Case #"<<tt<<": "<<ans<<endl;
		else cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
	}	
	return 0;
}
 

