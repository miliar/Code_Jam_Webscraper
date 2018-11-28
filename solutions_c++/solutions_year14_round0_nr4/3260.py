#include <stdio.h>
#include <vector>
#include <iostream>
#include<algorithm>

int war(std::vector<double> &naomi_blocks, std::vector<double> ken_blocks_sorted) {

	std::vector<double>::iterator naomi_iterator = naomi_blocks.begin();

	int points = 0;
	while (naomi_iterator != naomi_blocks.end()) {

		std::vector<double>::iterator ken_choice = std::upper_bound(ken_blocks_sorted.begin(), ken_blocks_sorted.end(), (*naomi_iterator));
		if (ken_choice == ken_blocks_sorted.end()) {
			// select lowest eleement
			ken_choice = ken_blocks_sorted.begin();
			points++;
		}

		ken_blocks_sorted.erase(ken_choice);

		naomi_iterator++;
	}

	return points;
}

int deceitful_war(std::vector<double> &naomi_blocks, std::vector<double> &ken_blocks_sorted) {

	std::sort(naomi_blocks.begin(), naomi_blocks.end());
	std::vector<double>::iterator naomi_iterator = naomi_blocks.begin();

	int points = 0;

	while (naomi_blocks.size() > 0) {

		double naomi_last = *(naomi_blocks.end() - 1);
		double ken_last = *(ken_blocks_sorted.end() - 1);

		if (naomi_last > ken_last) {
			points++;
			naomi_blocks.erase(naomi_blocks.end() - 1);
		} else {
			naomi_blocks.erase(naomi_blocks.begin());
		}

		ken_blocks_sorted.erase(ken_blocks_sorted.end() -1);
	}

	return points;
}

int main() {

	std::ios_base::sync_with_stdio(0);

	int caseNo;
	std::cin >> caseNo;
	for (int i = 1; i <= caseNo; i++) {

		int blocksNo;
		std::cin >> blocksNo;

		std::vector<double> naomi_blocks;
		std::vector<double> ken_blocks;

		for (int i = 1; i <= 2*blocksNo; i++) {
			
			double block;
			std::cin >> block;

			if (i <= blocksNo) {
				naomi_blocks.push_back(block);
			} else {
				ken_blocks.push_back(block);
			}
		}

		std::sort(ken_blocks.begin(), ken_blocks.end());
		int war_result = war(naomi_blocks, ken_blocks);
		int deceitful_war_result = deceitful_war(naomi_blocks, ken_blocks);

		std::cout << "Case #" << i << ": " << deceitful_war_result << " " << war_result << std::endl;
	}
}