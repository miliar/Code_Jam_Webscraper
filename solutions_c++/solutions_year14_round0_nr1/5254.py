#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

void solve()
{
	int a;
	cin >> a, --a;
	
	set<int> first, second;
	for (int i = 0; i < 4; ++i)
	{
		set<int> s;
		for (int j = 0, x; j < 4; ++j)
			cin >> x, s.insert(x);
		if (i == a) first = s;
	}
	
	cin >> a, --a;
	for (int i = 0; i < 4; ++i)
	{
		set<int> s;
		for (int j = 0, x; j < 4; ++j)
			cin >> x, s.insert(x);
		if (i == a) second = s;
	}
	
	int ans[4];
	int sz = set_intersection(first.begin(), first.end(), second.begin(), second.end(), ans) - ans;
	if (sz == 0) cout << "Volunteer cheated!" << endl;
	else if (sz == 1) cout << ans[0] << endl;
	else cout << "Bad magician!" << endl;
}

int main() 
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
    cin >> t;
    for (int i = 0; i < t; ++i) 
		cout << "Case #" << i + 1 << ": ", solve();
    return 0;
}

