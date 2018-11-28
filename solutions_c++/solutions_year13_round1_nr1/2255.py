#include <iostream>
#include <math.h>
using namespace std;
int main ( int argc, char * argv[] )
{
	int n;
	cin >> n;
	for ( int tc = 1 ; tc <= n ; tc++ )
	{
		long long r, t;
		cin >> r >> t;
		long long  area = 0;
		long long delta =  - r*r + (r+1)*(r+1);
		int i;
		for ( i = 0 ; 1 ; i++)
		{	area += delta;
			delta += 4;
			if ( area > t )
			{
				break;
			}
			r+=2;
		}
			
		cout << "Case #" << tc << ": " << i << endl;
	}
}
		

