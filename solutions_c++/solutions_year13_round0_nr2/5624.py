#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int input[100][100];

bool CheckValid(int row, int col, int n, int m, int leastInMatrix);


int main()
{
	int T, n, m;

	int leastInMatrix;

	string output;

	ifstream fin;
	ofstream fout;

	fin.open("C:\\Users\\KishoreVen\\Downloads\\B-small-attempt0.in", ios::in);
	fin >> T;

	for(int test=0; test<T; test++)
	{
		fin >> n;
		fin >> m;
		output = "YES";

		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				fin >> input[i][j];
			}
		}

		leastInMatrix = input[0][0];
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				if(input[i][j] < leastInMatrix)
					leastInMatrix = input[i][j];
			}
		}

		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				if(input[i][j] == leastInMatrix)
				{
					if(!CheckValid(i, j, n, m, leastInMatrix))
					{
						output = "NO";
						break;
					}
				}
			}

			if(output == "NO")
			{
				break;
			}
		}

		fout.open ("output.out", ios::out | ios::app);
		fout<<"Case #"<<test+1<<": "<<output<<endl;
		fout.close();

	}

	fin.close();
	return 0;
}


bool CheckValid(int row, int col, int n, int m, int leastInMatrix)
{
	bool rowValid = true;
	bool colValid = true;
	
	for(int i=0; i<m; i++)
	{
		if(input[row][i] != leastInMatrix)
		{
			rowValid = false;
			break;
		}
	}

	if(rowValid == true)
	{
		return true;
	}

	for(int i=0; i<n; i++)
	{
		if(input[i][col] != leastInMatrix)
		{
			colValid = false;
			break;
		}
	}

	if(colValid == true)
		return true;
	
	return false;
}