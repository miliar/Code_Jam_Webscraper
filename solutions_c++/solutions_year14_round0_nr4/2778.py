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

int first_game(set<double> a, set<double> b) {
	while (!a.empty() && !b.empty() && (*a.begin() < *(b.rbegin()))) {
		auto b_iter = b.upper_bound(*a.begin());
		b.erase(b_iter);
		a.erase(a.begin());
	}
	return a.size();
}

int second_game(set<double> a, set<double> b) {
	int ans = 0;
	while (!a.empty() && !b.empty()) {
		if (*(a.rbegin()) > *(b.rbegin())) {
			++ans;
			a.erase(--a.end());
		}
		else {
			a.erase(a.begin());
		}

		b.erase(--b.end());
	}
	return ans;
}

int main() {
	ifstream input("D-large.in");
	ofstream output("D-large.out");

	int test_count;
	input >> test_count;
	for (int i = 1; i <= test_count; ++i) {
		int N;
		input >> N;
		set<double> a;
		set<double> b;
		double val;
		for (int k = 0; k < N; ++k) {
			input >> val;
			a.insert(val);
		}
		for (int k = 0; k < N; ++k) {
			input >> val;
			b.insert(val);
		}

		output << "Case #" << i << ": " << second_game(a, b) << " " << first_game(a, b) << endl;
	}

	return 0;
}
