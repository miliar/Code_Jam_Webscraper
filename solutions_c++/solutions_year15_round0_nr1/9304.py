#include <string>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <limits>
#include <iostream>
#include <sstream>
#include <map>

using namespace std;




int main()
{ 
	int T;
	cin >> T;

	vector<string> str;

	for (int i = 1; i <= T; ++i)
	{
		int Smax;
		cin >> Smax;

		string s;
		cin >> s;

		int cnt = s[0] - '0';

		int ans = 0;

		for (int j = 1; j <= Smax; ++j)
			if (s[j] > '0')
			{
				auto t = max(0, j - cnt);
				ans += t;
				cnt += s[j] - '0' + t;
			}

		str.push_back(string("Case #") + to_string(i) + ": " + to_string(ans));
	}

	for (auto& s : str)
		cout << s << endl;

 	return 0;
} 