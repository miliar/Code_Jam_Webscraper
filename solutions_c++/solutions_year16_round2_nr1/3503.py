#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <stdint.h>
#include <stdio.h>
#include <iostream>
#include <utility>
#include <vector>
#include <string>
#include <string.h>

using namespace std;

bool is_empty_histogram
	(const int histogram[])
{
	for(int i = 0; i < 26; i++)
		if(histogram[i])
			return false;

	return true;
}

bool recurse
	(string& tele_no, // Always start from 0
	 const int digit_histogram[10][26],
	 int string_histogram[26])
{
	if(is_empty_histogram(string_histogram))
		return true;

	for(char i = tele_no[tele_no.size() - 1]; i <= '9'; i++)
	{
		bool is_valid = true;

		for(int j = 0; j < 26; j++)
			if(string_histogram[j] < digit_histogram[i - '0'][j])
			{
				is_valid = false;
				break;
			}

		if(is_valid)
		{
			for(int j = 0; j < 26; j++)
				string_histogram[j] -= digit_histogram[i - '0'][j];

			tele_no.push_back(i);

			if(recurse(tele_no, digit_histogram, string_histogram))
				return true;

			tele_no.resize(tele_no.size() - 1);

			for(int j = 0; j < 26; j++)
				string_histogram[j] += digit_histogram[i - '0'][j];
		}
	}

	return false;
}

int main()
{
	int T;

	cin >> T;

	char *digit_spell[] =
		{
			"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE",
		};

	int digit_histogram[10][26];

	memset(digit_histogram[0], 0, sizeof(digit_histogram));

	for(int i = 0; i < 10; i++)
		for(int j = 0; digit_spell[i][j]; j++)
			digit_histogram[i][digit_spell[i][j] - 'A']++;

	for(int test_index = 1; test_index <= T; test_index++)
	{
		string s;

		cin >> s;

		int string_histogram[26];

		memset(string_histogram, 0, sizeof(string_histogram));

		for(int i = 0; i < s.size(); i++)
			string_histogram[s[i] - 'A']++;

		string tele_no;

		tele_no.push_back('0');

		recurse
			(tele_no, // Always start from 0
			 digit_histogram,
			 string_histogram);

		cout << "Case #" << test_index << ": " << tele_no.substr(1) << endl;
	}

	return 0;
}
