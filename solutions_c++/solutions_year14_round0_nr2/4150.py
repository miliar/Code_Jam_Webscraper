#include <fstream>
#include <iostream>
//#include <math.h>
//#include <algorithm>
//#include <stdlib.h>
#include <vector>
#include <iomanip>


int main(int argc, char* argv[])
{
    int T;
	long double C, F, X, time, tau, rate;
    
    freopen ("B-large.in", "r", stdin);
    freopen ("B.out", "w", stdout);
    std::cin >> T;
	std::cout << std::setprecision(16);
    for( int i = 0; i < T; ++i )
	{
		std::cin >> C;
		std::cin >> F;
		std::cin >> X;
		
//		std::cerr << i+1 << std::endl;

		rate = 2;
		time = X / 2;
		tau = 0;
		while( X * F > C * (rate + F))
		{
			tau += C / rate;
			rate += F;
			time = X / rate + tau;
//			std::cerr << " " << rate << " " << time;
		}
		
//		std::cerr << std::endl;
		std::cout << "Case #" << i+1 << ": " << time << std::endl;
	}
	
    return 0;
}