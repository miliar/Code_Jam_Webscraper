#include <iostream>
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
		int row1, row2;
		int grid1[4][4], grid2[4][4];
		int answer;
		int hits = 0;

		infile >> row1;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				infile >> grid1[i][j];
		infile >> row2;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				infile >> grid2[i][j];

		--row1;
		--row2;

		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (grid1[row1][i] == grid2[row2][j])
				{
					answer = grid1[row1][i];
					++hits;
				}

		outfile << "Case #" << n + 1 << ": ";
		if (hits == 0)
			outfile << "Volunteer cheated!" << endl;
		else if (hits == 1)
			outfile << answer << endl;
		else
			outfile << "Bad magician!" << endl;
	}

	outfile.close();
	infile.close();

	delete [] filename;

	return EXIT_SUCCESS;
}
