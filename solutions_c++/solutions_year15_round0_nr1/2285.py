#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int solve(string &str)
{
	assert (str.length() > 0);
	int count = 0, friends = 0;

	for (int i = 0; i < str.length(); i++)
	{
		if (count < i)
		{
			count++;
			friends++;
		}

		assert (count >= i);
		count += str[i] - '0';
	}

	return friends;
}

int main()
{
	freopen("A-input.txt", "r", stdin);
	freopen("A-output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int testCase = 1; testCase <= T; testCase++)
	{
		string s;
		int smax;
		cin >> smax >> s;
		assert (s.length() == smax + 1);

		int friends = solve(s);
		cout << "Case #" << testCase << ": " << friends << endl;
	}

	return 0;
}
