#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

void set_vec2(std::vector<std::vector<int>>& vec2) {
	for (int y = 0; y < 4; ++y) {
		std::vector<int> line;
		for (int x = 0; x < 4; ++x) {
			int num;
			std::cin >> num;
			line.push_back(num);
		}
		vec2.push_back(line);
	}
}

std::string solve(const std::vector<int>& xs, const std::vector<int>& ys) {
	int match_count = 0;
	int card = -1;
	
	for (auto x : xs) {
		auto iter = find(ys.begin(), ys.end(), x);
		if (iter != ys.end()) {
			++match_count;
			card = *iter;
		}
	}
	
	if (match_count > 1) {
		return "Bad magician!";
	} else if (match_count == 1) {
		return std::to_string(card);
	} else {
		return "Volunteer cheated!";
	}
}

int main() {
	int n;
	std::vector<std::string> answers;
	
	std::cin >> n;
	for (int i = 0; i < n; ++i) {
		int row_num1, row_num2;
		std::vector<std::vector<int>> square_grid1, square_grid2;
		
		std::cin >> row_num1;
		set_vec2(square_grid1);
		std::cin >> row_num2;
		set_vec2(square_grid2);
		answers.push_back(
			solve(square_grid1.at(row_num1 - 1), square_grid2.at(row_num2 - 1))
		);
	}
	
	for (int i = 0; i < answers.size(); ++i) {
		std::cout << "Case #" << i + 1 << ": " << answers.at(i) << std::endl;
	}
}

