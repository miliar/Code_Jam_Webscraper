
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		string s;
		cin >> s;

		int alternateNum = 0;
		char lastChar = 0;
		for (unsigned int j = 0; j < s.length(); ++j)
		{
			if (lastChar != s[j])
			{
				lastChar = s[j];
				++alternateNum;
			}
		}

		if (lastChar == '+')
		{
			--alternateNum;
		}

		cout << "Case #" << i << ": " << alternateNum << endl;
	}

	return 0;
}
