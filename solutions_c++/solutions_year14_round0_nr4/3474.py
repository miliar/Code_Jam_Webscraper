#include<iostream>
#include<vector>
#include<algorithm>
#include<functional>

int indexOfNextBigger(std::vector<double> &vec, double find) {
	int i = 0;
	for (auto it : vec) {
		if (it > find)
			return i;
		i++;
	}
	return -1;
}

int standardWins(std::vector<double> mine, std::vector<double> theirs) {
	int wins = 0, idx;
	std::sort(mine.begin(), mine.end(), std::greater<double>());
	for (auto it = mine.begin(); it != mine.end();) {
		idx = indexOfNextBigger(theirs, *it);
		if (idx == -1) {
			theirs.erase(theirs.begin());
			it = mine.erase(it);
			wins++;
		}
		else {
			it = mine.erase(it);
			theirs.erase(theirs.begin() + idx);
		}
	}
	return wins;
}

int deceitfulWins(std::vector<double> mine, std::vector<double> theirs) {
	int wins = 0;
	int n, k, len;
	len = mine.size();
	
	for (n = 0, k = 0; n < len && k < len;) {
		if (mine[n] > theirs[k]) {
			wins++;
			n++;
			k++;
		}
		else
			n++;
	}

	return wins;
}

int main(void) {
	int cases;
	std::cout << std::fixed;
	std::cin >> cases;
	int current = 1;
	while (cases--) {
		int len;
		std::vector<double> Naomi;
		std::vector<double> Ken;
		std::cin >> len;
		double in;
		for (int i = 0; i < len; ++i) {
			std::cin >> in;
			Naomi.push_back(in);
		}

		for (int i = 0; i < len; ++i) {
			std::cin >> in;
			Ken.push_back(in);
		}

		std::sort(Naomi.begin(), Naomi.end());
		std::sort(Ken.begin(), Ken.end());
		std::cout << "Case #" << current << ": " << deceitfulWins(Naomi, Ken) << " " << standardWins(Naomi, Ken) << std::endl;
		current++;
	}
	return 0;
}
