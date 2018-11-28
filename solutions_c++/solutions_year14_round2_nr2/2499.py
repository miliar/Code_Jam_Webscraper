#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{

	ifstream infile(argv[1]);
	int numCases;

	infile >> numCases;

	for (int i = 1; i <= numCases; i++)
	{
		unsigned int A, B, K, count = 0;
		infile >> A >> B >> K;
		for (int c = 0; c < A; c++)
		{
			for (int d = 0; d < B; d++)
			{
				if ((c & d) < K)
					count++;
			}
		}
		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;

}
