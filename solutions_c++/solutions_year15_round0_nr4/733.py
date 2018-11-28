#include <bits/stdc++.h>
using namespace std;

string ansStr[] = { "RICHARD", "GABRIEL", "DUNNO" };

int main ( )
{
	int ntc;
	cin >> ntc;
	for ( int test = 1; test <= ntc; ++test ) {
		int X, R, C, ans = 1;
		cin >> X >> R >> C;
		if ( R > C ) swap ( R, C);

		if ( (R*C)%X != 0 )
			ans = 0;
		else if ( R == C )
		{
			if ( X > R )
				ans = 0;
		}
		else // R < C
		{
			if ( R == 1 ) {
				if ( X >= 3 )
					ans = 0;
			}
			else if ( R == 2 ) {
				if ( X >= 4 )
					ans = 0;
			}
			else if ( R == 3 ) {
				if ( X >= 7 )
					ans = 0;
				else if ( X == 6 ) {
					ans = 0;
					for ( int a = 0; a+3 <= C; ++a )
						if ( (3*a+1)%X == 0 && (3*(C-a-3)+2) == 0 )
							ans = 1;
				}
			}
			else {
				if ( X >= 7 )
					ans = 0;
			}
		}

		cout << "Case #" << test << ": " << ansStr[ans] << endl;
	}
	return 0;
}
