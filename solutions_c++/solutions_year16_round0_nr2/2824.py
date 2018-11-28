#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int n, m;

int main(){
	cin >> m;
	for (int T = 1; T <= m; ++T) {
		cout << "Case #" << T << ": ";

		string s;
		cin >> s;
		int n = s.length(), ans = 0;
		for (int i = n - 1; i >= 0; --i) {
			int c = (s[i] == '-');
			if ((ans + c) & 1) ++ans;
		}
		cout << ans << endl;
	}
}
