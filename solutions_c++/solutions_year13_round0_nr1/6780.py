#include <fstream>

using namespace std;

char matrix[4][4];

ifstream fin("input.txt");
ofstream fout("output.txt");

bool is_correct(char a, char b, char c, int d)
{
	if (a == '.' || b == '.' || c == '.' || d == '.')
		return false;
	if (a == b && a == c)
	{
		if (d == a || d == 'T')
			return true;
	}
	else if (a == c && a == d)
	{
		if (b == a || b == 'T')
			return true;
	}
	else if (b == c && b == d)
	{
		if (a == b || a == 'T')
			return true;
	}
	else if (a == b && a == d)
	{
		if (c == a || c == 'T')
			return true;
	}
	return false;
}

bool is_won()
{
	for (int j = 0; j < 4; ++j)
	{
		if (is_correct(matrix[j][0], matrix[j][1], matrix[j][2], matrix[j][3]))
		{
			fout << (matrix[j][0] == 'T' ? matrix[j][1] : matrix[j][0]) << " won\n";
			return true;
		}
	}
	for (int j = 0; j < 4; ++j)
	{
		if (is_correct(matrix[0][j], matrix[1][j], matrix[2][j], matrix[3][j]))
		{
			fout << (matrix[0][j] == 'T' ? matrix[1][j] : matrix[0][j]) << " won\n";
			return true;
		}
	}
	if (is_correct(matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3]))
	{
		fout << (matrix[0][0] == 'T' ? matrix[1][1] : matrix[0][0]) << " won\n";
		return true;
	}
	if (is_correct(matrix[0][3], matrix[1][2], matrix[2][1], matrix[3][0]))
	{
		fout << (matrix[0][3] == 'T' ? matrix[1][2] : matrix[0][3]) << " won\n";
		return true;
	}
	return false;
}

bool is_draw()
{
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (matrix[i][j] == '.')
				return false;
	return true;
}

int main()
{
	int N;

	fin >> N;

	for (int i = 0; i < N; ++i)
	{
		
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				fin >> matrix[i][j];

		fout << "Case #" << (i+1) << ": ";
		if (!is_won())
		{
			if (is_draw())
				fout << "Draw\n";
			else
				fout << "Game has not completed\n";
		}
	}
	return 0;
}