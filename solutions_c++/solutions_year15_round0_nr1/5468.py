#include <iostream>
#include <sstream>

int main(int argc, char* argv[])
{
	int numCases;
	std::cin >> numCases;
	for (int i=0; i<numCases; i++)
	{
		int Smax;
		std::cin >> Smax;

		int alreadyUp = 0;
		int peopleNeeded = 0;
		for (int j=0; j<=Smax; j++)
		{
			char cSj;
			std::cin >> cSj;
			int Sj = cSj - '0';

			if (alreadyUp < j)
			{
				peopleNeeded += (j-alreadyUp);
				alreadyUp += (j-alreadyUp);
			}
			alreadyUp += Sj;
		}
		
		std::cout << "Case #" << (i+1) << ": " << peopleNeeded << std::endl;

	}
	return 0;
}
