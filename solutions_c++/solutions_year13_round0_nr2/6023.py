#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int input[10][10];

bool CheckValid(int row, int col, int n, int m)
{
	int flagRow = 1, flagCol = 1;
	//Check row
	for(int i=0; i<m; i++)
	{
		if(input[row][i] != 1)
		{
			flagRow = 0;
			break;
		}
	}

	//Check col
	for(int i=0; i<n; i++)
	{
		if(input[i][col] != 1)
		{
			flagCol = 0;
			break;
		}
	}

	if(flagRow || flagCol)
		return true;
	else
		return false;
}

int main()
{
	int T, n, m;
	string output;
	ifstream inFile;
	ofstream oFile;
	inFile.open("input.txt");
	inFile >> T;

	for(int test=0; test<T; test++)
	{
		inFile >> n;
		inFile >> m;
		output = "YES";

		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				inFile >> input[i][j];
			}
		}
		
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				if(input[i][j] == 1)
					if(!CheckValid(i, j, n, m))
					{
						output = "NO";
						goto OUT;
					}
			}
		}

OUT:
		oFile.open ("output.txt", ios::out | ios::app);
		oFile<<"Case #"<<test+1<<": "<<output<<endl;
		oFile.close();

	}
	inFile.close();
	return 0;
}
