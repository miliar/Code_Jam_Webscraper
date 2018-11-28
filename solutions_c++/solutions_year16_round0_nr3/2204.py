#include <stdlib.h>
#include <vector>
#include <string>
#include <iostream>

int main()
{
	int T, N, J;
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.out", "w", stdout );
	std::cin >> T;
	for( int t = 1; t <= T; t++ )
	{
		std::cin >> N >> J;
		std::cout << "Case #" << t << ":" << std::endl;
		std::vector<std::vector<int>> indices;
		int halfSize = N / 2;
		bool enough = false;
		for( int i1 = 1; i1 < halfSize && !enough; i1++ )
			for( int i2 = i1 + 1; i2 < halfSize && !enough; i2++ )
				for( int i3 = i2 + 1; i3 < halfSize && !enough; i3++ )
					for( int i4 = i3 + 1; i4 < halfSize && !enough; i4++ )
					{
						std::vector<int> tmp = { i1, i2, i3, i4 };
						indices.push_back( tmp );
						int size = indices.size();
						enough = size*size > J;
					}
		for( int i = 0; i < indices.size() && J > 0; i++ )
			for( int j = 0; j < indices.size() && J > 0; j++ )
			{
				std::string jamCoin( N, '0' );
				jamCoin[ 0 ] = '1';
				jamCoin[ N - 1 ] = '1';
				for( int k = 0; k < indices[ i ].size(); k++ )
				{
					jamCoin[ 2 * indices[ i ][ k ] ] = '1';
					jamCoin[ 2 * indices[ j ][ k ] - 1 ] = '1';
				}
				std::cout << jamCoin << " 3" << " 2" << " 5" << " 2" << " 5" << " 2" << " 3" << " 2" << " 11" << std::endl;
				J--;
			}
	}
}