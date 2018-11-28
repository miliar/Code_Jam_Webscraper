#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std ;
int main ()
{
	ifstream inp("inb.txt") ;
	ofstream out("outb.txt") ;
	double ratio ;
	int t , ti , r , c , w , ans ;
	inp >> t ;
	for ( ti = 1 ; ti <= t ; ti ++ )
	{
		inp >> r >> c >> w ;
		ratio = double(c)/w ;
		if ( ratio == 1 )
			ans = r-1+c ;
		else if ( ratio < 2 )
			ans = r+w ;
		else if ( ratio >= 2 )
		{
			ans = floor(ratio)*(r-1) + w + floor(ratio) ;
			if ( ratio - floor(ratio) == 0 )
				ans -- ;
		}
		out << "Case #" << ti << ": " << ans << '\n' ;
	}
}