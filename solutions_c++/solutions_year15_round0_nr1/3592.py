#include <iostream>
#include <cstdio>

#include <cmath>
#include <algorithm>

#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;
typedef long long ll;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int testcases = 1; testcases <= t; ++testcases)
	{
		ll res = 0;
		int sm = 0;
		cin >> sm;
		vector <int> v(sm+1);
		string s;
		cin >> s;
		for (int i = 0; i < s.size(); ++i)
		{
			v[i] = s[i] - '0';
		}
		int cur = v[0];
		for (int i = 1; i < v.size(); ++i)
		{
			if (cur < i)
			{
				res += i - cur;
				cur = i;
			}
			cur += v[i];
		}
		cout << "Case #" << testcases << ": " << res<<endl;
	}
	return 0;
}