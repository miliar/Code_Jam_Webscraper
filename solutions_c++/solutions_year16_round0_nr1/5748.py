// Sheep.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream infile(argv[1]);
	ofstream outfile;

	outfile.open(argv[2]);
	
	
	int numCases;

	infile >> numCases;

	int casesCompleted = 0;
	
	int inputNumber;

	bool found[10];
	int test, numFound, digit, iteration;
	
	while (casesCompleted < numCases) {
		infile >> inputNumber;
		if (inputNumber == 0) {
			outfile << "Case #" << casesCompleted + 1 << ": " << "INSOMNIA" << "\n";
			++casesCompleted;
			continue;
		}
		for (int j = 0; j < 10; ++j) {
			found[j] = false;
		}
		numFound = 0;
		iteration = 1;
		bool flag = false;
		while (true) {
			test = iteration*inputNumber;
			while (test > 0) {
				digit = test % 10;
				if (found[digit] == false) {
					found[digit] = true;
					++numFound;
					if (numFound == 10) {
						outfile << "Case #" << casesCompleted + 1 << ": " << iteration*inputNumber << "\n";
						flag = true;
						break;
					}

				}
				test /= 10;

			}
			if (flag == true) {
				break;
			}

			++iteration;
		}


		++casesCompleted;
	}
	
	infile.close();
	outfile.close();

	
    return 0;
}

