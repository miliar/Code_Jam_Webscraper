#include <iostream>
#include <fstream>

using namespace std;

ifstream input ("input.txt");
ofstream output ("output.txt");

bool check()
{
	int N, M; //N - row amount, M - column amount
	input >> N;
	input >> M;
	cout << N;
	cout << M;
	int ** grid; //pointer to the grid
	int * rows; //highest grass in a row
	int * columns; // highest grass in a column

	rows = new int [N];
	columns = new int [M];

	for(int i = 0;i < N;i++) //initialize rows
	{
		rows[i] = 0;
	}

	for(int i = 0; i < M;i++) //initialize columns
	{
		columns[i] = 0;
	}

	grid = new int * [N]; // create the grid
	for(int i = 0;i < N;i++)
	{
		grid[i] = new int [M];
	}

	for(int i = 0;i < N;i++) //fill the grid
	{
		for(int i2 = 0;i2 < M;i2++)
		{
			input >> grid[i][i2];
			if(grid[i][i2] > columns[i2]) columns[i2] = grid[i][i2]; //get max values in row/column
			if(grid[i][i2] > rows[i]) rows[i] = grid[i][i2];
		}
	}
	for(int i = 0;i < N;i++)
	{
		for(int i2 = 0;i2 < M;i2++)
		{
			if((grid[i][i2] != columns[i2])&&(grid[i][i2] != rows[i])) return false;
		}
	}
	return true;
}

int main()
{

    int T;

    input >> T;

    for(int i = 1;i <= T;i++)
    {
    	output << "Case #" << i << ": ";
    	if(check()) output << "YES\n";
    	else output << "NO\n";
    }
    return 0;
}
