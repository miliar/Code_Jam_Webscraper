#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>


const int Max = 100;


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

	int n, w, h, i, j, k, min;
	bool x, y;
	int ** lawn;

	char * state = new char[count];
	for (n = 0; n < count; ++n)
		state[n] = 'Y';

	for (n = 0; n < count; ++n)
	{
		min = Max;
		infile >> h >> w;
		lawn = new int *[h];
		for (i = 0; i < h; ++i)
		{
			lawn[i] = new int[w];
			for (j = 0; j < w; ++j)
			{
				infile >> lawn[i][j];
				if (lawn[i][j] < min)
					min = lawn[i][j];
			}
		}

		for (i = 0; i < h && state[n] != 'N'; ++i)
			for (j = 0; j < w; ++j)
				if (lawn[i][j] == min)
				{
					x = y = true;

					for (k = 0; k < h; ++k)
						if (lawn[k][j] > min)
						{
							y = false;
							break;
						}

					for (k = 0; k < w; ++k)
						if (lawn[i][k] > min)
						{
							x = false;
							break;
						}

					if (!x && !y)
					{
						state[n] = 'N';
						break;
					}
				}

		for (i = 0; i < h; ++i)
			delete [] lawn[i];
		delete [] lawn;
	}

	for (n = 0; n < count; ++n)
	{
		outfile << "Case #" << n + 1 << ": ";
		switch (state[n])
		{
			case 'Y': outfile << "YES\n"; break;
			case 'N': outfile << "NO\n"; break;
		}
	}

	delete [] filename;
	delete [] state;
	outfile.close();
	infile.close();

	return EXIT_SUCCESS;
}
