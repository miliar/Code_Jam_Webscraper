#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

bool isPalindrom(int a) {
	char s[100];
	int n = sprintf(s, "%d", a), i;
	for( i = 0; i < n / 2; i++ )
		if( s[i] != s[n - i - 1] )
			break;
	return ( i >= n / 2 );
}

int main() {
	ifstream in;
	ofstream out;
	in.open( "C-small-attempt0.in" );
	out.open( "C-small-attempt0.out" );

	int t;
	in >> t;

	for( int k = 0; k < t; k++ ) {
		int a, b, count = 0;
		in >> a;
		in >> b;

		int x, y;
		x = (int)sqrt(a);
		if( sqrt(a) - x > 0 )
			x++;
		y = (int)sqrt(b);
		
		for( int i = x; i <= y; i++ )
			if( isPalindrom( i ))
				if( isPalindrom( i * i ))
					count++;
					
		out << "Case #" << k + 1 << ": " << count << endl;
	}

	in.close();
	out.close();
	return 0;
}