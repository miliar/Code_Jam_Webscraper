#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>
#define mp(x, y) make_pair(x, y)

using namespace std;

typedef long long ll;

int t, res, a[2000], pref[2000], n;
string s;

int main()
{
	freopen("/Users/user/Downloads/A-large.in", "r", stdin);
	freopen("key.out", "w", stdout);
	cin >> t;

	for(int q = 0; q < t; q++)
	{
		cin >> n >> s;
		n++;
		for(int i = 0; i < n; i++)
			a[i] = s[i] - '0';
		pref[0] = a[0];
		for(int i = 1; i < n; i++)
		{
			if(i > pref[i - 1] && a[i] != 0)
			{
				res += i - pref[i - 1];
				pref[i - 1] = i;
			}
			pref[i] = pref[i - 1] + a[i];
		}
		printf("Case #%d: %d\n", q + 1, res);
		res = 0;
	}
	
	return 0;
}
