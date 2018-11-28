// https://code.google.com/codejam/contest/6224486/dashboard#s=p0
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <iostream>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdint>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int Smax;
		cin >> Smax;
		string S;
		cin >> S;
		int ans = 0;
		int standup = 0;
		for (int i = 0; i < Smax + 1; i++) {
			int n = S[i] - '0';
			if (i > standup) {
				int need = (i - standup);
				ans += need;
				standup += need;
			}
			standup += n;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
