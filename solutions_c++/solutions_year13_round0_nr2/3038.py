// Lawnmover
#include <iostream>
#include <iomanip>
#include <sstream>

void print(const int *data, const int n, const int m) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			std::cout << std::setw(4) << data[i*m + j];
		}
		std::cout << std::endl;
	}
}

bool isPossible(const int *data, const int n, const int m) {
	int *lawn = new int[n*m];
	for (int i = 0; i < n*m; i++) {
		lawn[i] = 100;
	}

	// cut aong rows.
	for (int i = 0; i < n; i++) {
		int h = 100;
		auto maxel = [&] () {
			int mx = data[i*m];
			for (int j = 1; j < m; j++) {
				if (data[i*m + j] > mx) mx = data[i*m + j];
			}
			return mx;
		};
		auto runlm = [&] () {
			for (int j = 0; j < m; j++) {
				lawn[i*m + j] = std::min(h, lawn[i*m + j]);
			}
		};

		h = maxel();
		runlm();
	}

	// cut along columns
	for (int j = 0; j < m; j++) {
		int h = 100;
		auto maxel = [&] () {
			int mx = data[j];
			for (int i = 1; i < n; i++) {
				if (data[i*m + j] > mx) mx = data[i*m + j];
			}
			return mx;
		};
		auto runlm = [&] () {
			for (int i = 0; i < n; i++) {
				lawn[i*m + j] = std::min(h, lawn[i*m + j]);
			}
		};

		h = maxel();
		runlm();
	}

	bool pos = true;
	for (int i = 1; i < n*m; i++) {
		if (data[i] != lawn[i]) {
			pos = false;
			break;
		}
	}

	// std::cout << "After " << std::endl;
	// print(lawn, n, m);

	delete lawn;
	return pos;
}


int main(void) {
	std::string line;
	std::getline(std::cin, line);

	int ncases = std::stoi(line);

	auto readdata = [] (int *data, const int n, const int m) {
		for (int i = 0; i < n; i++) {
			std::string line;
			std::getline(std::cin, line);
			
			std::stringstream ss;
			ss << line;
			for (int j = 0; j < m; j++) {
				ss >>	data[i*m + j];
			}
		}
	};

	for (int i = 1; i <= ncases; i++) {
		std::getline(std::cin, line);
		int n, m;
		std::stringstream ss;
		ss << line;
		ss >> n >> m;

		int *data = new int[n*m];
		readdata(data, n, m);
		// std::cout << "Before " << std::endl;
		// print(data, n, m);

		std::string ans = isPossible(data, n, m) ? "YES" : "NO";
		std::cout << "Case #" << i << ": " << ans << std::endl;

		delete data;
	}
	return 0;
}

