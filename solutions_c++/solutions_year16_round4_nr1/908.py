#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<time.h>
using namespace std;

int n, r, p, s;

bool ok(string str)
{
	int rr = 0, pp = 0, ss = 0;
	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] == 'P') pp++;
		if (str[i] == 'R') rr++;
		if (str[i] == 'S') ss++;
	}

	if (pp != p || ss != s || rr != r)
		return false;
	return true;
}

string gen(string str, int len)
{
	if (len == 0)
		return str;

	string t = "";
	for (int i = 0; i < str.size(); i++)
	{
		string l, r;
		r = str[i];
		if (str[i] == 'P') 
		{
			l = "R";
		}
		if (str[i] == 'R')
		{
			l = "S";
		}
		if (str[i] == 'S')
		{
			l = "P";
		}

		l = gen(l, len - 1);
		r = gen(r, len - 1);

		t += min(l, r);
		t += max(l, r);
	}

	return t;
}

void solve()
{
	cin >> n >> r >> p >> s;

	string c[] = { "R", "S", "P" };

	string ans = "";
	for (int win = 0; win < 3; win++)
	{
		string s0 = c[win];
		string res = gen(s0, n);

		if ((ans == "" || ans > res) && ok(res))
			ans = res;
	}

	if (ans == "")
		ans = "IMPOSSIBLE";
	cout << ans;
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}