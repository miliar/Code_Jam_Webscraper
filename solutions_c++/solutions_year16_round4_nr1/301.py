#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <map>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> tll;

// globals starts here

int n, R, P, S;
map<char, string> moves;

string dp[20][256];

string f(int n, char c)
{
	if (!dp[n][c].empty())
	{
		return dp[n][c];
	}

	char c1 = moves[c][0];
	char c2 = moves[c][1];

	string s1 = f(n - 1, c1);
	string s2 = f(n - 1, c2);

	if (s1 < s2)
	{
		return dp[n][c] = s1 + s2;
	}
	else
	{
		return dp[n][c] = s2 + s1;
	}
}

bool check(const string& s)
{
	map<char, int> freq;

	for (int i = 0; i < s.size(); ++i)
	{
		freq[s[i]]++;
	}

	return freq['S'] == S && freq['P'] == P && freq['R'] == R;
}

string solve()
{
	vector<string> good;

	string s = f(n, 'P');
	if (check(s))
	{
		good.push_back(s);
	}

	s = f(n, 'S');
	if (check(s))
	{
		good.push_back(s);
	}

	s = f(n, 'R');
	if (check(s))
	{
		good.push_back(s);
	}

	if (good.empty())
	{
		return "IMPOSSIBLE";
	}
	
	return *min_element(good.begin(), good.end());
}

char winner(char c1, char c2)
{
	if (c1 == 'P')
	{
		if (c2 == 'R')
		{
			return 'P';
		}
		else if (c2 == 'S')
		{
			return 'S';
		}
	}

	if (c1 == 'S')
	{
		if (c2 == 'P')
		{
			return 'S';
		}
		else if (c2 == 'R')
		{
			return 'R';
		}
	}

	if (c1 == 'R')
	{
		if (c2 == 'P')
		{
			return 'P';
		}
		else if (c2 == 'S')
		{
			return 'R';
		}
	}

	assert(false);
}

bool checkok(const string& s)
{
	string act = s;
	for (int i = 0; i < n; ++i)
	{
		string next;
		for (int j = 0; j < act.size(); j += 2)
		{
			char c1 = act[j];
			char c2 = act[j + 1];

			if (c1 == c2)
			{
				return false;
			}

			next.push_back(winner(c1, c2));
		}
		act = next;
	}

	return true;
}

string solvestupid()
{
	string s;
	for (int i = 0; i < R; ++i)
	{
		s.push_back('R');
	}
	for (int i = 0; i < S; ++i)
	{
		s.push_back('S');
	}
	for (int i = 0; i < P; ++i)
	{
		s.push_back('P');
	}

	string best;
	for (int i = 0; i < (1 << n); ++i)
	{
		best.push_back('Z');
	}

	vector<int> nums;
	for (int i = 0; i < (1 << n); ++i)
	{
		nums.push_back(i);
	}

	do
	{
		string tocheck;
		for (int i = 0; i < (1 << n); ++i)
		{
			tocheck.push_back(s[nums[i]]);
		}

		if (checkok(tocheck))
		{
			best = min(best, tocheck);
		}
	} while (next_permutation(nums.begin(), nums.end()));

	if (best[0] == 'Z')
	{
		return "IMPOSSIBLE";
	}

	return best;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tests;
	cin >> tests;

	moves['P'] = "PR";
	moves['S'] = "SP";
	moves['R'] = "SR";

	dp[0]['P'] = "P";
	dp[0]['R'] = "R";
	dp[0]['S'] = "S";

	for (int tc = 1; tc <= tests; ++tc)
	{
		cin >> n >> R >> P >> S;

		cout << "Case #" << tc << ": ";
		//string ans = solvestupid();
		string ans2 = solve();

		/*if (ans != ans2)
		{
			cout << "FAIL" << endl;
			cout << ans << endl << ans2 << endl;
			return 0;
		}*/

		cout << ans2 << endl;
	}

	return 0;
}