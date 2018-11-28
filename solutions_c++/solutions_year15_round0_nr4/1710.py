#include <iostream>
#include <string>
#include <vector>
#include <queue>

const int RICHARD = -1;
const int GABRIEL =  1;

const int N = 4 * 2 - 1;

typedef std::vector< std::vector<int> > Omino;
typedef std::vector< std::vector<Omino> > OminoVector;

OminoVector omino3(2);
int init_omino3()
{
	omino3[0].push_back(Omino({{1,1,1},{0,0,0},{0,0,0}}));
	omino3[0].push_back(Omino({{1,0,0},{1,0,0},{1,0,0}}));
	
	/*
	110 100 010 110
	100 110 110 010
	000 000 000 000
	*/
	omino3[1].push_back(Omino({{1,1,0},{1,0,0},{0,0,0}}));
	omino3[1].push_back(Omino({{1,0,0},{1,1,0},{0,0,0}}));
	omino3[1].push_back(Omino({{0,1,0},{1,1,0},{0,0,0}}));
	omino3[1].push_back(Omino({{1,1,0},{0,1,0},{0,0,0}}));
	
	return 0;
}

OminoVector omino4(5);
int init_omino4()
{
	omino4[0].push_back(Omino({{1,1,0,0},{1,1,0,0},{0,0,0,0},{0,0,0,0}}));
	
	omino4[1].push_back(Omino({{1,1,1,1},{0,0,0,0},{0,0,0,0},{0,0,0,0}}));
	omino4[1].push_back(Omino({{1,0,0,0},{1,0,0,0},{1,0,0,0},{1,0,0,0}}));
	
	/*
	1000 0110 1100 0100
	1100 1100 0110 1100
	0100 0000 0000 1000
	0000 0000 0000 0000
	*/
	omino4[2].push_back(Omino({{1,0,0,0},{1,1,0,0},{0,1,0,0},{0,0,0,0}}));
	omino4[2].push_back(Omino({{0,1,1,0},{1,1,0,0},{0,0,0,0},{0,0,0,0}}));
	omino4[2].push_back(Omino({{1,1,0,0},{0,1,1,0},{0,0,0,0},{0,0,0,0}}));
	omino4[2].push_back(Omino({{0,1,0,0},{1,1,0,0},{1,0,0,0},{0,0,0,0}}));
	
	/*
	1110 0100 0100 1000
	0100 1100 1110 1100
	0000 0100 0000 1000
	0000 0000 0000 0000
	*/
	omino4[3].push_back(Omino({{1,1,1,0},{0,1,0,0},{0,0,0,0},{0,0,0,0}}));
	omino4[3].push_back(Omino({{0,1,0,0},{1,1,0,0},{0,1,0,0},{0,0,0,0}}));
	omino4[3].push_back(Omino({{0,1,0,0},{1,1,1,0},{0,0,0,0},{0,0,0,0}}));
	omino4[3].push_back(Omino({{1,0,0,0},{1,1,0,0},{1,0,0,0},{0,0,0,0}}));
	
	/*
	1100 1110 0100 1000 1100 1110 1000 0010
	1000 0010 0100 1110 0100 1000 1000 1110
	1000 0000 1100 0000 0100 0000 1100 0000
	0000 0000 0000 0000 0000 0000 0000 0000
	*/
	omino4[4].push_back(Omino({{1,1,0,0},{1,0,0,0},{1,0,0,0},{0,0,0,0}}));
	omino4[4].push_back(Omino({{1,1,1,0},{0,0,1,0},{0,0,0,0},{0,0,0,0}}));
	omino4[4].push_back(Omino({{0,1,0,0},{0,1,0,0},{1,1,0,0},{0,0,0,0}}));
	omino4[4].push_back(Omino({{1,0,0,0},{1,1,1,0},{0,0,0,0},{0,0,0,0}}));
	omino4[4].push_back(Omino({{1,1,0,0},{0,1,0,0},{0,1,0,0},{0,0,0,0}}));
	omino4[4].push_back(Omino({{1,1,1,0},{1,0,0,0},{0,0,0,0},{0,0,0,0}}));
	omino4[4].push_back(Omino({{1,0,0,0},{1,0,0,0},{1,1,0,0},{0,0,0,0}}));
	omino4[4].push_back(Omino({{0,0,1,0},{1,1,1,0},{0,0,0,0},{0,0,0,0}}));
	
	return 0;
}

class Board
{
private:
	int *_board;

public:
	Board()
	{
		_board = new int[N * N];
		for(unsigned i=0; i<N*N; ++i) _board[i] = 0;
	}
	
	Board(const Board *board)
	{
		_board = new int[N * N];
		for(unsigned y=0; y<N; ++y)
		{
			for(unsigned x=0; x<N; ++x)
			{
				_board[y*N+x] = board->at(y, x);
			}
		}
	}
	
	int at(unsigned y, unsigned x) const
	{
		if(y < N && x < N) return _board[y*N+x];
		else return 2;
	}
	
	void put(unsigned y, unsigned x)
	{
		++_board[y*N+x];
	}
	
