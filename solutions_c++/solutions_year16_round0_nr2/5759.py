#include <iostream>
#include <string>
using namespace std;

int findNumber(string pancakes)
{
	int ret = 0;
	char cur = pancakes[0];
	for (auto pan : pancakes)
	{
		if (pan != cur)
		{
			ret++;
			cur = pan;
		}
	}
	
	if (cur == '-')
	{
		ret++;
	}

	return ret;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		string str;
		cin >> str;
		cout << "Case #" << t << ": " << findNumber(str) << endl;
	}
	return 0;
}