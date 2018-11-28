#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int test = 0; test < T; ++test)
	{
		long long up = 0;
		long long result = 0;
		int n;
		string s;
		cin >> n >> s;
		for (int i = 0; i < s.size(); ++i)
		{
			int needed = 0;
			if(s[i] > '0' && up < i) needed = i - up;
			result += needed;
			up += needed + (s[i] - '0');
		}
		cout << "Case #" << test+1 << ": " << result << endl;
	}
	return 0;
}