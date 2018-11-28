#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

//ifstream fin("input.in");
//ofstream fout("output.out");

int solve (string str)
{
	int answer = 0;
	if (str.length() == 1)
		str[0] == '-' ? answer++ : answer;
	else if (str.length() == 2)
	{
		if (str[0] == '-' && (str[1] == '+' || str[1] == '-')) answer++;
		else if (str[0] == '+' && str[1] == '-') answer += 2;
	}
	else
	{
		auto i = str.end() - 1;
		for (i; i != str.begin() - 1; i--)
		{
			if (*i == '-')
			{
				if (*str.begin() == '+')
				{
					for (auto j = str.begin(); *j == '+'; j++)
						*j = '-';
					answer++;
				}

				answer++;
				reverse(str.begin(), i + 1);
				for (auto j = str.begin(); j != i + 1; ++j)
					*j = *j == '-' ? '+' : '-';
 			}
		}
		if (str[0] == '-' && (str[1] == '+' || str[1] == '-')) answer++;
		else if (str[0] == '+' && str[1] == '-') answer += 2;
	}
	return answer;
}
int main()
{
	int n = 0;
	cin >> n;
	string str = "";
	for (int i = 0; i < n; ++i)
	{
		cin >> str;
		cout << "Case #" << i + 1 << ": " << solve(str) << '\n';
	}
	return 0;
}