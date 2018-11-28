#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

void Open()
{
	freopen("P1.in", "r", stdin);
	freopen("P1.out", "w", stdout);
}

void Close()
{
	fclose(stdin);
	fclose(stdout);
}

void Run(int casenum)
{
	vector<int> row1, row2;
	int R1, R2, tmp;
	cin >> R1;
	row1.resize(4);
	for (int i = 0; i < 4; i++)
	{
		if (i == R1 - 1)
			for (int j = 0; j < 4; j++)
				cin >> row1[j];
		else
			for (int j = 0; j < 4; j++)
				cin >> tmp;
	}

	cin >> R2;
	row2.resize(4);
	for (int i = 0; i < 4; i++)
	{
		if (i == R2 - 1)
			for (int j = 0; j < 4; j++)
				cin >> row2[j];
		else
			for (int j = 0; j < 4; j++)
				cin >> tmp;
	}

	int count = 0;
	int num;
	for (int i = 0; i < row1.size(); i++)
		for (int j = 0; j < row2.size(); j++)
		{
			if (row1[i] == row2[j]) 
			{
				count++;
				num = row1[i];
			}
		}
	cout << "Case #" << casenum << ": ";
	if (count == 1)
		cout << num << endl;
	else
		if (count == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;

}

void Process()
{
	int casenum;
	cin >> casenum;
	for (int i = 1; i <= casenum; i++)
		Run(i);
}

int main()
{
	Open();
	Process();
	Close();
	return 0;
}