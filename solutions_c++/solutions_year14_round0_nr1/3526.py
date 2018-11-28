#include <iostream>
#include <vector>

using std::vector;

int main()
{
	int T = 0;
	std::cin >> T;
	for ( int test = 1 ; test <= T ; ++test )
	{
		int value = 0;
		int temp = 0;
		vector<int> a(5);
		vector<int> b(5);
		std::cin >> value;
		for ( int p = 1 ; p <= 4 ; ++p )
		{
			for ( int q = 1 ; q <= 4 ; ++q )
			if ( p == value )
			{
				std::cin >> a[q];
			}
			else {
					std::cin >> temp;
				 }
		}

		std::cin >> value;
		for ( int p = 1 ; p <= 4 ; ++p )
		{
			for ( int q = 1 ; q <= 4 ; ++q )
			if ( p == value )
			{
				std::cin >> b[q];
			}
			else {
					std::cin >> temp;
				 }
		}

		value = 0 ;

		for ( int p = 1 ; p <= 4 ; ++p )
		{
			for ( int q = 1 ; q <= 4 ; ++q)
			{
				if ( a[p] == b[q] ) 
				{
					if ( value == 0 )
					{
						value = a[p];
					}
					else {
							value = -1;
						 }
				}
			}
		}
		std::cout << "Case #" << test << ": ";
		if ( value > 0 )
		{
			std::cout << value;
		}
		else if ( value != 0 )
			 {
				 std::cout << "Bad magician!" ;
			 }
			 else {
					  std::cout << "Volunteer cheated!" ;
				  }
		std::cout << std::endl;
	}
}
