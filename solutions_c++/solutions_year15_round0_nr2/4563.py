#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

bool done(const std::vector<int>& data) {
	for (int i = 0; i < data.size(); ++i) {
		if (data[i] > 1) {
			return false;
		}
	}
	return true;
}

std::vector<int> eat(const std::vector<int>& data) {
	std::vector<int> new_data;
	for (int i = 0; i < data.size(); ++i) {
		if (data[i] > 1) {
			new_data.push_back(data[i] - 1);
		}
	}
	return new_data;
}

std::vector<int> split(const std::vector<int>& data, int& count) {
	std::vector<int> new_data = data;
	int max = 0;
	for (int i = 0; i < data.size(); ++i) {
		if (data[i] > data[max]) {
			max = i;
		}
	}
	if (data[max] < 4) {
		new_data[max] -= 1;
		new_data.push_back(1);
		count = 1;
	}
	else {
		int num = floor(pow(data[max], 0.5f));
		int a = floor(data[max] / num);
		for (int i = 0; i < num - 1; ++i) {
			new_data[max] -= a;
			new_data.push_back(a);
		}
		count = num - 1;
	}

	return new_data;
}

int solve(const std::vector<int>& data) {
	if (done(data)) {
		return 1;
	}
	else {
		int count = 0;
		int minutes = solve(split(data, count));
		return std::min(minutes + count, solve(eat(data)) + 1);
	}
}

int main() {
	std::ifstream input("B-small-attempt5.in");
	std::ofstream output("output.txt");

	int count;
	input >> count;
	
	for (int i = 0; i < count; ++i) {
		int diners;
		input >> diners;

		std::vector<int> data;
		for (int j = 0; j < diners; ++j) {
			int pancakes;
			input >> pancakes;
			data.push_back(pancakes);
		}

		output << "Case #" << (i + 1) << ": " << solve(data) << std::endl;
	}

	return 0;
}
