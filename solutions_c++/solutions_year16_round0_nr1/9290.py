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

int T, N;
bool was[10];

void mark(int X) {
	ostringstream os;
	os << X;
	string s = os.str();
	for (int i = 0; i < s.length(); ++i)
		was[s[i] - '0'] = 1;
}

bool check() {
	for (int i = 0; i < 10; ++i)
		if (!was[i])
			return false;
	return true;
}

void solve(int tc) {
	cin >> N;
	int tmp = N, ans = -1;
	memset(was, 0, sizeof was);
	if (N != 0) {
		while (true) {
			mark(tmp);
			if (check()) {
				ans = tmp;
				break;
			}
			tmp += N;
		}
	}
	cout << "Case #" << tc << ": ";
	if (N != 0)
		cout << ans << '\n';
	else
		cout << "INSOMNIA" << '\n';
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
