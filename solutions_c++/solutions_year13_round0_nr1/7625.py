// TicTacToeTomek.cpp : Defines the entry point for the console application.
//
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <algorithm>
#include <functional>
#include <vector>

using namespace std;


template<typename T>
T ConvertInt(string number)
{
    stringstream ss;
    T no;

    ss << number;
    ss >> no;

    return no;
}

template<typename T>
string ConvertString(T number)
{
    stringstream ss;
    string no;

    ss << number;
    ss >> no;

    return no;
}


int main(int argc, char* argv[])
{
	string lineBuffer;
	ifstream file;
	ofstream fileoutput;

	file.open(argv[1]);
	fileoutput.open("./output.txt");

	if (!file.is_open())
		throw exception("Input file couldn't be opened!");

	getline(file, lineBuffer);
	int Cases = ConvertInt<int>(lineBuffer);

	for (int k = 0; k < Cases; k++)
	{
		char grid[4][4];
		bool XWon = false;
		bool OWon = false;
		size_t EmptyCellsCount = 0;

		cout << "Case #" << k + 1 << ": ";
		fileoutput << "Case #" << k + 1 << ": ";

		for (int i = 0; i < 4; i++)
		{
			getline(file, lineBuffer);
			
			stringstream ss;
			ss << lineBuffer;
			
			for (int j = 0; j < 4; j++)
			{
				char cell;
				
				ss >> cell;
				grid[i][j] = cell;

				if (cell == '.')
					EmptyCellsCount++;
			}
		}

		// Check all rows
		for (int i = 0; i < 4; i++)
		{
			string row;

			for (int j = 0; j < 4; j++)
			{
				row += grid[i][j];
			}

			size_t Xn = count(row.begin(), row.end(), 'X');
			size_t On = count(row.begin(), row.end(), 'O');
			size_t Tn = count(row.begin(), row.end(), 'T');

			if (Xn + Tn == 4)
			{
				XWon = true;

				break;
			}
			else if (On + Tn == 4)
			{
				OWon = true;

				break;
			}
		}

		// Check for win
		if (XWon)
		{
			cout << "X won" << endl;
			fileoutput << "X won" << endl;
			goto Next;
		}
		else if (OWon)
		{
			cout << "O won" << endl;
			fileoutput << "O won" << endl;
			goto Next;
		}

		// Check all columns
		for (int j = 0; j < 4; j++)
		{
			string col;

			for (int i = 0; i < 4; i++)
			{
				col += grid[i][j];
			}

			size_t Xn = count(col.begin(), col.end(), 'X');
			size_t On = count(col.begin(), col.end(), 'O');
			size_t Tn = count(col.begin(), col.end(), 'T');

			if (Xn + Tn == 4)
			{
				XWon = true;

				break;
			}
			else if (On + Tn == 4)
			{
				OWon = true;

				break;
			}
		}

		// Check for win
		if (XWon)
		{
			cout << "X won" << endl;
			fileoutput << "X won" << endl;
			goto Next;
		}
		else if (OWon)
		{
			cout << "O won" << endl;
			fileoutput << "O won" << endl;
			goto Next;
		}

		// Check all left right diagonal
		{
			string dia;

			for (int ij = 0; ij < 4; ij++)
			{
				dia += grid[ij][ij];
			}

			size_t Xn = count(dia.begin(), dia.end(), 'X');
			size_t On = count(dia.begin(), dia.end(), 'O');
			size_t Tn = count(dia.begin(), dia.end(), 'T');

			if (Xn + Tn == 4)
				XWon = true;
			else if (On + Tn == 4)
				OWon = true;
		}

		// Check for win
		if (XWon)
		{
			cout << "X won" << endl;
			fileoutput << "X won" << endl;
			goto Next;
		}
		else if (OWon)
		{
			cout << "O won" << endl;
			fileoutput << "O won" << endl;
			goto Next;
		}


		// Check right to left diagonal
		{
			string dia;

			for (int ij = 0; ij < 4; ij++)
			{
				dia += grid[ij][3 - ij];
			}

			size_t Xn = count(dia.begin(), dia.end(), 'X');
			size_t On = count(dia.begin(), dia.end(), 'O');
			size_t Tn = count(dia.begin(), dia.end(), 'T');

			if (Xn + Tn == 4)
				XWon = true;
			else if (On + Tn == 4)
				OWon = true;
		}

		// Check for win
		if (XWon)
		{
			cout << "X won" << endl;
			fileoutput << "X won" << endl;
			goto Next;
		}
		else if (OWon)
		{
			cout << "O won" << endl;
			fileoutput << "O won" << endl;
			goto Next;
		}

		if (EmptyCellsCount == 0)
		{
			cout << "Draw" << endl;
			fileoutput << "Draw" << endl;
		}
		else
		{
			cout << "Game has not completed" << endl;
			fileoutput << "Game has not completed" << endl;
		}

		Next:
		// Ignore last empty line
		getline(file, lineBuffer);
	}

	return 0;
}