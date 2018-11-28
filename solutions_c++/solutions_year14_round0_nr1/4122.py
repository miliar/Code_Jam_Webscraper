#include <fstream>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>


int main(int argc, char* argv[])
{
    int T, Ans, card, n1, n2, n3, n4;
	std::vector<bool> numbers(16);
    
    freopen ("A-small-attempt0.in", "r", stdin);
    freopen ("A.out", "w", stdout);
    std::cin >> T;
    for( int i = 0; i < T; ++i )
	{
		card = 0;
		std::cin >> Ans;
		for( int j = 0; j < 4; j++ )
		{
			std::cin >> n1;
			std::cin >> n2;
			std::cin >> n3;
			std::cin >> n4;
			numbers[n1 - 1] = ( Ans - 1 == j);
			numbers[n2 - 1] = ( Ans - 1 == j);
			numbers[n3 - 1] = ( Ans - 1 == j);
			numbers[n4 - 1] = ( Ans - 1 == j);
		}

		std::cin >> Ans;
		for( int j = 0; j < 4; j++ )
		{
			std::cin >> n1;
			std::cin >> n2;
			std::cin >> n3;
			std::cin >> n4;
			numbers[n1 - 1] = numbers[n1 - 1] && ( Ans - 1 == j);
			numbers[n2 - 1] = numbers[n2 - 1] && ( Ans - 1 == j);
			numbers[n3 - 1] = numbers[n3 - 1] && ( Ans - 1 == j);
			numbers[n4 - 1] = numbers[n4 - 1] && ( Ans - 1 == j);
		}
		
		for( int j = 0; j < 16; j++ )
		{
			if( numbers[j] )
			{
				if( card )
					card = 17;
				else
					card = j + 1;
			}
		}

//		std::cerr << i+1 << std::endl;
		if( card )
		{
			if( card == 17 )
				std::cout << "Case #" << i+1 << ": " << "Bad magician!" << std::endl;
			else
				std::cout << "Case #" << i+1 << ": " << card << std::endl;
		}
		else
		{
			std::cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << std::endl;
		}
		
	}
	
    return 0;
}