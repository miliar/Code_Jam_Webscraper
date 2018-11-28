#include <iostream>
#include <direct.h>
#include <assert.h>
#include <vector>
using namespace std;

int R, C, M;
char MINE = '*';

class Matrix
{
public:
	void create() 
	{
		mat.clear();

		string s;
		for (int i=0; i<C; i++)
			s += '.';

		for (int i=0; i<R; i++)
			mat.push_back(s);
	}

	void makeSolution2(int rows, int cols, int mm)
	{
		int mines = 0;
		for (int r=rows-1; r>=0; r--)
		{
			for (int c=cols-1; c>=0; c--)
			{
				if ((mines < mm) && (c >= 2))
				{
					mat[r][c] = MINE;
					mines++;
				}
				else if ((c==0) && (r==0))
					mat[r][c] = 'c';
				else 
					mat[r][c] = '.';
			}
		}
	}

	void fillRow(int row, int col)
	{
		for (int c=0; c<col; c++)
			mat[row-1][c] = MINE;
	}

	void fillCol(int row, int col)
	{
		for (int r=0; r<row; r++)
			mat[r][col-1] = MINE;
	}

	void print()
	{
		for (int r=0; r<R; r++)
		{
			for (int c=0; c<C; c++)
				cout << mat[r][c];
			cout << endl;
		}
	}

	int findNeighbors(int r, int c)
	{
		if (r<0 || r>=R)
			return -1;
		if (c<0 || c>=C)
			return -1;

		int n = 0;
		for (int i=-1; i<=1; i++)
		{
			if ((r+i<0) || r+i>=R)
				continue;

			for (int j=-1; j<=1; j++)
			{
				if ((c+j<0) || c+j>=C)
					continue;

				if (mat[r+i][c+j]==MINE)
					n++;
			}
		}
		return n;
	}

	void solveBoard(int r, int c)
	{
		for (int i=-1; i<=1; i++)
		{
			if ((r+i<0) || r+i>=R)
				continue;

			for (int j=-1; j<=1; j++)
			{
				if ((c+j<0) || c+j>=C)
					continue;

				if (i==0 && j==0)	// skip my pos
					continue;

				if (mat[r+i][c+j] != '.')
					continue;

				int n = findNeighbors(r+i, c+j);
				assert(n>=0);
				mat[r+i][c+j] = (char)n + '0';
				if (n == 0)
					solveBoard(r+i, c+j);
			}
		}
	}

	bool validateBoard()
	{
		for (int r=0; r<R; r++)
			for (int c=0; c<C; c++)
				if (mat[r][c]=='.')
					return false;
		return true;
	}

	bool readBoard()
	{
		freopen("board.in",  "r", stdin);
		freopen("board.out", "w", stdout);
		char* row = new char[C+1];

		int sr = 0, sc = 0;	//startPos 
		for (int r=0; r<R; r++)
		{
			for (int c=0; c<C; c++)
			{
				char ch;
				cin >> ch;
				assert(ch=='.'||ch=='c'||ch==MINE);
				row[c] = ch;
				if (ch == 'c')
				{
					sc = c;
					sr = r;
				}
			}
			row[C] = 0;
			mat.push_back(row);
		}

		delete[] row;

		mat[sr][sc] = (char)('0' + findNeighbors(sr, sc));
		if (mat[sr][sc] == '0')
			solveBoard(sr, sc);

		bool solved = validateBoard();
		print();
		cout << solved << endl;
		return solved;
	}

private:
	vector<string> mat;
};
Matrix mat;

// factor * factor2 = prod (factor>=2)
// Return: -1 if not found
int findWFactor(int prod)
{
	if (R==1)
		return prod;
	if (C==1)
		return 1;

	int maxFactor = prod/2;
	maxFactor = min(maxFactor, C);

	for (int i=2; i<=maxFactor; i++)
		if (prod % i == 0)
			if (prod/i <= R)
				return i;

	return -1;
}

void printSolution1(int w, int h)
{
	for (int r=0; r<R; r++)
	{
		for (int c=0; c<C; c++)
		{
			if ((r==0) && (c==0))
				cout << 'c';
			else if ((c < w) && (r < h))
				cout << '.';
			else 
				cout << MINE;
		}
		cout << endl;
	}
}

// xxxx..
// ......
// .....c
// Need at least 2 spaces from the mines.
void printSolution2()
{
	int mines = 0;
	for (int r=0; r<R; r++)
	{
		for (int c=0; c<C; c++)
		{
			if ((mines < M) && (c < C-2))
			{
				cout << MINE;
				mines++;
			}
			else if ((c==C-1) && (r==R-1))
				cout << 'c';
			else 
				cout << '.';
		}
		cout << endl;
	}
}

bool findSolution(int row, int col, int mm)
{
	if (mm < 0)
		return false;

	int maxLim = max(0, (row-2)*(col-2));
	if (mm <= maxLim)
	{
		mat.makeSolution2(row, col, mm);
		return true;
	}

	if (row>2)
		if (findSolution(row-1, col, mm-col))
		{
			mat.fillRow(row, col);
			return true;
		}

	if (col>2)
		if (findSolution(row, col-1, mm-row))
		{
			mat.fillCol(row, col);
			return true;
		}

	return false;
}

void runCase(int Case)
{
    cout << "Case #" << Case+1 << ": " << endl;
	cerr << "Case #" << Case+1 << endl;

	int remain = R*C - M;
	int maxMine_Sol2 = (R-2)*(C-2);

	if (M <= maxMine_Sol2)
		printSolution2();
	else if (remain == 1)
		printSolution1(1, 1);
	else 
	{
		int factor = findWFactor(remain);
		if (factor > 0)
			printSolution1(factor, remain/factor);
		else
		{
			mat.create();
			if (findSolution(R, C, M))
				mat.print();
			else
				cout << "Impossible" << endl;
		}
	}
}


void Run()
{
    int T;
    cin >> T;
	cerr << T << " cases" << endl;

    for (int i=0; i < T; i++)
    {
		// Read input
        cin >> R;
		cin >> C;
		cin >> M;

		// Solve
        runCase(i);
    }
}


void main()
{
    _chdir(".\\Archive_Google");

	#define FILE_NAME "C-small-attempt2" 
    FILE* in = freopen(FILE_NAME ".in",  "r", stdin);
    FILE* out= freopen(FILE_NAME ".out", "w", stdout);
	assert(in!=NULL && out!=NULL);

    Run();
	//R=4; C=5; readBoard();

    //system("pause");
}

