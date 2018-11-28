#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t, x, r, c, ans;
	cin >> t;
	for ( int tt = 1; tt <= t ; tt++)
	{
		ans = 0;
		cin >> x >> r >> c;
		if ( x == 1 )
		{
			ans = 0;
		}
		else
		{
			switch(x)
			{
				case 2:
					ans = ( r*c ) % 2;
					break;
				case 3:
					if ( r == 1 || c == 1 )
						ans = 1;
					else
						ans = ( r*c ) % 3;
						break;
				case 4:
					if ( r >=3 && c >=3 && (r*c) % 4 == 0 )
						ans = 0;
					else
						ans = 1;
					break;
			}
		}
		
		cout << "Case #" << tt << ": ";
		if ( !ans )
		{
			cout << "GABRIEL" << endl;
		}
		else
		{
			cout << "RICHARD" << endl;
		}
	}
	return 0;
}