#include <iostream>
#include <string>
#include<vector>
#include<unordered_set>
using namespace std;

void run();

int main()
{
	long T;
	cin >> T;

	for (int c = 1; c <= T; ++c)
	{
		cout << "Case #" << c << ": ";
		run();
	}
}

void run()
{
	long N;
	cin >> N;
	int value;

	vector<vector<int>> rows;

	// Read in
	for (int i = 0; i < (2 * N - 1); ++i)
	{
		vector<int> row;
		for (int j = 0; j < N; ++j)
		{
			cin >> value;
			row.push_back(value);
		}
		rows.push_back(row);
	}

	// Group into pairs
	int missingRowIdx = -1;
	vector<vector<int>> pairIndexes;
	unordered_set<int> used;
	for (int i = 0; i < N; ++i)
	{
		int min = 2501;
		vector<int> indexes;
		for (int j = 0; j < rows.size(); ++j)
		{
			if (used.count(j) != 0)
				continue;

			if (rows[j][i] < min)
			{
				indexes.clear();
				indexes.push_back(j);
				min = rows[j][i];
			}
			else if (rows[j][i] == min)
			{
				indexes.push_back(j);
			}
		}

		if (indexes.size() == 1)
			missingRowIdx = i;

		for (auto idx : indexes)
			used.insert(idx);

		pairIndexes.push_back(indexes);
	}

	
	vector<int> missingRow = rows[pairIndexes[missingRowIdx][0]];

	for (int i = 0; i < N; ++i)
	{
		if (i == missingRowIdx)
			continue;

		vector<int> row = rows[pairIndexes[i][0]];
		if (row[missingRowIdx] == missingRow[i])
			pairIndexes[i].erase(pairIndexes[i].begin());
	}

	for (int i = 0; i < N; ++i)
		cout << rows[pairIndexes[i][0]][missingRowIdx] << " ";

	cout << endl;
}