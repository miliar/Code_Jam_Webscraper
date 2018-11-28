#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <memory>
#include <numeric>

typedef int64_t INT;
typedef uint64_t UINT;

using namespace std;

class Pb {
public:
	UINT mod = UINT(1000000007L);
	int N;
	vector<string> cars;

	string str;
	vector<bool> met;

	Pb(int N) : N(N), cars(N), met(256) {
	}


	bool isok(const vector<int>& order) {
		if (order.empty()) return false;
		int offset = 0;
		for (int i : order) {
			for (char c : cars[i]) {
				str[offset++] = c;
			}
		}
		char c = str[0];
		for (int i = 'a'; i <= 'z'; ++i) {
			met[i] = false;
		}
		met[c] = true;
		for (int i = 1; i < str.length(); ++i) {
			if (str[i] == c) continue;
			c = str[i];
			if (met[c]) return false;
			met[c] = true;;
		}
		return true;
	}

	UINT solveSmall() {
		for (int i = 0; i < N; ++i) {
			str += cars[i];
		}
		vector<int> order(N);
		vector<int> gen(N, 0);
		UINT count = 0;
		while (true) {
			for (int i = 0; i < N; ++i) {
				order[i] = i;
			}
			for (int i = 0; i < N; ++i) {
				swap(order[i], order[i + gen[N-i-1]]);
			}
			if (isok(order)) {
				++count;
			}
			int zeroes = 0;
			for (int i = 0; i < N; ++i) {
				gen[i]++;
				if (gen[i] == i + 1) {
					gen[i] = 0;
					++zeroes;
				}
				else {
					break;
				}
			}
			if (zeroes == N) {
				break;
			}
		}
		return count % mod;
	}

	UINT _solveSmall() {
		UINT max = 1;
		for (int i = 0; i < N; ++i) max *= N;
		vector<bool> taken(N);
		vector<int> order;
		order.reserve(N);
		UINT count = 0;
		for (UINT i = 0; i <= max; ++i) {
			order.clear();
			for (int j = 0; j < N; ++j) taken[j] = false;
			UINT t = i;
			bool error = false;
			for (int j = 0; j < N; ++j) {
				UINT c = t%N;
				t /= N;
				if (taken[c]) {
					error = true;
					break;
				}
				taken[c] = true;
				order.push_back(c);
			}
			if (!error) {
				if (isok(order)) {
					++count;
				}
			}
		}
		return count % mod;
	}
};

int main(int argc, char* argv[])
{
	ifstream input("C:/users/sebastien/Downloads/B-small-attempt0.in");
	//ifstream input("C:/users/sebastien/Downloads/example.in");
	ofstream output("C:/users/sebastien/Downloads/output.txt");

	output.precision(10);

	int T;
	input >> T;

	for (int test = 1; test <= T; ++test) {
		cout << "test " << test << "\n";
		output << "Case #" << test << ": ";

		int N;
		input >> N;
		Pb pb(N);
		for (int i = 0; i < N; ++i) {
			input >> pb.cars[i];
		}
		output << pb.solveSmall();

		output << "\n";
	}
	output.close();

	{
		cout << "DONE\n";
		int _;
		cin >> _;
	}

	return 0;
}
