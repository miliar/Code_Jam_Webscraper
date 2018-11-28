#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <fstream>

using namespace std;

int solve(
	const vector< vector<int> > a, int ra,
	const vector< vector<int> > b, int rb
) {
	vector<bool> used(17, false);

	for (int i = 0; i < a[ra].size(); ++i) {
		used[a[ra][i]] = true;
	}

	int cnt = 0;
	int ans = -2;
	for (int i = 0; i < b[rb].size(); ++i) {
		if (used[b[rb][i]]) {
			ans = b[rb][i];
			++cnt;
		}
	}

	if (cnt == 1) {
		return ans;
	}
	else if (cnt > 1) {
		return -1;
	}

	return ans; // cnt == 0
}

int main() {
	ifstream input("A-small-attempt0.in");
	ofstream output("A-small-attempt0.out");

	int test_count;
	input >> test_count;

	for (int i = 1; i <= test_count; ++i) {
		int ra;
		input >> ra;
		vector< vector<int> > a(4, vector<int>(4));
		for (int x = 0; x < 4; ++x) {
			for (int y = 0; y < 4; ++y) {
				input >> a[x][y];
			}
		}

		int rb;
		input >> rb;
		vector< vector<int> > b(4, vector<int>(4));
		for (int x = 0; x < 4; ++x) {
			for (int y = 0; y < 4; ++y) {
				input >> b[x][y];
			}
		}

		int res = solve(a, ra - 1, b, rb - 1);
		output << "Case #" << i << ": ";
		if (res > 0) {
			output << res;
		}
		else if (res == -1) {
			output << "Bad magician!";
		}
		else {
			output << "Volunteer cheated!";
		}
		output << endl;
	}

	return 0;
}
