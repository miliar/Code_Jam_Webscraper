//be naame khodaa

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
typedef long long ll;

using namespace std;
typedef pair <int, int> pii;

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++)
	{
		string s, res = "";
		cin >> s;
		for (int i = 0; i < s.length(); i++)
		{
			string s1 = s[i] + res, s2 = res + s[i];
			if (s1 > s2) res = s1;
			else res = s2;
		}
		cout << "Case #" << it << ": " << res << endl;
	}
	return 0;
}
