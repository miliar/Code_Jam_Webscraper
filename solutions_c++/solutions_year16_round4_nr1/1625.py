#include <iostream>
#include <string>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <iterator>
#include <functional>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

bool good(char & a, char & b)
{
	if (a == b) return false;
	if (a == 'S' && b == 'R')swap(a, b);
	if (a == 'P' && b == 'S')swap(a, b);
	if (a == 'R' && b == 'P')swap(a, b);
	return true;
}

bool correct(const vector<char>& a)
{
	vector<char> b = a;
	vector<char> c;

	while (b.size() > 1)
	{
		c.clear();
		for (int i = 0; i < b.size(); i += 2)
		{
			if (good(b[i], b[i + 1]))
			{
				c.push_back(b[i]);
			}
			else
			{
				return false;
			}
		}
		swap(b, c);
	}
	return true;
}

void solve()
{
	int n, r, p, s;  cin >> n >> r >> p >> s;
	
	vector<char> a;
	for (int i = 0; i < p; ++i) a.push_back('P');
	for (int i = 0; i < r; ++i) a.push_back('R');
	for (int i = 0; i < s; ++i) a.push_back('S');

	vector<string> w;

	do
	{
		if (correct(a))
		{
			w.push_back(string(a.begin(), a.end()));
		}
	} while (next_permutation(a.begin(), a.end()));

	sort(w.begin(), w.end());
	
	if (w.empty())
		cout << "IMPOSSIBLE" << endl;
	else
		cout << w[0] << endl;
}

int main()
{
	//freopen("i:/input.txt", "rt", stdin);
	//freopen("i:/input.out", "wt", stdout);

	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}