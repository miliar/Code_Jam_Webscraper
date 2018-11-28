#include <iostream>
#include <vector>
#include <set>

using namespace std;

void doit(int casenum)
{
	cout << "Case #" << casenum << ": ";
	int r1, r2, dummy;
	vector<int> row1(4), row2(4);
	cin >> r1;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (r1 - 1 == i) cin >> row1[j];
			else cin >> dummy;
		}
	}

	cin >> r2;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (r2 - 1 == i) cin >> row2[j];
			else cin >> dummy;
		}
	}

	vector<int> answers;
	for (int i = 0; i < 4; ++i)
	{
		bool found = false;
		for (int j = 0; !found && j < 4; ++j)
		{
			found = (row1[i] == row2[j]);
		}
		if (found) answers.push_back(row1[i]);
	}

	switch (answers.size()) {
	case 1:
		cout << answers[0];
		break;
	case 0:
		cout << "Volunteer cheated!";
		break;
	default:
		cout << "Bad magician!";
		break;
	}
	cout << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) doit(i);
	return 0;
}