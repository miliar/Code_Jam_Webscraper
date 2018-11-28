#include <algorithm>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

bool good(const string &s)
{
	return count(s.begin(), s.end(), '+') == (int)s.size();
}

int main()
{
	int t;
	cin >> t;
	for(int q = 1; q <= t; ++q)
	{
		string s;
		cin >> s;

		int cnt = 0;
		for(int i = 0; i < (int)s.size() - 1; ++i)
		{
			if(s[i] != s[i+1])
				++cnt;
		}

		cnt += int(s[s.size()-1] == '-');
		cout << "Case #" << q << ": " << cnt << endl;
	}
	return 0;
}