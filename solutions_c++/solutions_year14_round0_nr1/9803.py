#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

typedef long long dlong;

string solve(int firstAnswer, vector<vector<int>> &firstCards, int secondAnswer, vector<vector<int>> &secondCards)
{
	ostringstream os;
	firstAnswer -= 1;
	secondAnswer -= 1;
	int counter = 0;
	int solution = 0;
	for (int i = 0; i < firstCards[0].size(); i++)
	{
		vector<int>::iterator it = find(secondCards[secondAnswer].begin(), secondCards[secondAnswer].end(), firstCards[firstAnswer][i]);
		if (it != secondCards[secondAnswer].end())
		{
			solution = *it;
			counter++;
		}
	}
	if (counter == 1)
	{
		os << solution;
		return os.str();
	}
	else if (counter == 0)
	{
		return "Volunteer cheated!";
	}
	else
	{
		return "Bad magician!";
	}

}

int main()
{
	int T;
	cin >> T;
	int row = 4;
	int column = 4;
	vector<vector<int>> firstCards(row, vector<int>(column));
	vector<vector<int>> secondCards(row, vector<int>(column));
	for (int i = 1; i <= T; i++)
	{
		int firstAnswer;
		cin >> firstAnswer;
		for (int j = 0; j < firstCards.size(); j++)
		{
			for (int k = 0; k < firstCards.size(); k++)
			{
				cin >> firstCards[j][k];
			}
		}
		int secondAnswer;
		cin >> secondAnswer;
		for (int j = 0; j < secondCards.size(); j++)
		{
			for (int k = 0; k < secondCards.size(); k++)
			{
				cin >> secondCards[j][k];
			}
		}
		cout << "Case #" << i << ": " << solve(firstAnswer, firstCards, secondAnswer, secondCards) << endl;
	}
}