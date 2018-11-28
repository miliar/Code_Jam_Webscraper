#include<iostream>
#include<fstream>
#include<string>
#include<vector>

int resolve(std::vector<int>& data) {
	if (data.size() > 0) {
		int sum = 0;
		for (int i = 0; i < data.size() - 1; ++i) {
			sum += data[i];
		}
		int last = data.size() - 1;
		data.pop_back();
		for (int i = 0; i < last - sum; ++i) {
			++data[0];
		}
		return (sum > last ? 0 : last - sum) + resolve(data);
	}
	else {
		return 0;
	}
}

int main() {
	std::ifstream input("A-large.in");
	std::ofstream output("output.txt");

	int count;
	input >> count;
	
	for (int i = 0; i < count; ++i) {
		int max;
		input >> max;

		std::vector<int> audiences;

		char c;
		input.get(c);
		for(int j = 0; j <= max; ++j) {
			input.get(c);
			audiences.push_back(atoi(&c));
		}

		output << "Case #" << (i + 1) << ": " << resolve(audiences) << std::endl;
	}

	return 0;
}
