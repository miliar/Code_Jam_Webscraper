#include <iostream>
#include <vector>
#include <string>
using namespace std;

int calc(string s)
{
	int ret = 0;
	bool plus = false;
	bool state = false;

	for (int i = 0; i < s.length(); ++i)
	{
		// transition from - to + or first character is +
		if (s[i] == '+' && state == false)
		{
			if (i != 0)
				ret += plus ? 2 : 1;

			state = true;
			plus = true;
		}

		if (s[i] == '-') state = false;
	}

	if (state == false)
	{
		ret += plus ? 2 : 1;
	}

	return ret;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i)
	{
		string S;
		cin >> S;

		int n = calc(S);

		cout << "Case #" << i << ": " << n << endl;
	}
}