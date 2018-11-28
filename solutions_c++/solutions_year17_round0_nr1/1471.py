/*
Hanit Banga
*/

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define fast_cin() ios_base::sync_with_stdio(false)

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int N = 1e5 + 5;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		string s; int k;
		cin >> s >> k;
		int n = s.length(), ans = 0;
		for (int i = 0; i < n - k + 1; ++i)
		{
			if (s[i] == '-')
			{
				++ans;
				for (int j = i; j < i + k; ++j)
					s[j] = '+' + '-' - s[j];
			}
		}

		bool f = true;
		for (int i = n - k + 1; i < n; ++i)
		{
			if (s[i] == '-')
			{
				f = false;
				break;
			}
		}

		if (f)
			cout << ans << '\n';
		else
			cout << "IMPOSSIBLE\n";
	}
}