// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
string nums[] = { "ZERO", "TWO", "FOUR", "SIX", "EIGHT", "SEVEN", "THREE", "FIVE", "ONE", "NINE"};
string numss[] = { "0", "2", "4", "6", "8", "7", "3", "5", "1", "9" };
int numsss[] = { 0, 8, 1, 6, 2, 7, 3, 5, 4, 9 };

string compute(string s)
{
	string result = "";
	int* let = new int[26];
	int* numbers = new int[10];
	for (int k = 0; k < 26; k++)
		let[k] = 0;
	for (int k = 0; k < 10; k++)
		numbers[k] = 0;
	for (unsigned int k = 0; k < s.length(); k++)
	{
		let[(s[k] - 'A')]++;
	}
	for (int k = 0; k < 10; k++)
	{
		int* mylet = new int[26];
		for (unsigned int j = 0; j < nums[k].length(); j++)
		{
			mylet[nums[k].at(j) - 'A'] = let[nums[k].at(j) - 'A'];
		}

		int min = mylet[nums[k].at(0) - 'A'];
		for (unsigned int j = 0; j < nums[k].length(); j++)
		{
			int m = mylet[nums[k].at(j) - 'A'];
			mylet[nums[k].at(j) - 'A']--;
			if (m < min)
				min = m;
		}
		if (min > 0)
		{
			numbers[k] += min;
			for (unsigned int j = 0; j < nums[k].length(); j++)
			{
				let[nums[k].at(j) - 'A'] -= min;
			}
		}
	}
	for (int k = 0; k < 10; k++)
	{
		for (int j = 0; j < numbers[numsss[k]]; j++)
			result.append(numss[numsss[k]]);
	}
	return result;
}

int main()
{
	ifstream input("input.in");
	if (input.is_open())
	{
		int T;
		ofstream output("output.out");
		input >> T;
		for (int i = 1; i <= T; i++)
		{
			string S;
			input >> S;
			string y = compute(S);
			output << "Case #" << i << ": " << y << endl;
		}
		input.close();
		output.close();
	}
	return 0;
}