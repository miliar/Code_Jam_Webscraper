
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <limits>
using namespace std;


void testCase()
{
	int n;
	cin >> n;

	vector<vector<pair<char, int>>> data(n);

	for (int i = 0; i < n; i++)
	{
		string input;
		cin >> input;
		char last = 0;
		int count = 0;
		for (int j = 0; j < input.length(); j++)
		{
			if (last != input[j])
			{
				if (last)
				{
					data[i].push_back(make_pair(last, count));
				}
				last = input[j];
				count = 0;
			}
			count++;
		}
		data[i].push_back(make_pair(last, count));

		if (i > 0)
		{
			if (data[0].size() != data[i].size())
			{
				printf("Fegla Won");
				return;
			}
			for (int j = 0; j < data[0].size(); j++)
			{
				if (data[0][j].first != data[i][j].first)
				{
					printf("Fegla Won");
					return;
				}
			}
		}
	}

	int answer = 0;

	for (int digit = 0; digit < data[0].size(); digit++)
	{
		int digitMin = numeric_limits<int>::max();

		for (int target = 0; target < n; target++)
		{
			int current = 0;
			for (int source = 0; source < n; source++)
			{
				current += abs(data[target][digit].second - data[source][digit].second);
			}
			digitMin = min(digitMin, current);
		}
		answer += digitMin;
	}

	printf("%d", answer);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("ouptut.txt", "wt", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		testCase();
		printf("\n");
	}

	return 0;
}
