#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <complex>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

struct Pos
{
	Pos() {}
	Pos(int y, int x, int dy, int dx)
		: y(y), x(x), dy(dy), dx(dx)
	{
	}
	int y;
	int x;
	int dy;
	int dx;
};

VVI vMaze;
int R;
int C;

Pos startpos(int n, int R, int C)
{
	if (0 <= n && n < C)
		return Pos(-1, n, 1, 0);
	n -= C;
	if (0 <= n && n < R)
		return Pos(n, C, 0, -1);
	n -= R;
	if (0 <= n && n < C)
		return Pos(R, C-1-n, -1, 0);
	n -= C;
	return Pos(R-1-n, -1, 0, 1);
}

Pos go(Pos pos, int steps)
{
	pos.y += pos.dy;
	pos.x += pos.dx;
	if (pos.y < 0 || pos.y >= R || pos.x < 0 || pos.x >= C)
		return pos;
	if (vMaze[pos.y][pos.x] == 0)
	{
		swap(pos.dy, pos.dx);
	}
	else
	{
		swap(pos.dy, pos.dx);
		pos.dy *= -1;
		pos.dx *= -1;
	}
	return go(pos, steps+1);
}

int main()
{
	int T;
	cin >> T;
	for (int t=1; t<=T; t++)
	{
		cout << "Case #" << t << ":" << endl;

		cin >> R >> C;
		int N = 2 * (R + C);
		VI love(N);
		for (int i=0; i<N; i++)
		{
			cin >> love[i];
			love[i]--;
		}

		vector<Pos> vPos;
		for (int i=0; i<N; i++)
			vPos.push_back(startpos(i, R, C));

		bool any = false;

		vMaze.assign(R, VI(C, 0));
		int MazeEnd = (1 << (R*C));
		for (int maze=0; maze<MazeEnd; maze++)
		{
			int _maze = maze;
			for (int r=0; r<R; r++)
				for (int c=0; c<C; c++)
				{
					vMaze[r][c] = _maze & 1;
					_maze = (_maze >> 1);
				}

			bool legal = true;
			for (int i=0; i<N; i+=2)
			{
				Pos dst = go(vPos[love[i]], 0);
				Pos dst2 = vPos[love[i+1]];
				if (dst.y != dst2.y || dst.x != dst2.x)
				{
					legal = false;
					break;
				}
			}

			if (legal)
			{
				for (int r=0; r<R; r++)
				{
					for (int c=0; c<C; c++)
						cout << (vMaze[r][c] == 0 ? '\\' : '/');
					cout << endl;
				}
				any = true;
				break;
			}

		}


		/*
		cerr << "R=" << R << " C=" << C << endl;
		for (int i=0; i<N; i++)
			cerr << i << ": " << startpos(i, R, C) << endl;
		cerr << endl;
		*/

		if (!any)
			cout << "IMPOSSIBLE" << endl;
	}
    return 0;
}