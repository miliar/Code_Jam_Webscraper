#include<cstdio>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
//first longer
int result(string first, string second)
{
	int number = 0;
	int j = 0;
	bool allCompared = false;
	while (allCompared == false)
	{
		if (j == first.length() && j == second.length())
		{
			allCompared = true;
			break;
		}
		if (first[j] != second[j])
		{
			if (j > 0)
			{
				if (first[j] == first[j - 1])
				{
					char helper = second[j - 1];
					second.insert(j, 1, helper);
					++number;
				}
				else if (second[j] == second[j - 1])
				{
					char helper = first[j - 1];
					first.insert(j, 1, helper);
					++number;
				}
				if (first[j] != second[j])
				{
					return -1;
				}
				else
					++j;
			}
			else
				return -1;
		}
		else
			++j;

	}
	
	return number;
}
int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int m;
		scanf("%d", &m);
		// assume m == 2	
		string first, second;
		cin >> first;
		cin >> second;
		int lenFirst = first.length();
		int lenSec = second.length();
		int res = 0;
		if (lenFirst > lenSec)
			res = result(first, second);
		else
			res = result(second, first);
		if (res != -1)
			printf("Case #%d: %d\n", i + 1, res);
		else
			printf("Case #%d: Fegla Won\n", i + 1);
	}
	return 0;
}