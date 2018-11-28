#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	cin >> t;
	string s;
	int sm;
	for(int x = 1; x <= t; ++x)
	{
		cin >> sm >> s;
		int tmp = 0;
		int res = 0;
		for(int i = 0; i <= sm; ++i)
		{
			tmp += s[i] - '0';
			if(s[i+1] - '0' > 0)
			{
				if(tmp < i + 1)
				{
					res += (i + 1 - tmp);
					tmp = i + 1;
				}
			}
		}
		cout << "Case #" << x << ": " << res << endl;
	}
	return 0;
}