	int answer(unsigned R, unsigned C) const
	{
		int flag = 0;
		
		for(unsigned y=0; y<N; ++y)
		{
			if(y < R)
			{
				for(unsigned x=0; x<C; ++x)
				{
					if(at(y, x) == 0)
					{
						flag = 1;
					}
					else if(at(y, x) > 1)
					{
						return -1;
					}
				}
				for(unsigned x=C; x<N; ++x)
				{
					if(at(y, x) > 0)
					{
						return -1;
					}
				}
			}
			else
			{
				for(unsigned x=0; x<N; ++x)
				{
					if(at(y, x) > 0)
					{
						return -1;
					}
				}
			}
		}
		
		return flag;
	}
	
	void display(unsigned R, unsigned C) const
	{
		for(unsigned y=0; y<N; ++y)
		{
			for(unsigned x=0; x<N; ++x)
			{
				std::cout << at(y, x) << ' ';
				if(x == C-1) std::cout << "| ";
			}
			std::cout << std::endl;
			
			if(y == R-1)
			{
				for(unsigned x=0; x<N; ++x)
					std::cout << ((x==C) ? "+-" : "--");
				std::cout << std::endl;
			}
		}
	}
};

int put3(Board *board, unsigned y, unsigned x, unsigned index, unsigned rotate)
{
	for(unsigned j=0; j<3; ++j)
	{
		for(unsigned i=0; i<3; ++i)
		{
			if(omino3[index][rotate][j][i] == 1)
				board->put(y+j, x+i);
		}
	}
	return 0;
}

int solve3(unsigned R, unsigned C, unsigned index)
{
	unsigned MaxRotate = omino3[index].size();
	
	std::queue<Board*> q;
	q.push( new Board() );
	
	while(!q.empty())
	{
		Board *bd = q.front(); q.pop();
		int f = bd->answer(R, C);
		
		if(f == 0) 
		{
			return GABRIEL;
		}
		
		if(f == 1)
		{
			for(unsigned rotate=0; rotate<MaxRotate; ++rotate)
			{
				for(unsigned y=0; y<R; ++y)
				{
					for(unsigned x=0; x<C; ++x)
					{
						Board *bd2 = new Board(bd);
						put3(bd2, y, x, index, rotate);
						q.push(bd2);
					}
				}
			}
		}
	}
	
	return RICHARD;
}
/*
int solve3(unsigned R, unsigned C)
{
	for(unsigned index=0; index<omino3.size(); ++index)
	{
		if(solve3(R, C, index) == RICHARD) return RICHARD;
	}
	return GABRIEL;
}

int put4(Board *board, unsigned y, unsigned x, unsigned index, unsigned rotate)
{
	for(unsigned j=0; j<4; ++j)
	{
		for(unsigned i=0; i<4; ++i)
		{
			if(omino4[index][rotate][j][i] == 1)
				board->put(y+j, x+i);
		}
	}
	return 0;
}

int solve4(unsigned R, unsigned C, unsigned index)
{
	unsigned MaxRotate = omino4[index].size();
	
	std::queue<Board*> q;
	q.push( new Board() );
	
	while(!q.empty())
	{
		Board *bd = q.front(); q.pop();
		int f = bd->answer(R, C);
		
		if(f == 0) 
		{
			return GABRIEL;
		}
		
		if(f == 1)
		{
			for(unsigned rotate=0; rotate<MaxRotate; ++rotate)
			{
				for(unsigned y=0; y<R; ++y)
				{
					for(unsigned x=0; x<C; ++x)
					{
						Board *bd2 = new Board(bd);
						put4(bd2, y, x, index, rotate);
						q.push(bd2);
					}
				}
			}
		}
	}
	
	return RICHARD;
}

int solve4(unsigned R, unsigned C)
{
	for(unsigned index=0; index<omino4.size(); ++index)
	{
		if(solve4(R, C, index) == RICHARD) return RICHARD;
	}
	return GABRIEL;
}
*/

int solve3(unsigned R, unsigned C)
{
	if(
		   (R == 3 && C == 2) || (R == 2 && C == 3)
		|| (R == 3 && C == 3)
		|| (R == 4 && C == 3) || (R == 3 && C == 4)
	) return GABRIEL;
	else return RICHARD;
}

int solve4(unsigned R, unsigned C)
{
	if(
		   (R == 4 && C == 3) || (R == 3 && C == 4)
		|| (R == 4 && C == 4)
	) return GABRIEL;
	else return RICHARD;
}

int solve(unsigned X, unsigned R, unsigned C)
{
	if(X == 3) return solve3(R, C); else
	if(X == 4) return solve4(R, C); else
	return -1;
}

int main()
{
	unsigned T;
	std::cin >> T;
	
	init_omino3();
	init_omino4();
	
	for(unsigned t=0; t<T; ++t)
	{
		unsigned X, R, C;
		std::cin >> X >> R >> C;
		
		std::cout << "Case #" << (t+1) << ": ";
		
		if(X == 1)
		{
			std::cout << "GABRIEL" << std::endl;
			continue;
		}
		else if(X == 2)
		{
			std::cout << ((R * C % 2 == 0) ? "GABRIEL" : "RICHARD") << std::endl;
			continue;
		}
		else
		{
			std::cout << ((solve(X, R, C) == GABRIEL) ? "GABRIEL" : "RICHARD") << std::endl;
		}
	}
	
	return 0;
}
