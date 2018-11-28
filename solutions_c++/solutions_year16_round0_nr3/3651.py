#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <queue>
#include <unordered_map>
#include <cmath>
#include <cstdint>

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

class CoinJam {
public:
	vector<int> representBasesstring;
	int N;
	vector<int64_t> representBases;

	explicit CoinJam(const int N) : N{N}, representBasesstring(N), representBases(9) {
		representBasesstring[0] = 1;
		representBasesstring[N - 1] = 1;
	}	

	bool isCoinJam() {
		calculateRepresentBases();

		for (auto& representVal : representBases) {
			if (isPrime(representVal)) return false;
		}

		return true;
	}

	vector<int64_t> getDivisors() {
		vector<int64_t> divisors{};

		for (auto number : representBases) {
			divisors.emplace_back(findNonTrivialDivisor(number));
		}

		return divisors;
	}

private:

	void calculateRepresentBases() {
		for (int base = 2; base <= 10; ++base) {
			representBases[base - 2] = 0;
			for (int i = 0; i < N; i++) {
				if (representBasesstring[i] == 0) continue;
				representBases[base - 2] += static_cast<int64_t>(pow(base, N - 1 - i));
			}
		}
	}

	bool isPrime(int64_t number) {
		if (number <= 1) return 0; // zero and one are not prime
		int64_t i;
		for (i = 2; i*i <= number; i++) {
			if (number % i == 0) return false;
		}
		return true;
	}	

	int64_t findNonTrivialDivisor(const int64_t number) {
		for (int64_t i = 2; i*i <= number; i++) {
			if (number % i == 0) return i;
		}

		return -1;
	}
};

void solve(std::ifstream& in, std::ofstream& out) {
	int testCaseNum;
	in >> testCaseNum;
	int t{ 1 };

	while (t <= testCaseNum) {
		int N, J;
		in >> N;
		in >> J;
		int j = 0;
		vector<CoinJam> coinJamList{ CoinJam{N} };		

		out << "Case #" << t << ": " << std::endl;

		// generate all posible string 
		for (int i = N-2; i > 0; --i) {
			vector<CoinJam> newCoinJamList{};

			for (auto& coinJam : coinJamList) {	
				CoinJam newCoinJam = coinJam;
				newCoinJam.representBasesstring[i] = 1;
				if (newCoinJam.isCoinJam()) {
					for (auto number : newCoinJam.representBasesstring) {
						out << number;
					}
					out << " ";

					/*
					for (auto number : newCoinJam.representBases) {
					out << number << " ";
					}
					*/

					auto divisors = newCoinJam.getDivisors();
					for (auto number : divisors) {
						out << number << " ";
					}
					out << std::endl;

					j++;
					if (j == J) {
						break;
					}
				}
				newCoinJamList.push_back(newCoinJam);
			}

			if (j == J) {
				break;
			}

			coinJamList.insert(coinJamList.begin(), newCoinJamList.begin(), newCoinJamList.end());
		}

		//out << "Case #" << t << ": " << step << std::endl;
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