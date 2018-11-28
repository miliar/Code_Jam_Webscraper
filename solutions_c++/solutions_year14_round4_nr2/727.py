#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define foreach(e, x) for (__typeof(x.begin()) e = x.begin(); e != x.end(); e++)
typedef long long LL;
typedef pair<int, int> PII;

int t, n;
vector<int> a;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    cin >> t;
    REP(test, t) {
		cin >> n;
		a.resize(n);
		REP(i, n)
			cin >> a[i];
		int ans = 0;
		while (a.size() > 1) {
			int mni = 0;
			for (int i = 1; i < (int)a.size(); ++i)
				if (a[i] < a[mni])
					mni = i;
			ans += min(mni, (int)a.size() - 1 - mni);
			a.erase(a.begin() + mni, a.begin() + mni + 1);
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
    }
    return 0;
}
