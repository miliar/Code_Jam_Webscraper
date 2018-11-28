#include <bits/stdc++.h>

using namespace std;

vector< int > a;

inline bool canEatWithin(int time)
{
    bool found = false;
    for (int totalSplitCount = 0; totalSplitCount < time && !found; totalSplitCount++) {
	int curTotalSplits = 0;

	for (int i = 0; i < a.size() && curTotalSplits <= totalSplitCount; i++) {
	    int haveTime = time - totalSplitCount;
	    int k = (a[i] + haveTime - 1) / haveTime;
	    curTotalSplits += (k - 1);
	}

	if (curTotalSplits <= totalSplitCount) {
	    found = true;
	}
    }

    return found;
}

void solve(int testnum)
{
    int n;
    cin >> n;

    a.resize(n);

    for (int i = 0; i < n; i++) {
	cin >> a[i];
    }

    int l = 0;
    int r = 3000;
    while (l < r - 1) {
	int m = l + (r - l) / 2;

	if (canEatWithin(m)) {
	    r = m;
	} else {
	    l = m;
	}
    }

    cout << "Case #" << testnum + 1 << ": " << r << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int q = 0; q < t; q++) {
	solve(q);
    }
}
