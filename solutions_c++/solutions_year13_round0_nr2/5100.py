#include <fstream>
#include <algorithm>
using namespace std;

int pos (int x, int y, int width)
{
	return (y * width) + x;
}

int main (void)
{
	fstream input("B-large.in");
	ofstream output("B-large.out");

	int T;
	input >> T;

	for (int t = 1; t <= T; t++)
	{
		int M, N;
		input >> N;
		input >> M;

		int *grid = new int[N*M];
		//read in the pattern
		for (int n = 0; n < N; n++)
			for (int m = 0; m < M; m++)
				input >> grid[pos(m, n, M)];

		//get the max height for each row/column
		int* rows = new int[N]();
		int* columns = new int[M]();

		//find the minimum height setting that the mower can have for each row and column
		for (int x = 0; x < M; x++)
			for (int y = 0; y < N; y++)
			{
				int height = grid[pos(x, y, M)];

				if (height > rows[y])
					rows[y] = height;

				if (height > columns[x])
					columns[x] = height;
			}

		//pass again over all the values and see if it is possible,
		//now knowing what settings the mower must be at

		bool valid = true;

		for (int x = 0; x < M; x++)
			for (int y = 0; y < N; y++)
			{
				int height = grid[pos(x, y, M)];
				
				int minMow = min(rows[y], columns[x]);

				if (height != minMow)
					valid = false;
			}

		//output answer
		output << "Case #" << t << ": ";

		if (valid)
			output << "YES";
		else
			output << "NO";

		if (t != T)
			output << endl;

		//delete data
		delete[] grid;
		delete[] rows;
		delete[] columns;
	}

	input.close();
	output.close();
}