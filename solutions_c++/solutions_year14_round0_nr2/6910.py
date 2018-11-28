#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <cstring>


int main(int argc, char * argv[])
{
	using namespace std;

	if (argc < 2)
	{
		cerr << "Usage: " << argv[0] << " inputFile\n";
		exit(EXIT_FAILURE);
	}

	ifstream infile;
	infile.open(argv[1]);
	if (!infile.is_open())
	{
		cerr << "Could not open the file " << argv[1]
			<< "\nProgram terminating.\n";
		exit(EXIT_FAILURE);
	}

	int count;
	infile >> count;
	infile.get();

	ofstream outfile;
	char * filename = new char[strlen(argv[1]) + 2];
	strcpy(filename, argv[1]);
	strcpy(filename + strlen(argv[1]) - 2, "out");
	outfile.open(filename);

	for (int n = 0; n < count; ++n)
	{
		double cost, farm, target;
		infile >> cost >> farm >> target;
		double rate = 2.0;

		double choice1, choice2;
		double time = 0.0;
		while(true)
		{
			choice1 = target / rate;
			choice2 = cost / rate + target / (rate + farm);

			if (choice2 < choice1)
			{
				time += cost / rate;
				rate += farm;
			}
			else
			{
				time += choice1;
				break;
			}
		}

		outfile << "Case #" << n + 1 << ": " << fixed << setprecision(7) << time << endl;
	}

	outfile.close();
	infile.close();

	delete [] filename;

	return EXIT_SUCCESS;
}
