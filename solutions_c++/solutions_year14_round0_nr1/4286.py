#include<climits>
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

void magic(int row1, vector<vector<int>> &mat1, int row2, vector<vector<int>> &mat2)
{
	int match = 0;
	int index = 0;
	
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (mat1[row1][i] == mat2[row2][j])
			{
				index = mat1[row1][i];
				match++;
			}
		}
			
	}
	if (match == 0)
	{
		cout << "Volunteer cheated!" << endl;
		return;
	}
	else if (match > 1)
	{
		cout << "Bad magician!" << endl;
		return;
	}
	else
	{
		cout << index << endl;
	}
}


int main()
{
	int T = 0;

	cin >> T;
	vector<vector<int>> mat1(4, vector<int>(4, 0));
	vector<vector<int>> mat2(4, vector<int>(4, 0));
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		int row1 = 0;
		cin >> row1;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int temp = 0;
				cin >> temp;
				mat1[i][j] = temp;
			}
		}

		int row2 =0;
		cin >> row2;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int temp = 0;
				cin >> temp;
				mat2[i][j] = temp;
			}
		}


		magic(row1 -1, mat1, row2 -1, mat2);
	}
}