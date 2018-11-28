#include <bits/stdc++.h>
using namespace std;

int parse ( )
{
	int row, ans = 0, x, i, j;
	cin >> row;
	for ( i = 1; i <= 4; ++i )
		for ( j = 1; j <= 4; ++j ) {
			cin >> x;
			if ( i == row )
				ans |= (1<<x);
		}
	return ans;
}

int main ( )
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int nTests;
	cin >> nTests;
	for ( int test = 1; test <= nTests; ++test )
	{
		int a = parse();
		a &= parse();

		int cnt = 0, i = 0;
		for ( int j = 1; j <= 16; ++j )
			if ( ( (a>>j)&1 ) == 1 )
				cnt++, i=j;

		cout << "Case #" << test << ": ";
		if ( cnt == 0 ) cout << "Volunteer cheated!";
		else if ( cnt == 1 ) cout << i;
		else cout << "Bad magician!";
		cout << '\n';
	}
	
	return 0;
}
