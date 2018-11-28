#include <iostream>
#include <iomanip>

int main()
{
	int T = 0;
	std::cin >> T;

	for ( int test = 1 ; test <= T ; ++test )
	{
		double c,f,x;
		std::cin >> c >> f >> x;

		double t = 0;
		double s = 2;
		while ( x/s > c/s+x/(s+f) )
		{
			t += c/s;
			s += f;
		}

		t += x/s;
		std::cout << "Case #" << test << ": " << std::setprecision(10) <<t << std::endl;
	}
}
