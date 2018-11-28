#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

std::vector<std::string> splitString(const std::string& s, const std::string& delimiter) {
	std::vector<std::string> v;
	size_t start = 0;
	auto end = s.find(delimiter);

	if (end == std::string::npos) {
		v.push_back(s);
	}
	else {
		while (end != std::string::npos) {
			v.push_back(s.substr(start, end - start));
			end += delimiter.length();
			start = end;
			end = s.find(delimiter, end);

			if (end == std::string::npos) {
				v.push_back(s.substr(start, s.length()));
			}
		}
	}

	return v;
}

struct Digits {
	vector<bool> digits;
	int fillNumber;
	explicit Digits() : digits(10), fillNumber{ 0 } {}
};

static bool fillDigits(Digits& digits, int N) {
	if (digits.fillNumber == 10) return true;

	while (N > 0) {
		const int digit = N % 10;
		if (digits.digits[digit] == false) {
			digits.digits[digit] = true;
			digits.fillNumber++;
		}
		N /= 10;
	}

	return digits.fillNumber == 10;
}

void solve(std::ifstream& in, std::ofstream& out) {
	int testCaseNum, N;
	in >> testCaseNum;

	int t{ 1 };

	while (t <= testCaseNum) {
		Digits digits{};
		bool find = false;
		int i;
		in >> N;
		int nextN = N;

		for (i = 1; i < 100000; i++) {
			if (fillDigits(digits, nextN)) {
				find = true;
				break;
			}
			nextN += N;
		}

		if (i == 100000) {
			out << "Case #" << t << ": " << "Something Wrong here" << std::endl;
		}

		if (find) {
			out << "Case #" << t << ": " << nextN << std::endl;
		}
		else {
			out << "Case #" << t << ": " << "INSOMNIA" << std::endl;
		}
		t++;
	}
}

int main() {
	std::ifstream smallDataFile{ "small-practice.in" };
	//std::ifstream largeDataFile{ "C-large-practice.in" };
	std::ofstream smallOutputFile{ "small.out" };
	//std::ofstream largeOutputFile{ "C-large.out" };

	solve(smallDataFile, smallOutputFile);
	//solve(largeDataFile, bigOutputFile);

	return 0;
}