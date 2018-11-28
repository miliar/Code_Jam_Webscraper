#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	scanf("\n");

	map<char, pair<string, int>> odd_digits = {
		{ 'Z', pair<string, int>("ZERO", 0) },
		{ 'W', pair<string, int>("TWO", 2) },
		{ 'U', pair<string, int>("FOUR", 4) },
		{ 'X', pair<string, int>("SIX", 6) },
		{ 'G', pair<string, int>("EIGHT", 8) }
	};

	map<char, pair<string, int>> even_digits = {
		{ 'O', pair<string, int>("ONE", 1) },
		{ 'H', pair<string, int>("THREE", 3) },
		{ 'V', pair<string, int>("FIVE", 5) },
		{ 'S', pair<string, int>("SEVEN", 7) }
	};

	for (int i = 0; i < T; ++i)
	{
		string line;
		vector<int>freq(256, 0);
		getline(cin, line);
		for (auto it = line.begin(); it != line.end(); ++it)
			freq[*it]++;

		vector<int> ans;

		for (auto odd_it = odd_digits.begin(); odd_it != odd_digits.end(); ++odd_it)
		{
			while (freq[odd_it->first] != 0)
			{
				for (auto k = odd_it->second.first.begin(); k != odd_it->second.first.end(); ++k)
					freq[*k]--;

				ans.push_back(odd_it->second.second);
			}
		}

		for (auto even_it = even_digits.begin(); even_it != even_digits.end(); ++even_it)
		{
			while (freq[even_it->first] != 0)
			{
				for (auto k = even_it->second.first.begin(); k != even_it->second.first.end(); ++k)
					freq[*k]--;

				ans.push_back(even_it->second.second);
			}
		}

		while (freq['E']-- != 0)
		{
			ans.push_back(9);

		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << i + 1 << ": ";
		for (auto it = ans.begin(); it != ans.end(); ++it)
			cout << *it;
		cout << "\n";
	}
	return 0;
}