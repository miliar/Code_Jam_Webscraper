#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#define lol long long
using namespace std;

string filename = "A-large.in";
ifstream in(filename);
ofstream out(filename + "_out.txt");

#define cin in
#define cout out

void result(char v0, char v1, char v2, int x, vector<int> & a)
{
	string s;
	for (int i = x; i < 2 * x; ++i)
	{
		if (a[i] == 0)
			s += v0;
		if (a[i] == 1)
			s += v1;
		if (a[i] == 2)
			s += v2;
	}
	for (int i = 1; i < x; i *= 2)
	{
		for (int j = 0; j < s.length(); j += 2 * i)
		{
			if (s.substr(j, i) > s.substr(j + i, i))
				for (int k = j; k < j + i; ++k)
					swap(s[k], s[k + i]);
		}
	}
	cout << s;
	cout << endl;
}

int main()
{
	//ios_base::sync_with_stdio(0);
	//cin.tie(0);
	int t;
	cin >> t;
		vector<int> a(4096 * 4);
	a[1] = 0;
	for (int i = 1; i < 4096 * 2; ++i)
	{
		int f = a[i];
		int s = (a[i] + 2) % 3;
		a[2 * i] = f;
		a[2 * i + 1] = s;
	}

	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		int n, r, p, s;
		cin >> n >> r >> p >> s;

		int x = 1;
		for (int i = 0; i < n; ++i)
			x *= 2;
		vector<int> cnt(3, 0);
		for (int j = x; j < 2 * x; ++j)
			++cnt[a[j]];

		if (r == cnt[0] && p == cnt[1] && s == cnt[2])
		{
			result('R', 'P', 'S', x, a);
			continue;
		}
		if (p == cnt[0] && s == cnt[1] && r == cnt[2])
		{
			result('P', 'S', 'R', x, a);
			continue;
		}
		if (s == cnt[0] && r == cnt[1] && p == cnt[2])
		{
			result('S', 'R', 'P', x, a);
			continue;
		}
		cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
