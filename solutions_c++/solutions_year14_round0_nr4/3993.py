#include <iostream>
#include <list>

int get_dw_score(std::list<double> naomi, std::list<double> ken)
{
	int score = 0;

	while (naomi.size()) {
		if (naomi.front() < ken.front()) {
			ken.pop_back();
		} else {
			ken.pop_front();
			score++;
		}

		naomi.pop_front();
	}

	return score;
}

int get_w_score(std::list<double> naomi, std::list<double> ken)
{
	int score = 0;

	while (ken.size()) {
		while (ken.size()) {
			if (ken.front() < naomi.front()) {
				ken.pop_front();
				score++;
			} else {
				naomi.pop_front();
				ken.pop_front();
				break;
			}
		}
	}

	return score;
}

int main()
{
	int cases;

	std::cin >> cases;

	for (int i = 1; i <= cases; i++) {
		int n;

		std::cin >> n;

		double block;
		std::list<double> naomi;
		std::list<double> ken;

		for (int j = 0; j < n; j++) {
			std::cin >> block;
			naomi.push_back(block);
		}

		for (int j = 0; j < n; j++) {
			std::cin >> block;
			ken.push_back(block);
		}

		naomi.sort();
		ken.sort();

		int dw_score = get_dw_score(naomi, ken);
		int w_score = get_w_score(naomi, ken);

		std::cout << "Case #" << i << ": " << dw_score << " " <<  w_score << std::endl;
	}

	return 0;
}
