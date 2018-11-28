#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;
typedef long long LL;
typedef vector<LL> VLL;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
const int INF = 1000000001;
const double EPS = 10e-9;

struct Block
{
	vector<pair<int, int>> comp;
	int family;
	Block(vector<pair<int, int>> comp, int family)
	{
		this->comp = comp;
		this->family = family;
	}
};

struct Board
{
	const int n, m;
	vector<vector<bool>> board;
	Board(int x, int y) : n(x), m(y), board(x, vector<bool>(y, false))
	{
	}
	void Print()
	{
		REP(x, m + 2) cout << "-";
		cout << endl;
		REP(x, n)
		{
			cout << "|";
			REP(y, m)
			{
				if(board[x][y]) cout << "X";
				else cout << " ";
			}
			cout << "|\n";
		}
		REP(x, m + 2) cout << "-";
		cout << endl;
	}
	void Clear()
	{
		REP(x, n) REP(y, m) board[x][y] = false;
	}
	bool IsFull()
	{
		REP(x, n) REP(y, m) if(!board[x][y]) return false;
		return true;
	}
	bool Add(Block& block, int x, int y)
	{
		auto tmp = board;
		for(auto it : block.comp)
		{
			if(it.ST + x >= n|| it.ND + y >= m || tmp[it.ST + x][it.ND + y])
				return false;
			tmp[it.ST + x][it.ND + y] = true;
		}
		board = tmp;
		return true;
	}
};

struct Polyomino
{
	vector<Block> blocks;

	void Print()
	{
		Board board(4, 4);
		for(auto it: blocks)
		{
			board.Clear();
			board.Add(it, 0, 0);
			board.Print();
		}
	}

	bool Solve(Board& board)
	{
		set<int> k;
		for(auto block : blocks) if(k.find(block.family) == k.end())
		{
			bool can = false;
			// Board disp(4, 4);
			// disp.Add(block, 0, 0);
			// disp.Print();
			REP(x, board.n)
			{
				REP(y, board.m)
				{
					board.Clear();
					if(board.Add(block, x, y))
					{
						// board.Print();
						if(Try(board))
						{
							// cout << "Potrafi!\n";
							can = true;
							break;
						}
					}
				}
				if(can) break;
			}
			if(can) k.insert(block.family);
		}
		for(auto block : blocks) if(k.find(block.family) == k.end()) return false;
		return true;
	}
	bool Try(Board& board)
	{
		if(board.IsFull()) return true;
		for(auto block : blocks)
		{
			REP(x, board.n)
			{
				REP(y, board.m)
				{
					auto tmp = board;
					if(tmp.Add(block, x, y) && Try(tmp))
					{
						return true;
					}
				}
			}
		}
		return false;
	}
};

struct Monomino : public Polyomino
{
	Monomino()
	{
		blocks.PB(Block({{0, 0}}, 0));
	}
};

struct Domino : public Polyomino
{
	Domino()
	{
		blocks.PB(Block({{0, 0},{0, 1}}, 0));
		blocks.PB(Block({{0, 0},{1, 0}}, 0));
	}
};

struct Tromino : public Polyomino
{
	Tromino()
	{
		blocks.PB(Block({{0, 0},{0, 1},{0, 2}}, 0));
		blocks.PB(Block({{0, 0},{1, 0},{2, 0}}, 0));

		blocks.PB(Block({{0, 0},{0, 1},{1, 0}}, 1));
		blocks.PB(Block({{0, 0},{0, 1},{1, 1}}, 1));
		blocks.PB(Block({{0, 1},{1, 1},{1, 0}}, 1));
		blocks.PB(Block({{0, 0},{1, 0},{1, 1}}, 1));
	}
};

struct Tetromino : public Polyomino
{
	Tetromino()
	{
		blocks.PB(Block({{0, 0},{0, 1},{0, 2},{0, 3}}, 0));
		blocks.PB(Block({{0, 0},{1, 0},{2, 0},{3, 0}}, 0));

		blocks.PB(Block({{0, 0},{1, 0},{2, 0},{0, 1}}, 1));
		blocks.PB(Block({{0, 0},{0, 1},{1, 1},{2, 1}}, 1));
		blocks.PB(Block({{0, 0},{1, 0},{2, 0},{2, 1}}, 1));
		blocks.PB(Block({{2, 0},{0, 1},{1, 1},{2, 1}}, 1));

		blocks.PB(Block({{0, 0},{0, 1},{0, 2},{1, 2}}, 1));
		blocks.PB(Block({{0, 0},{0, 1},{0, 2},{1, 0}}, 1));
		blocks.PB(Block({{0, 0},{1, 0},{1, 1},{1, 2}}, 1));
		blocks.PB(Block({{0, 2},{1, 0},{1, 1},{1, 2}}, 1));

		blocks.PB(Block({{0, 0},{1, 0},{1, 1},{0, 1}}, 2));

		blocks.PB(Block({{1, 0},{1, 1},{0, 1},{0, 2}}, 3));
		blocks.PB(Block({{0, 0},{0, 1},{1, 1},{1, 2}}, 3));
		blocks.PB(Block({{0, 0},{1, 0},{1, 1},{2, 1}}, 3));
		blocks.PB(Block({{0, 1},{1, 1},{1, 0},{2, 0}}, 3));

		blocks.PB(Block({{0, 0},{0, 1},{0, 2},{1, 1}}, 4));
		blocks.PB(Block({{1, 0},{1, 1},{1, 2},{0, 1}}, 4));
		blocks.PB(Block({{0, 0},{1, 0},{2, 0},{1, 1}}, 4));
		blocks.PB(Block({{0, 1},{1, 1},{2, 1},{1, 0}}, 4));
	}
};



int main()
{
	int t, n, r, c;
	cin >> t;
	FOR(o, 1, t)
	{
		cin >> n >> r >> c;
		Polyomino* poly;
		switch(n)
		{
		case 1:
			poly = new Monomino();
			break;
		case 2:
			poly = new Domino();
			break;
		case 3:
			poly = new Tromino();
			break;
		case 4:
			poly = new Tetromino();
			break;
		}
		Board board(r, c);
		cout << "Case #" << o << ": ";
		if(poly->Solve(board))
			cout << "GABRIEL\n";
		else
			cout << "RICHARD\n";
	}
	return 0;
}