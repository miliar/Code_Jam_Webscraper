#include<iostream>
#include<set>
#include<vector>
using namespace std;

void print (int R, int C, int r, int c, int p, int right, int down)
{
	cout << "\n";
	//cout << r << " " << c << " " << p << "\n";
	vector<vector<int> >grid;
	grid.assign(R + 1, vector<int>(C + 1, 0));

	for(int i = 1; i<=r; ++i)
		for(int j = 1; j<= c; ++j)
			grid[i][j] = 1;

	if (right == 1)
	 for(int i = 1; i<=p; ++i)
		 grid[i][c + 1] = 1;

	if (down == 1)
		for(int j = 1; j<=p; ++j)
			grid[r + 1][j] = 1;

	grid[1][1] = 2;

	for(int i = 1; i<=R; ++i, cout << "\n")
		for(int j = 1; j<=C; ++j)
		{
			if (grid[i][j] == 0)cout << '*';
			if (grid[i][j] == 1)cout << '.';
			if (grid[i][j] == 2)cout << 'c';
		}
}

void Solve(int t)
{
	cout << "Case #" << t << ": ";
	int R, C, M;
	cin >> R >> C >> M;
	int N = R * C - M;
	for(int r = 1; r <= R; ++r)
		for(int c = 1; c <= C; ++c)
		{
			int p = N - r*c;
			if (p < 0)continue;
			if (p == 0)
			{
				if (r == 1 && c == 1){print(R, C, 1, 1, 0, 0, 0); return;}
				if (r >= 2 && c >= 2){print(R, C, r, c, 0, 0, 0); return;}
				if (R == 1 || C == 1){print(R, C, r, c, 0, 0, 0); return;}
			}

			if (r != 1 && c != 1)
			{
				if (p == 1)continue;
				if (p < r && c < C){print(R, C, r, c, p, 1, 0); return;}
				if (p < c && r < R){print(R, C, r, c, p, 0, 1); return;}
			}
			if (R >= 2 && C >= 2 && N >= 2*R + 2*C - 4)
			{
				cout << "\n";
				vector<vector<int> >grid;
				grid.assign(R + 1, vector<int>(C + 1, 0));

				for(int i = 1; i<=2; ++i)
					for(int j = 1; j<=C; ++j)
						grid[i][j] = 1;

				for(int i = 1; i<=R; ++i)
					for(int j = 1; j<=2; ++j)
						grid[i][j] = 1;

				grid[1][1] = 2;// cout << "azazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazazaza\n";

				N -= (2*R + 2*C - 4);

				bool flag = false;
				if (N == 0)flag = true;

				for (int i = 3; i<=R && !flag; ++i)
					for(int j = 3; j<=C && !flag; ++j)
					{
						grid[i][j] = 1;
						--N;
						if (N == 0) flag = true;
					}

				for(int i = 1; i<=R; ++i, cout << "\n")
					for(int j = 1; j<=C; ++j)
					{
						if (grid[i][j] == 0)cout << '*';
						if (grid[i][j] == 1)cout << '.';
						if (grid[i][j] == 2)cout << 'c';
					}
					return;
			}
		}

		cout << endl << "Impossible\n";
}

int main()
{
	freopen ("input.txt", "r", stdin );
	freopen("output.txt", "w", stdout);

	int T;
	cin>>T;

	for(int i = 1; i <= T; ++i)
	{
		Solve(i);
	}

}


