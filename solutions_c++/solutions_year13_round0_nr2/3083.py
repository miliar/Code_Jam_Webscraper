#include <iostream>
using namespace std;
int main ( int argc, char * argv[] )
{
	int n;
	cin >> n;
	for ( int tc = 1 ; tc <= n ; tc++ )
	{
		int r, c, rn, cn;
		int b[100][100] = {{0}};
		int rmax[100] = {0};
		int cmax[100] = {0};
		cin >> rn >> cn;
		for ( int r = 0 ; r < rn ; r ++ )
		{
			for ( int c = 0 ; c < cn ; c++ )
			{
				cin >> b[r][c];
				if ( b[r][c] > cmax[c] )
					cmax[c] = b[r][c];
				if ( b[r][c] > rmax[r] )
					rmax[r] = b[r][c];
			}
		}
		int possible = 1;
		for ( int r = 0 ; r < rn && possible ; r ++ )
		{
			for ( int c = 0 ; c < cn && possible ; c++ )
			{
				if ( b[r][c] < cmax[c] && b[r][c] < rmax[r] )
					possible = 0;
			}
		}
		cout << "Case #" << tc << ": ";
		if ( possible )
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
}
		

