#include "Board.h"


Board::Board(void)
{
	_size = 4;
}


Board::~Board(void)
{
}

ostream& operator<<(ostream& os, Board b)
{
	unsigned int size = b.GetSize();

	for(int row = 0; row < size; row++)
	{
		for(int col = 0; col < size; col++)
		{
			os << b.GetCellChar(row, col);
		}

		os << endl;
	}

	return os;
}