#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

vector<int> digits = { 0, 2, 4, 6, 8, 1, 3, 5, 7, 9 };
vector<string> literal_digits = { "ZERO", "TWO", "FOUR", "SIX", "EIGHT", "ONE", "THREE", "FIVE", "SEVEN", "NINE"} ;

bool remove_digit(const string& digit, vector<int>& character_occurences)
{
	for (const auto c : digit)
	{
		if (character_occurences[c - 'A'] == 0)
		{
			return false;
		}
	}

	for (const auto c : digit)
	{
		--character_occurences[c - 'A'];
	}

	return true;
}

void main()
{
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": ";

		string S;
		cin >> S;

		vector<int> character_occurences(26, 0);
		for (const auto s : S)
		{
			++character_occurences[s - 'A'];
		}

		vector<int> number;
		for (int i = 0; i < 10; ++i)
		{
			while (remove_digit(literal_digits[i], character_occurences))
			{
				number.push_back(digits[i]);
			}
		}

		sort(number.begin(), number.end());

		for (const auto n : number)
		{
			cout << n;
		}

		cout << endl;
	}
}
