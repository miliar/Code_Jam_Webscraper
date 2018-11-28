#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("Result1");
	int T;
	in >> T;
	int row1,row2;
	for (int k = 0; k < T; k++)
	{
		in >> row1;
		int temp;
		vector<vector<int>> matrix1(4, vector<int>(4)), matrix2(4, vector<int>(4));
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> temp;
				matrix1[i][j] = temp;
			}
		}
		in >> row2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> temp;
				matrix2[i][j] = temp;
			}
		}
		int count = 0, num;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (matrix1[row1-1][i] == matrix2[row2-1][j])
				{
					count++;
					num = matrix1[row1-1][i];
				}
			}
		}
		out << "Case #" << k + 1 << ": ";
		if (count == 0)
		{
			out << "Volunteer cheated!" << endl;
		}
		else if (count == 1)
		{
			out << num << endl;
		}
		else
		{
			out << "Bad magician!" << endl;
		}
	}
	out.close();
	system("PAUSE");
	return 0;
}