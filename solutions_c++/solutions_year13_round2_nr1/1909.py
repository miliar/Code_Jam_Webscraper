#include <iostream>
#include <fstream>
#include <algorithm>
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

	ofstream outfile;
	char * filename = new char[strlen(argv[1]) + 2];
	strcpy(filename, argv[1]);
	strcpy(filename + strlen(argv[1]) - 2, "out");
	outfile.open(filename);

	int armin, motecount, i, changes, changestore;
	int * motes;

	for (int n = 0; n < count; ++n)
	{
		changes = 0;
		changestore = 101;

		infile >> armin >> motecount;
		motes = new int[motecount];

		for (i = 0; i < motecount; ++i)
			infile >> motes[i];

		sort(motes, motes + motecount);

		if (armin == 1)
			changes = motecount;
		else
			for (i = 0; i < motecount; ++i)
			{
				if (armin > motes[i])
				{
					armin += motes[i];
					continue;
				}

				if (armin + armin - 1 > motes[i])
				{
					armin += armin - 1;
					armin += motes[i];
					++changes;
					continue;
				}

				if (changestore == 101)
					changestore = changes + motecount - i;

				while (armin <= motes[i])
				{
					armin += armin - 1;
					++changes;
				}
				armin += motes[i];
			}

		if (changes > changestore)
			changes = changestore;
		outfile << "Case #" << n + 1 << ": " << changes << endl;

		delete [] motes;
	}

	outfile.close();
	infile.close();

	delete [] filename;

	return EXIT_SUCCESS;
}
