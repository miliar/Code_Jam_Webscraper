#include <iostream>
#include <string>
#include <fstream>

//auto& in = std::cin;
//auto& out = std::cout;

int main() {
	std::ifstream in("A-large.in");
	std::ofstream out("output.txt");
	int t; in >> t;

	for (int k = 1; k <= t; ++k) {
		int smax; in >> smax;
		std::string a; in >> a;

		int sum = 0;
		int r   = 0;

		for (int i = 0; i < a.length(); ++i) {
			sum += (a[i] - '0');
			if (a[i] == '0' && sum < (i+1)) {
				r++;
				sum++;
			}
		}

		out << "Case #" << k << ": " << r << '\n';
	}

	return 0;
}