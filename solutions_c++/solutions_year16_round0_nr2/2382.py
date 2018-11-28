#include<iostream>
#include<cstdio>

using namespace std;

int t, ans;
char znak;
string ciag;

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "dane.txt", "w", stdout );
	ios_base::sync_with_stdio( 0 );
	cin>>t;
	for( int a = 1; a <= t; a++ )
	{
		ans = 0;
		cin>>ciag;
		znak = ciag[0];
		for( int b = 1; b < ciag.size(); b++ )
		{
			if( ciag[b] != znak )
			{
				++ans;
				if( znak == '-' )znak = '+';
				else znak = '-';
			}
		}
		if( znak == '-' )++ans;
		cout<<"Case #"<<a<<": "<<ans<<endl;
	}
	
	return 0;
}
