#include<iostream>
#include<fstream>
#include<vector>

int a(const std::vector<int>& data) {
	int sum = 0;
	for (int i = 0; i < data.size() - 1; ++i) {
		if (data[i] > data[i + 1]) {
			sum += (data[i] - data[i + 1]);
		}
	}
	return sum;
}

int b(const std::vector<int>& data) {
	int max = 0;
	for (int i = 0; i < data.size() - 1; ++i) {
		int diff = data[i] - data[i + 1];
		if (max < diff) {
			max = diff;
		}
	}

	int count = 0;
	for (int i = 0; i < data.size() - 1; ++i) {
		int t = data[i] - max;
		if (t > 0) {
			count += max;
		}
		else {
			count += data[i];
		}
//		int c = data[i + 1] - t;
	}
	return count;
}

int main() {
	std::ifstream input("A-large.in");
	std::ofstream output("output.txt");

	int count;

	input >> count;

	for (int i = 0; i < count; ++i) {
		int size;
		input >> size;

		std::vector<int> data;

		for (int j = 0; j < size; ++j) {
			int tmp;
			input >> tmp;
			data.push_back(tmp);
		}

		output << "Case #" << (i + 1) << ": " << a(data) << " " << b(data) << "\n";
	}
}
