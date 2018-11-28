#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef int Board[100][100];

void printBoard(const Board& map, int n, int m)
{
	for (int row=0; row < n; ++row)
	{
		for (int col=0; col<m; ++col)
			cerr << map[row][col];
		cerr << endl;
	}
}

bool rowTest(const Board& map, int n, int m, int i, int j)
{
	int c = map[i][j];
	for (int k=0; k<n; ++k)
		if (map[k][j] > c)
			return false;
	return true;
}

bool colTest(const Board& map, int n, int m, int i, int j)
{
	int c = map[i][j];
	for (int k=0; k<m; ++k)
		if (map[i][k] > c)
			return false;
	return true;
}

bool processCase(istream &in)
{
	int n, m;
	in >> n >> m;
	Board map;
	int i, j;
	for (i=0; i<n; ++i)
		for (j=0; j<m; ++j)
			in >> map[i][j];
	for (i=0; i<n; ++i)
		for (j=0; j<m; ++j)
			if (!rowTest(map, n, m, i, j) && !colTest(map, n, m, i, j))
				return false;
	return true;
}

void process(istream &in, ostream &out)
{
	int cases;
	in >> cases;
	for (int i=1; i<=cases; ++i)
	{
		out << "Case #" << i << ": " << (processCase(in) ? "YES" : "NO") << endl;
	}
}

int main(int argc, char* argv[])
{
	if (argc == 1)
	{
		process(cin, cout);
	}
	else if (argc == 2)
	{
		ifstream in(argv[1], ifstream::in);
		process(in, cout);
	}
	return 0;
}
