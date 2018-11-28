#include <iostream>
#include <set>
#include <cassert>
#include <algorithm>
#include <vector>

int solve() {
	int n;
	std::cin >> n;
	std::vector<int> A;
	for (int i = 0; i < n; ++i) {
		int a;
		std::cin >> a;
		A.push_back(a);
	}

	std::vector<int> pos(n);
	struct index_sorter_int {
		const int *base;
		index_sorter_int(const int *base) : base(base) {}

		bool operator() (int x, int y) {
			return base[x] < base[y];
		}
	};
	for (int i = 0; i < n; ++i)
		pos[i] = i;

	std::sort(pos.begin(), pos.end(), index_sorter_int(A.data()));
	{
		int last = A[pos[0]];
		for (int i = 1; i < n; ++i) {
			assert(A[pos[i]] > last);
			last = A[pos[i]];
		}
	}


	std::vector<bool> removed(n, false);
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		int p = pos[i];
		removed[p] = true;
		int left_moves = 0;
		for (int j = 0; j < p; ++j)
			if (!removed[j])
				++left_moves;
		int right_moves = 0;
		for (int j = n - 1; j > p; --j)
			if (!removed[j])
				++right_moves;
		ret += std::min(left_moves, right_moves);
	}

	return ret;
}

int main() {
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		std::cout << "Case #" << i << ": "
			  << solve() << "\n";
	}
	return 0;
}
