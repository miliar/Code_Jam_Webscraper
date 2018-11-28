#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void GetOptionAndItems(int& option, vector<vector<int>>& items)
{
	cin >> option;
	for (int i = 0; i < 4; ++i)
	{
		vector<int> v;
		for (int j = 0; j < 4; j++)
		{
			int num;
			cin >> num;
			v.push_back(num);
		}
		items.push_back(v);
	}
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w+", stdout);
	int totalTestCases;
	cin >> totalTestCases;
	for (int testCase = 1; testCase <= totalTestCases; testCase++)
	{
		int option = 0;
		vector<vector<int>> items;
		GetOptionAndItems(option, items);
		vector<int>& try1 = items[option - 1];
		int option2 = 0;
		vector<vector<int>> items2;
		GetOptionAndItems(option2, items2);
		vector<int>& try2 = items2[option2 - 1];
		vector<int> common;
		for (vector<int>::iterator firstIt = try1.begin(); firstIt != try1.end(); ++firstIt)
		{
			for (vector<int>::iterator secondIt = try2.begin(); secondIt != try2.end(); ++secondIt)
			{
				if (*firstIt == *secondIt)
					common.push_back(*firstIt);
			}
		}
		cout << "Case #" << testCase << ": ";
		switch (common.size())
		{
		case 1:
			cout << *common.begin() << endl;
			break;
		case 0:
			cout << "Volunteer cheated!" << endl;
			break;
		default:
			cout << "Bad magician!" << endl;
			break;
		}
	}
	return 0;
}

