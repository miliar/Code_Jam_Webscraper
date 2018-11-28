#include <fstream>
#include <iostream>
//#include <math.h>
//#include <algorithm>
//#include <stdlib.h>
//#include <vector>


int main(int argc, char* argv[])
{
    int T;
	unsigned long long A, B, K, y;
    
    freopen ("B-small-attempt0.in", "r", stdin);
    freopen ("B-small-attempt0.out", "w", stdout);
    std::cin >> T;
    for( int i = 0; i < T; ++i )
	{
//		std::cerr << i+1 << std::endl;
		std::cin >> A;
		std::cin >> B;
		std::cin >> K;
		y = 0;
		for( unsigned long long j = 0; j < A; ++j)
			for( unsigned long long k = 0; k < B; ++k)
				if( (j bitand k) < K )
					++y;

		std::cout << "Case #" << i+1 << ": " << y << std::endl;
	}
	
    return 0;
}