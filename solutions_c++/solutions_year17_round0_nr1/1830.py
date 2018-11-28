#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

void solve()
{
	string p;
	int k, f(0);
	cin >> p >> k;
	FOR(i, (int) p.size() - k + 1) {
		if (p[i] == '-') {
			++f;
			for (int j=i; j<i+k; ++j) p[j] = '+' + '-' - p[j];
		}
	}
	for (int i=p.size() - k + 1; i<(int) p.size(); ++i) {
		if (p[i] == '-') {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << f;
}

int main()
{
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
