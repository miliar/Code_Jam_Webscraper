#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
#include<cmath>
#include<fstream>
#include<string>
#include<sstream>
#include<cstdlib>
using namespace std;

int minimum(vector<vector<int> > &height, int N, int M, int &locN, int &locM)
{
	int smallest = 101;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (height[i][j] < smallest)
			{
				smallest = height[i][j];
				locN = i;
				locM = j;
			}

	return smallest;
}

int reverse(vector<vector<int> > &height, int N, int M, int smallest, int locN, int locM)
{
	// test row
	int statusRow = 0;
	for (int i = 0; i < M; i++)
		if (height[locN][i] != smallest && height[locN][i] != 101)
			statusRow = -1;
	if (statusRow == 0)
		for (int i = 0; i < M; i++)
			height[locN][i] = 101;

	// test column
	int statusColumn = 0;
	for (int i = 0; i < N; i++)
		if (height[i][locM] != smallest && height[i][locM] != 101)
			statusColumn = -1;
	if (statusColumn == 0)
		for (int i = 0; i < N; i++)
			height[i][locM] = 101;

	if (statusRow == -1 && statusColumn == -1)
		return -1;	//impossible
	else
		return 0;
}

int if_possible(vector<vector<int> > height, int N, int M)
{
	int smallest = 0;
	int locN, locM;

	smallest = minimum(height, N, M, locN, locM);
	while (smallest < 100)
	{
		if (reverse(height, N, M, smallest, locN, locM) == -1)
			return -1;
		smallest = minimum(height, N, M, locN, locM);
	}
	return 0;
}

int main(int argv, char* argc)
{
	ifstream infile("test.txt");
	ofstream outfile("result.txt");
	if (!infile || !outfile)
	{
		cout << "wrong" << endl;
		return -1;
	}

	int numCase;
	infile >> numCase;
	
	for (int i = 0; i < numCase; i++)
	{
		int N, M, temp;
		infile >> N >> M;
		vector<vector<int> > height;
		for (int j = 0; j < N; j++)
		{
			vector<int> line;
			for (int k = 0; k < M; k++)
			{
				infile >> temp;
				line.push_back(temp);
			}
			height.push_back(line);
		}

		int result = if_possible(height, N, M);
		outfile << "Case #" << i+1 << ": ";
		if (result == 0)
			outfile << "YES" << endl;
		else
			outfile << "NO" << endl;
	}

	infile.close();
	outfile.close();
}