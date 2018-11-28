#include <fstream>
#include <iostream>
//#include <math.h>
#include <algorithm>
//#include <stdlib.h>
#include <vector>
//#include <iomanip>
//#include <string>


int main(int argc, char* argv[])
{
    int T;
	int N, y, z, NaomiR, KenR, KenL;
 	long double temp;
	std::vector<long double> Naomi, Ken;
    
    freopen ("D-large.in", "r", stdin);
    freopen ("D.out", "w", stdout);
    std::cin >> T;
//	std::cout << std::setprecision(16);
    for( int i = 0; i < T; ++i )
	{
//		std::cerr << i+1 << std::endl;
		y = 0;
		z = 0;
		std::cin >> N;
		Naomi.resize(N);
		Ken.resize(N);
		NaomiR = N;
		KenR = N;
		
		for( int j = 0; j < N; j++)
			std::cin >> Naomi[j];
		for( int j = 0; j < N; j++)
			std::cin >> Ken[j];

		std::sort(Naomi.begin(), Naomi.end());
		std::sort(Ken.begin(), Ken.end());

/*		for( int j = 0; j < N; j++)
			std::cerr << Naomi[j] << " ";
		std::cerr << std::endl;
		for( int j = 0; j < N; j++)
			std::cerr << Ken[j] << "  ";
		std::cerr << std::endl;*/
		
		
		while( NaomiR )
		{
			if( Ken[KenR - 1] > Naomi[NaomiR - 1] )
			{
				z++;
				KenR--;
				NaomiR--;
			}
			else
			{
				NaomiR--;
			}
		}
		z = N - z;

		
		KenR = N - 1;
		KenL = 0;
		for( int j = 0; j < N; j++ )
		{
			if( Ken[KenL] > Naomi[j] )
			{
				KenR--;
			}
			else
			{
				if( Ken[KenR] < Naomi[N - 1] )
				{
					KenL++;
					y++;
				}
				else
				{
					KenR--;
				}
			}
		}

//		std::cerr << std::endl;
		std::cout << "Case #" << i+1 << ": " << y << " " << z << std::endl;
	}
	
    return 0;
}