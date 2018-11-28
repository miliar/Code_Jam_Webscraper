#include <iostream>
#include <string>
#include <set>

using namespace std;

string solve(long N) {
	if (N == 0)
		return "INSOMNIA";

	set<char> seen;
	string product = "";

	for (long i = 1; seen.size() < 10; i++) {
		product = to_string(i * N);
		for (auto c : product) {
			seen.insert(c);
		}
	}
	return product;
}

int main() {
	int T;
	cin >> T;

	for (int t = 0; t < T; t++) {
		long N;
		cin >> N;
		cout << "Case #" << t+1 << ": " << solve(N) << endl;
	}

	return 1;
}
