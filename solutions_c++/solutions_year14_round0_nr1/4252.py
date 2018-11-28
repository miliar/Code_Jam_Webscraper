#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <cstring>

#define forn(i, n) for (int i = 0; i < (int)n; ++i)

using namespace std;

vector<int> answer() {
	int r;
	scanf("%d", &r);
	vector<int> res;
	forn(i, 4) {
		forn(j, 4) {
			int x;
			scanf("%d", &x);
			if (i + 1 == r) {
				res.push_back(x);
			}
		}
	}
	return res;
}

void solve()
{
	vector<int> ans1 = answer();
	vector<int> ans2 = answer();
	vector<int> res;
	for (int i = 0; i < ans1.size(); ++i) {
		for (int j = 0; j < ans2.size(); ++j) {
			if (ans1[i] == ans2[j]) {
				res.push_back(ans1[i]);
			}
		}
	}
//	cout << res.size() << endl << endl;
	if (res.size() == 1) {
		cout << res[0] << endl;
	} else if (res.size() > 1) {
		cout << "Bad magician!" << endl;
	} else {
		cout << "Volunteer cheated!" << endl;
	}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	forn(t, tt)
	{
		cout << "Case #" << (t + 1) << ": ";
		solve();
	}
	return 0;
}
