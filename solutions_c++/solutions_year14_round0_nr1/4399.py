#include <iostream>
#include <fstream>
using namespace std;

int answer;

int numAnswers(int arr1[], int arr2[])
{
	int num = 0;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (arr1[i] == arr2[j])
			{
				num++;
				answer = arr1[i];
			}
		}
	}
	return num;
}

int main()
{
	ofstream fout("out.out", ios::out);
	ifstream fin("A-small-attempt0.in");
	int numTests; fin >> numTests;

	for (int i = 0; i < numTests; i++)
	{
		int arr1[4], arr2[4];
		int row1, row2;

		fin >> row1;
		for (int j = 0; j < 4; j++)
		{
			if (row1 == j + 1)
			{
				for (int k = 0; k < 4; k++)
				{
					fin >> arr1[k];
				}
			}
			else
			{
				for (int k = 0; k < 4; k++)
				{
					int x;
					fin >> x;
				}
			}
		}
		fin >> row2;
		for (int j = 0; j < 4; j++)
		{
			if (row2 == j + 1)
			{
				for (int k = 0; k < 4; k++)
				{
					fin >> arr2[k];
				}
			}
			else
			{
				for (int k = 0; k < 4; k++)
				{
					int x; fin >> x;
				}
			}
		}

		if (numAnswers(arr1, arr2) == 0)
			fout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		else if (numAnswers(arr1, arr2) > 1)
			fout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
		else
			fout << "Case #" << i + 1 << ": " << answer << endl;

	}

	return 0;
}