#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

#define TYPE string
#define f(i, N) for(unsigned i = 0; i < N; ++i)
#define fr(i, N) for(int i = N-1; i >= 0; --i) // reverse
#define ff(i, j, N) for(unsigned i = 0; i < N; ++i) for(unsigned j = 0; j < N; ++j)
#define V vector<TYPE>


int solve(TYPE input)
{
	int count = 0;
	char last = input[0];
	for (auto c : input) {
		if (last != c) {
			++count;
			last = c;
		}
	}
	if (input.back() == '-') ++count;
	return count;
}

int main() {
	unsigned T;
	TYPE N;
	cin >> T;
	f(t, T) {
		cin >> N;
		try {
			cout << "Case #" << t + 1 << ": " << solve(N) << endl;
		}
		catch (const std::exception& e) {
			cout << e.what() << endl;
		}
		catch (...) {
			cout << "Unknown exception" << endl;
		}
	}
}