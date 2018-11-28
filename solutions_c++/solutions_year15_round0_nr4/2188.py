#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;

int main()
{
	ll casses;
	cin >> casses;
	ll x, r, c;
	for( int i = 0; i < casses && cin >> x >> r >> c; i++ )
	{
		if( x == 1 )
			cout << "Case #" << i + 1 << ": GABRIEL" << endl;
		if( x == 2 )
		{
			if( r * c % 2 == 0 )
			{
				cout << "Case #" << i + 1 << ": GABRIEL" << endl;
			}else
			{
				cout << "Case #" << i + 1 << ": RICHARD" << endl;
			}
		}
		if( x == 3 )
		{
			if( r * c == 3 )
			{
				cout << "Case #" << i + 1 << ": RICHARD" << endl;
			}else if( r * c % 3 == 0 )
			{
				cout << "Case #" << i + 1 << ": GABRIEL" << endl;
			}else
			{
				cout << "Case #" << i + 1 << ": RICHARD" << endl;
			}
		}
		if( x == 4 )
		{
			if( r <= 2 || c <= 2 )
			{
				cout << "Case #" << i + 1 << ": RICHARD" << endl;
			}else if( r * c % 4 == 0 )
			{
				cout << "Case #" << i + 1 << ": GABRIEL" << endl;
			}else
			{
				cout << "Case #" << i + 1 << ": RICHARD" << endl;
			}
		}
	}
	return 0;
}
