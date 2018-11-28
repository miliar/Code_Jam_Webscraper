#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <array>
#include <cassert>

using namespace std;

struct Pancakes {
	Pancakes(const std::string s) {
		mem.resize(s.size());
		for (size_t i = 0; i < s.size(); ++i) mem[i] = s[i] == '+' ? 1 : 0;
	}

	Pancakes(const Pancakes&) = default;
	Pancakes& operator=(const Pancakes&) = default;
	Pancakes(Pancakes&&) = default;
	Pancakes& operator=(Pancakes&&) = default;

	void flip(size_t end) {
		assert(end <= mem.size());
		std::reverse(mem.begin(), mem.begin() + end);
		for (size_t i = 0; i < end; ++i)
			mem[i] = mem[i] == 0 ? 1 : 0;
	}

	bool operator< (const Pancakes& other) const {
		return mem < other.mem;
	}

	bool operator== (const Pancakes& other) const {
		return mem == other.mem;
	}

	vector<char> mem;
};

int main()
{
	int t; cin >> t;
	for (int i = 1; i <= t; ++i) {
		string in;
		cin >> in;

		vector<set<Pancakes>> levels(20);
		string init(in.size(), '+');
		levels[0].emplace(init);

		const Pancakes goal(in);

		auto res = [&] {
			for (size_t l = 0; levels[l].size(); ++l) {
				for (const auto& x : levels[l]) {
					if (x == goal)
						return l;
					for (size_t i = 1; i <= in.size(); ++i) {
						auto cpy = x;
						cpy.flip(i);
						if (cpy == goal)
							return l + 1;
						levels[l + 1].emplace(std::move(cpy));
					}
				}
			}
		};

		std::cout << "Case #" << i << ": " << res() << "\n";
	}

	return 0;
}