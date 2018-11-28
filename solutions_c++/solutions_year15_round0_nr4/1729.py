#include <iostream>
#include <fstream>
#include <algorithm>
#include <list>

#define READFROMFILE
#define WRITETOFILE

int X;
int rows, cols;
int colLimit;
int map[21][21];

struct Pos
{
	enum Dir {Up, Down, Left, Right};
	int row;
	int col;
	Pos(){}
	Pos(int row, int col) : row(row), col(col)
	{}

	Pos move(Dir dir) const
	{
		Pos newPos(*this);

		switch (dir)
		{
		case Up:
			newPos.row--;
			break;
		case Down:
			newPos.row++;
			break;
		case Left:
			newPos.col--;
			break;
		case Right:
			newPos.col++;
			break;
		}
		return newPos;
	}

	inline bool isValid() const
	{
		return 0 <= row && row < rows && 0 <= col && col <= colLimit;
	}
};



bool placeBlock(int remainingEmptyPlace, int blocksToPlace, std::list<Pos> &available)
{
	if (remainingEmptyPlace == 0 && blocksToPlace == 0)
		return true;

	if (blocksToPlace == 0)
	{
		if (remainingEmptyPlace < X)
			return false;

		std::list<Pos> newAvailable;
		placeBlock(remainingEmptyPlace, X, newAvailable);
	}
	else
	{
		Pos picked = available.front();
		available.pop_front();

		map[picked.row][picked.col] = 1;

		const Pos newPos[] = { picked.move(Pos::Up), picked.move(Pos::Down), picked.move(Pos::Left), picked.move(Pos::Right) };

		for (int i = 0; i < 4; i++)
		{
			if (newPos[i].isValid())
			{
				available.push_back(newPos[i]);
			}
		}

		placeBlock(remainingEmptyPlace - 1, blocksToPlace - 1, available);
	}
	return false;
}
/*
bool test()
{
	if ((rows * cols) % X != 0)
		return false;

	for (int row = 0; row < rows; row++)
		for (int col = 0; col < cols; col++)
			map[row][col] = 0;

	if (rows < cols)
	{
		int tmp = cols;
		cols = rows;
		rows = tmp;
	}

	colLimit = std::min((int)std::ceil(sqrt(X)), cols - 1);
	std::list<Pos> newAvailable;
	newAvailable.push_back(Pos(0, 0));
	return placeBlock(cols * rows, X, newAvailable);
}
*/

bool test()
{
	if ((rows * cols) % X != 0)
		return false;
	if (rows >= 3 && cols >= 3 && X >= 7)
		return false;
	for (int len = 1; len < X; len++)
		if (len > rows || len > cols)
			return false;

	return true;
}

int main()
{
	int numOfTestCases;

#ifdef READFROMFILE
	std::ifstream input("ProblemD.in", std::ifstream::in);
#else
	std::istream &input = std::cin;
#endif

#ifdef WRITETOFILE
	std::ofstream output("ProblemD.out", std::ofstream::out);
#else
	std::ostream &output = std::cout;
#endif

	input >> numOfTestCases;

	for (int testCase = 1; testCase <= numOfTestCases; testCase++)
	{
		input >> X >> rows >> cols;

		

		output << "Case #" << testCase << ": " << (test() ? "GABRIEL" : "RICHARD") << std::endl;
#ifdef WRITETOFILE
		std::cout << "Case #" << testCase << ": " << (test() ? "GABRIEL" : "RICHARD") << std::endl;
#endif
	}
}