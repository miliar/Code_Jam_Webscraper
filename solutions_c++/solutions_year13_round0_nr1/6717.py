#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <utility>
#include <list>

using namespace std;

typedef string (*solve_Tpf)(ifstream &);

void usage()
{
	cerr << "./storecredit [inputfile]" << endl;
	exit(-1);
}

string tictactoe(ifstream & i)
{
	bool emptyCasePresent = false;
	if (i)
	{
		// Reading of the 4 lines
		char a[4][4];
		string line;
		for(int lineIndex = 0 ; lineIndex < 4 ; ++lineIndex)
		{
			getline(i, line);
			for(int colIndex = 0 ; colIndex < 4 ; ++colIndex)
			{
				if (line[colIndex] == '.')
					emptyCasePresent = true;
				a[lineIndex][colIndex] = line[colIndex];
			}
		}

		// Grid analysis
		for(int colId = 0 ; colId < 4 ; ++colId)
		{
			int xc, oc = xc = 0;
			for(int rowId = 0 ; rowId < 4 ; ++rowId)
			{
				if (a[rowId][colId] == 'X' || a[rowId][colId] == 'T')
					++xc;
				if (a[rowId][colId] == 'O' || a[rowId][colId] == 'T')
					++oc;
			}

			if (xc == 4)
				return "X won";
			if (oc == 4)
				return "O won";
		}

		for(int rowId = 0 ; rowId < 4 ; ++rowId)
		{
			int xc, oc = xc = 0;
			for(int colId = 0 ; colId < 4 ; ++colId)
			{
				if (a[rowId][colId] == 'T')
				{
					xc++;
					oc++;
				}
				if (a[rowId][colId] == 'X')
					xc++;
				if (a[rowId][colId] == 'O')
					oc++;
				if (xc == 4)
					return "X won";
				if (oc == 4)
					return "O won";
			}
		}

		// Diagonales
		int xc, oc = xc = 0;
		for(int i = 0 ; i < 4 ; i++)
		{
			switch (a[i][i])
			{
				case 'T':
					{
						++xc;
						++oc;
					}
					break;
				case 'X':
					{
						++xc;
					}
					break;
				case 'O':
					{
						++oc;
					}
			}
		}
		if (xc == 4)
			return "X won";
		if (oc == 4)
			return "O won";

		xc = oc = 0;
		for(int i = 0 ; i < 4 ; i++)
		{
			switch (a[i][3 - i])
			{
				case 'T':
					{
						++xc;
						++oc;
					}
					break;
				case 'X':
					{
						++xc;
					}
					break;
				case 'O':
					{
						++oc;
					}
			}
		}
		if (xc == 4)
			return "X won";
		if (oc == 4)
			return "O won";
	}

	return (emptyCasePresent ? "Game has not completed" : "Draw");
}

void resolve(char *filename, solve_Tpf func)
{
	if (func == 0)
		return;

	ifstream i(filename);

	if (i)
	{
		int index;
		string line;
		getline(i, line);
		int testcases = atoi(line.c_str());

		for(index = 1 ; index <= testcases ; ++index)
		{
			cout << "Case #" << index << ": " << func(i) << endl;
			getline(i, line);
		}

		i.close();
	}
}

int main(int argc, char **argv)
{
	if (argc != 2)
		usage();

	//storeCredit(argv[1]);
	//time_t startingTime = time(0);
	resolve(argv[1], &tictactoe);
	//cout << "Execute en " << (time(0) - startingTime) << endl;

	return EXIT_SUCCESS;
}
