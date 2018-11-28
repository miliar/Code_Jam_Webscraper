#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cassert>

using namespace std;


int main()
{
	int t; cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n; cin >> n;
		if (n == 0) {
			std::cout << "Case #" << i << ": INSOMNIA\n";
			continue;
		}
		bool seen[10] = {};
		auto all_seen = [&] { return std::all_of(seen, seen + 10, [](bool b) { return b; });};
		int res = 1;
		for (; !all_seen(); ++res) {
			int x = n * res;
			char nums[64] = {};
			snprintf(nums, 64, "%d", x);
			for (int k = 0; k < strlen(nums); ++k) 
				seen[nums[k] - '0'] = true;
		}
		std::cout << "Case #" << i << ": " << (n*(res - 1)) << "\n";
	}

	return 0;
}