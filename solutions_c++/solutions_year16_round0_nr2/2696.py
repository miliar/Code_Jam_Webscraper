#include <stdlib.h>
#include <string>
#include <iostream>

int main()
{
	int T;
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	std::cin >> T;
	for( int t = 1; t <= T; t++ )
	{
		std::string S;
		std::cin >> S;
		S = S + '+';
		int flips = 0;
		for( int i = 0; i < S.size() - 1; i++ )
			if( S[ i ] != S[ i + 1 ] )
				flips++;
		std::cout << "Case #" << t << ": " << flips << std::endl;
	}
}