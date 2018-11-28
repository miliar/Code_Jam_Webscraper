#include <iostream>
#include <thread>
#include <atomic>
#include <vector>
#include <map>

int main(int argc, char** argv) {
	typedef std::map<int, int> map_t;

	int t;
	std::cin >> t;
	for(int t_=1; t_<=t; ++t_) {
		map_t m;
		int shy;
		char c;

		std::cin >> shy;
		for(int i=0; i<=shy; ++i) {
			std::cin >> c;

			m.insert(std::make_pair(i, int(c - '0')));
		}

		int add = 0;
		int current = 0;
		auto it = m.begin();
		auto itEnd = m.end();

		while(it != itEnd) {
			auto const& p = *it;
			if(p.second > 0) {
				int tmp = std::max(0, (p.first - current));
				add += tmp;
				current += tmp + p.second;
			}

			++it;
		}

		std::cout << "Case #" << t_ << ": " << add << std::endl;
	}

	return 0;
}