#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

bool valid(int **a, int N, int M)
{
	bool row, col;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			row = true;
			col = true;
			if (a[i][j] == 1)
			{
				for (int k = 0; k < M; k++)
				{
					if(a[i][k] != a[i][j])
					{
						row = false;
						break;
					}
				}
				
				for (int k = 0; k < N; k++)
				{
					if(a[k][j] != a[i][j])
					{
						col = false;
						break;
					}
				}
			}
			if (!row && !col)
				return false;
		}
	}
	
	return true;
}

int main(int argc, char **argv)
{
	if (argc != 3)
	{
		cout << "Invalid number of arguments" << endl;
		return 0;
	}
	
	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);
	
	string in;
	int T, N, M;
	int **a;
	
	if (infile.is_open())
	{
		infile >> in;
		T = atoi(in.c_str());
		
		for (int k = 1; k <= T; k++)
		{
			infile >> in;
			N = atoi(in.c_str());
			infile >> in;
			M = atoi(in.c_str());
			a = new int*[N];
			for (int i = 0; i < N; i++)
				a[i] = new int[M];
			
			for (int i = 0; i < N; i++)
			{
				for (int j = 0; j < M; j++)
				{
					infile >> in;
					a[i][j] = atoi(in.c_str());
				}
			}
			
			bool is_valid = valid(a, N, M);
			outfile << "Case #" << k << ": ";
			if (is_valid)
				outfile << "YES" << endl;
			else outfile << "NO" << endl;
		}
		
		for (int i = 0; i < N; i++)
			delete [] a[i];
		delete [] a;
		infile.close();
		outfile.close();
	}
	else cout << "Unable to open file" << endl;
	
	return 0;
}
