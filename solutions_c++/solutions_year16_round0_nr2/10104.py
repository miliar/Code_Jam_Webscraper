#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

// false = happy, true = blank
vector<long long> sol;
vector<bool> happy(100, false);	// no pancake stack will be over 100 so no buffer overrun issues
unordered_map<string, long long> memo;

void solve(vector<bool> pancakes, bool flipped, int pos, long long flips) {
	string s = "";
	for (size_t i = 0; i < pancakes.size(); i++) {
		s += pancakes[i];
	}

	if (equal(pancakes.begin(), pancakes.end(), happy.begin())) {
		sol.push_back(flips);
		return;
	}

	if (pos == pancakes.size())
		return;

	if (flipped) {
		solve(pancakes, false, pos + 1, flips);
		return;
	}

	// try flipping and not flipping
	vector<bool> flipped_stack(pancakes);
	for (int i = 0; i <= pos; i++) {
		flipped_stack[i] = !flipped_stack[i];
	}
	solve(flipped_stack, true, pos, flips + 1);
	solve(pancakes, false, pos + 1, flips);
}

int main() {
	ios_base::sync_with_stdio(false);
	int tc;
	string pancakes;

	cin >> tc;

	for (int t = 1; t <= tc; t++) {
		cin >> pancakes;
		vector<bool> stack(pancakes.length(), 0);
		for (size_t i = 0; i < pancakes.length(); i++) {
			stack[i] = pancakes[i] == '+' ? 0 : 1;
		}

		solve(stack, false, 0, 0);
		cout << "Case #" << t << ": " << *min_element(sol.begin(), sol.end()) << "\n";
		sol.clear();
	}
}