#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

void main1( int t1 )
{
	int a, b, i, x, y, z, temp, count, j;
	cin >> a >> b;
	count = 0;
	
	for ( i = a; i <= b; i ++ ) {
		x = i;
		y = i;
		z = 0;
		
		while ( y ) {
			temp = y % 10;
			z = z * 10;
			z += temp;
			y = y / 10;
		}
		
		if ( x == z ) {
			j = sqrt( i );
			y = j * j;
			if ( i == y ) {
				x = j;
				y = j;
				z = 0;
				
				while ( y ) {
					temp = y % 10;
					z = z * 10;
					z += temp;
					y = y / 10;
				}
				
				if ( x == z ) {
					count ++;
				}
			}
		}
	}
	
	cout << "Case #" << t1 << ": " << count << "\n";
}

int main()
{
	int i, t;
	cin >> t;
	
	for ( i = 1; i <= t; i ++ ) {
		main1( i );
	}
	
	return 0;
}