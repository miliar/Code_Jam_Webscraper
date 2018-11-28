#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include<fstream>
#include <limits>


int main()
{
	std::ofstream outFile;
	outFile.open("a.out");

	std::ifstream inFile;
	inFile.open("a.in");

	int NN;
	inFile >> NN;
	//inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int N=1; N<=NN; ++N)
	{
		long long t, r;
		inFile >> r >> t;
		//inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

		// solution
		unsigned long nRes = 0;
		while (1)
		{
			t -= 2*r+1;
			r += 2;
			if (t < 0) break;
			++nRes;
		}

		// output result
		outFile << "Case #" << N << ": " << nRes;
		if (N!=NN) outFile << std::endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}