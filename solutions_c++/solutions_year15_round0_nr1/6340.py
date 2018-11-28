#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int solve(int s_max, string s_k) {
	int i_k[s_k.length()];
	for (int i = 0; i < s_k.length(); i++) {
		i_k[i] = s_k[i] % 48;
	}

	int ret = 0;
	int currentlyStanding = 0;
	for (int i = 0; i <= s_max; i++) {
		if (i_k[i] == 0) continue;

		if (i <= currentlyStanding) {
			currentlyStanding += i_k[i];
		} else {
			ret += (i - currentlyStanding);
			currentlyStanding += (i - currentlyStanding);
			currentlyStanding += i_k[i];
		}

//		cout << "index: " << i << endl;
//		cout << "ret: " << ret << endl;
//		cout << "curst: " << currentlyStanding << endl;
		
	}

	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int s_max;
		cin >> s_max;
		string s_k;
		cin >> s_k;
		
		int res = solve(s_max, s_k);
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}
