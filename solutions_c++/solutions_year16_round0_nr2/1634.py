#include <iostream>

using namespace std;

int main()
{
	int T;
	string s;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		cin >> s;
		int result = 0;

		int n = s.length();
		bool neg = true;
		for(int i = n - 1; i >= 0; i--)
		{
			if((neg && s[i] == '-') || (!neg && s[i] == '+'))
			{
				result++;
				neg = !neg;
			}
		}

		cout << "Case #" << t << ": " << result << endl;
	}


	return 0;
}