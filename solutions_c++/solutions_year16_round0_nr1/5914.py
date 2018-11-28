#include <iostream>
#include <fstream>



void updateArray(int N, bool flagTable[]) {

	while (true) 
	{
		if (N == 0)
			return;
		int singleDigit = N % 10;
//		std::cout << "N: " << N << std::endl;
//		std::cout << "sd: " << singleDigit << std::endl;
		flagTable[singleDigit] = true;
		N = N / 10;

	}
}

bool checkFlagTable(bool flagTable[]) {
	for (int i = 0; i < 10; i++)
		if (flagTable[i] == false)
			return false;
	return true;
}

int computeN(int N) 
{
	int originalN = N;
	bool flagTable[10] = {0};

	int nbIteration = 1;
	while (true) {
		updateArray(N, flagTable);
		if (checkFlagTable(flagTable))
			break;
		nbIteration++;
		N = nbIteration * originalN;
//		std::cout << "newN: " << N << std::endl;
		if (N == originalN)
			return -1;
	}
	return N;
}

int main(int argc, char *args[])
{
	std::ifstream input(args[1]);

	int nbCase;

	input >> nbCase;

	for (int curCase = 1; curCase <= nbCase; curCase++)
	{
		int N;
		input >> N;

		int result = computeN(N);

		std::cout << "Case #" << curCase << ": ";
		if (result != -1)
			std::cout << result << std::endl;
		else
			std::cout << "INSOMNIA" << std::endl;
	}
	return 0;
}