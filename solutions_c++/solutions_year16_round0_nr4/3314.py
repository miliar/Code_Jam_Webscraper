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


void solve(std::ifstream& in, std::ofstream& out) {
	int T;
	in >> T;
	int t{ 1 };

	while (t <= T) {
		int K, C, S;
		in >> K >> C >> S;
		
		out << "Case #" << t << ": ";
		
		for (int64_t i = 1; i <= K; i++) {
			int64_t pos = i;
			out << pos << " ";
		}
		out << std::endl;
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