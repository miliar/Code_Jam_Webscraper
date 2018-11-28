#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++)
	{
		string s;
		cin >> s;
		s += '+';

		int ret = 0;
		for(int i = 1; i < s.length(); i++)
		{
			if(s[i] != s[i-1])
				ret++;
		}

		cout << "Case #" << i << ": " << ret << endl;
	}

	return 0;
}
