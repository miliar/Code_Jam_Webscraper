#include <iostream>
#include <iomanip>

int main(void)
{
	int nbTests;
	std::cin >> nbTests;
	for(int t = 1; t <= nbTests; ++t)
	{
		double secs = 0;
		double c, f, x, prod = 2;
		std::cin >> c >> f >> x;

		bool buy = true;
		while(buy)
		{
			double nextX = x / prod;

			double nextFarm = c / prod;
			double farmProd = prod + f;
			double nextXFarm = nextFarm + (x / farmProd);

			if(nextXFarm < nextX)
			{
				buy = true;
				prod = farmProd;
				secs += nextFarm;
			}
			else
			{
				buy = false;
				secs += nextX;
			}
		}


		std::cout << std::fixed << std::setprecision(7)
			<< "Case #" << t << ": " << secs << "\n";
	}

	return 0;
}
