#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>

using namespace std;

int solve(string& str)
{
	int ans = 0;
	if (str[0] == '-')
		ans -= 1;
	bool is_seq = false;
	int count = 0;
	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] == '-')
		{
			if (!is_seq)
			{
				count++;
				is_seq = true;
			}
		}
		else
		{
			is_seq = false;
		}
	}
	return ans + 2 * count;
}

int main(void)
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	scanf("\n");
	for (int i = 0; i < T; i++)
	{
		string line;
		getline(cin, line);
		printf("Case #%d: %d\n", i + 1, solve(line));
	}
	return 0;
}