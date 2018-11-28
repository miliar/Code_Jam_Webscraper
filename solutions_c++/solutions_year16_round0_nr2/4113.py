#include <iostream>
#include <string>
using namespace std;

typedef long long ll;


int main(void)
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T = 0;
	cin >> T;
	ll Answer = 0;
	string s;

	for (int i = 0; i < T; ++i)
	{
		cin >> s;
		int len = s.length();
		if (len)
		{
			int flipCnt = 0;
			char curChar = s.at(0);
			for (int j = 1; j < len; ++j)
			{
				if (curChar != s.at(j))
				{
					curChar = s.at(j);
					flipCnt++;
				}
			}
			if (curChar == '-')
			{
				flipCnt++;
			}
			Answer = flipCnt;
		}

		cout << "Case #" << i + 1 << ": " << Answer << endl;
	}
	return 0;
}
