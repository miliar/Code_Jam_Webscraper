#include <algorithm>
#include <deque>
#include <iostream>

int war(std::deque<double> my_blocks, std::deque<double> your_blocks);
int deceitfulWar(std::deque<double> my_blocks, std::deque<double> your_blocks);

int main() {
	int tests;
	std::cin >> tests;
	for (int i = 1; i <= tests; ++i) {
		int blocks;
		std::cin >> blocks;
		std::deque<double> blocks_naomi, blocks_ken;

		for (int j = 0; j < blocks; ++j) {
			double in;
			std::cin >> in;
			blocks_naomi.push_back(in);
		}
		for (int j = 0; j < blocks; ++j) {
			double in;
			std::cin >> in;
			blocks_ken.push_back(in);
		}

		std::sort(blocks_naomi.begin(), blocks_naomi.end());
		std::sort(blocks_ken.begin(), blocks_ken.end());

		std::cout << "Case #" << i << ": "
		          << deceitfulWar(blocks_naomi, blocks_ken)
		          << " "
		          << war(blocks_naomi, blocks_ken)
		          << std::endl;
	}
}

int war(std::deque<double> my_blocks, std::deque<double> your_blocks) {
	int points = 0;
	while (my_blocks.size() > 0) {
		if (my_blocks.back() > your_blocks.back()) {
			++points;
			my_blocks.pop_back();
			your_blocks.pop_front();
		} else {
			my_blocks.pop_back();
			your_blocks.pop_back();
		}
	}
	return points;
}

int deceitfulWar(std::deque<double> my_blocks, std::deque<double> your_blocks) {
	int points = 0;
	while (my_blocks.size() > 0) {
		for (int j = 0; j < my_blocks.size(); ++j) {
			if (my_blocks.front() < your_blocks.front()) {
				my_blocks.pop_front();
				your_blocks.pop_back();
			} else {
				break;
			}
		}
		for (int j = 0; j < my_blocks.size(); ++j) {
			if (my_blocks.front() > your_blocks.front()) {
				my_blocks.pop_front();
				your_blocks.pop_front();
				++points;
			} else {
				break;
			}
		}
	}
	return points;
}
