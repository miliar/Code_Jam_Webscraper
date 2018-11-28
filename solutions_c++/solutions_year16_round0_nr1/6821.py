#include <iostream>
#include <set>
using namespace std;

int parseDigits(int number, set<int>& digits) {
	while (number > 0) {
		digits.insert(number % 10);
		number /= 10;
	}
}

int processCase(int N) {
	if (N == 0)
		return -1;
	set<int> digits;
	int last = 0;
	while (digits.size() < 10) {
		last += N;
		parseDigits(last, digits);
	}
	return last;
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	int N;
	int highest;
	for (int c = 0; c < T; ++c) {
		cin >> N;
		highest = processCase(N);
		cout << "Case #" << c + 1 << ": ";
		if (highest == -1)
			cout << "INSOMNIA" << endl;
		else 
			cout << highest << endl;
	}
	return 0;
}