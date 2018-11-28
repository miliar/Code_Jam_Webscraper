#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 1000;

int T;
string s;
char ans[2 * MAXN];

void solve(int tc) {
	cin >> s;
	int len = s.length(), first = MAXN, last = MAXN;
	ans[first] = s[0];
	for (int i = 1; i < len; ++i) {
		if (s[i] >= ans[first])
			ans[--first] = s[i];
		else
			ans[++last] = s[i];
	}
	cout << "Case #" << tc << ": ";
	for (int i = first; i <= last; ++i)
		cout << ans[i];
	cout << '\n';
}

int main() {
	ios_base::sync_with_stdio(0);
	#ifdef ACMTUYO
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
		clock_t start = clock();
	#endif
	
	cin >> T;
	for (int tc = 1; tc <= T; ++tc)
		solve(tc);
	
	#ifdef ACMTUYO
		fprintf(stderr, "\ntime=%.3fsec\n", 1. * (clock() - start) / CLOCKS_PER_SEC);
	#endif
	return 0;
}
