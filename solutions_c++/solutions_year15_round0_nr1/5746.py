#include<iostream>
#include<string>
#include<vector>
using namespace std;
#define _CRT_SECURE_NO_DEPRECATE
int main()
{
	int test, testcase;
	freopen("C://Users//Tanvir//Desktop//A-large.in", "r", stdin);
	freopen("C://Users//Tanvir//Desktop//out1.txt", "w", stdout);
	cin >> testcase;
	for (test = 1; test <= testcase; test++)
	{
		cout << "Case #" << test << ": ";
		int result = 0;
		int max;
		string s;

		cin >> max >> s;
		int i;
		vector<int> items;
		vector<int> cumSums;
		for (i = 0; i < s.length(); i++)
		{
			items.push_back(s[i] - '0');
		}
		int sum = 0;
		for (i = 0; i < s.length(); i++)
		{
			sum += items[i];
			cumSums.push_back(sum);
		}
		sum = 0;
		int diff = 0;
		int j = 0;
		for (i = 1; i < s.length(); i++)
		{
			if (i > cumSums[i - 1])
			{
				diff = i - cumSums[i - 1];
				for (j = i; j < s.length(); j++)
				{
					cumSums[j] += diff;
				}
				sum += diff;
			}
			else
				diff = 0;
		}
		cout << sum;
		cout << endl;
	}
	return 0;
}