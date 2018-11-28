#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <string>
using namespace std;
int t;

void solve()
{
	vector<set<int> > a(4), b(4);
	int r1, r2, tmp;
	cin >> r1;
	--r1;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cin >> tmp;
			a[i].insert(tmp);
		}
	}

	cin >> r2;
	--r2;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cin >> tmp;
			b[i].insert(tmp);
		}
	}
	set<int> ans;
	for (set<int>::const_iterator it = a[r1].begin(); it != a[r1].end(); ++it )
	{
		if (b[r2].find(*it) != b[r2].end())
			ans.insert(*it);
	}
	if (ans.size() == 0)
		cout << "Volunteer cheated!" << endl;
	else if (ans.size() == 1)
		cout << *(ans.begin()) << endl;
	else
		cout << "Bad magician!" << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}