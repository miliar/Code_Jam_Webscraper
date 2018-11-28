#include <iostream>

using namespace std;

void increment_level(int grid[100][100], int N, int M, int minimum)
{
	for(int n = 0; n < N; ++n)
	{
		for(int m = 0; m < M; ++m)
		{
			if(grid[n][m] == minimum)
			{
				++grid[n][m];
			}
		}
	}
}
int detect_level(int grid[100][100], int N, int M)
{
	bool same = true;
	int minimum = grid[0][0];

	for(int n = 0; n < N; ++n)
	{
		for(int m = 0; m < M; ++m)
		{
			if(same && grid[n][m] != minimum)
				same = false;

			if(grid[n][m] < minimum)
			{
				minimum = grid[n][m];
			}
		}
	}
	if(same)
		return -1;
	else return minimum;
}

bool check(bool row, int minimum, int grid[100][100], int N, int M, int n, int m)
{
	int K = 0;

	if(row)
	{
		K = N;
	}
	else
	{
		K = M;
	}

	for(int k = 0; k < K; ++k)
	{
		if(row && grid[k][m] != minimum)
		{
			return false;
		}
		if(!row && grid[n][k] != minimum)
		{
			return false;
		}
	}
	return true;
}

bool detect(int grid[100][100], int N, int M)
{
	// Detect lowest setting
	// See if lowest setting is contiguous on either row or column
	// if so, replace lowest with next higher setting
	// if whole field is level, the design is possible
	while(true)
	{
		// is whole field level?
		int minimum = detect_level(grid, N, M);

		if(minimum == -1)
		{
			return true;
		}

		bool ok_n = false;
		bool ok_m = false;
		for(int n = 0; n < N; ++n)
		{
			for(int m = 0; m < M; ++m)
			{
				if(grid[n][m] == minimum)
				{
					ok_n = check(true, minimum, grid, N, M, n, m);
					ok_m = check(false, minimum, grid, N, M, n, m);
					

					if(!ok_n && !ok_m)
					{
						return false;
					}

					if(ok_m)
					{
						break;	// this column is ok
					}
					// if ok_n the row is ok, but we need to continue along the column
				}
			}
		}
		// Seems OK. Replace minimum with minimum + 1
		increment_level(grid, N, M, minimum);

	}

	return false;
}

void main()
{
	
	int T;
	int grid[100][100];

	cin >> T;

	for(int t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";

		int N, M;
		cin >> N >> M;

		for(int n = 0; n < N; ++n)
		{
			for(int m = 0; m < M; ++m)
			{
				cin >> grid[n][m];
			}
		}

		bool result = detect(grid, N, M);

		if(result) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
}