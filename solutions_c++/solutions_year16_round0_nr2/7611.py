#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <list>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
#include <cstring>
#include <tuple>
#include <cassert>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		string s;
		cin >> s;

		int ans = (s.back() == '-');
		for(int i = 1; i < s.size(); i++)
		{
			if(s[i] != s[i - 1]) ans++;
		}
		cout << "Case #" << t << ": " << ans << '\n';
	}

	return 0;
}