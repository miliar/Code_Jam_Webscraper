#include<iostream>
#include<fstream>
#include<vector>

int gcd(int x, int y) {
	if (x < y) {
		return gcd(y, x);
	}

	int f = x % y;
	if (f == 0) {
		return y;
	}
	else {
		return gcd(y, f);
	}
}

int lcm(int x, int y) {
	return x * y / gcd(x, y);
}

int a(const std::vector<int>& data, int position) {
	std::vector<int> queue;
	for (int i = 0; i < data.size(); ++i) {
		queue.push_back(0);
	}
	int c = 1;
	for (int i = 0; i < data.size(); ++i) {
		c = lcm(c, data[i]);
	}
	std::cout << c << "\n";
	int d = 0;
	for (int i = 0; i < data.size(); ++i) {
		d += c / data[i];
	}
	std::cout << d << "\n";
	position %= d;
	std::cout << position << "\n";
	if (position == 0) {
		position = d;
	}
	while (true) {
		int min = INT_MAX;
		for (int i = 0; i < queue.size(); ++i) {
			if (queue[i] <= 0) {
				queue[i] = data[i];
				--position;
				if (position == 0) {
					return i + 1;
				}
			}
			if (min > queue[i]) {
				min = queue[i];
			}
		}
		for (int i = 0; i < queue.size(); ++i) {
			queue[i] -= min;
		}
	}
}

int main() {
	std::ifstream input("B-small-attempt6.in");
	std::ofstream output("output.txt");

	int count;

	input >> count;

	for (int i = 0; i < count; ++i) {
		int barbers;
		int position;
		input >> barbers >> position;

		std::vector<int> data;
		for (int j = 0; j < barbers; ++j) {
			int tmp;
			input >> tmp;
			data.push_back(tmp);
		}

		output << "Case #" << (i + 1) << ": " << a(data, position) << "\n";
		std::cout << (i + 1) << "\n";
	}
}
