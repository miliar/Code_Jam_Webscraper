#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

#define TYPE long long
#define f(i, N) for(unsigned i = 0; i < N; ++i)
#define fr(i, N) for(int i = N-1; i >= 0; --i) // reverse
#define ff(i, j, N) for(unsigned i = 0; i < N; ++i) for(unsigned j = 0; j < N; ++j)
#define V vector<TYPE>

void count(set<int>& d, TYPE input) {
	while (input > 0) {
		d.insert(input % 10);
		input /= 10;
	}
}

TYPE solve(TYPE input)
{
	set<int> digits;
	TYPE current = 0;
	do {
		current += input;
		count(digits, current);
	} while (digits.size() < 10);
	return current;
}

int main() {
	unsigned T;
	TYPE N;
	cin >> T;
	f(t, T) {
		cin >> N;
		try {
			cout << "Case #" << t + 1 << ": ";
			if (N == 0) cout << "INSOMNIA" << endl;
			else        cout << solve(N) << endl;
		}
		catch (const std::exception& e) {
			cout << e.what() << endl;
		}
		catch (...) {
			cout << "Unknown exception" << endl;
		}
	}
}