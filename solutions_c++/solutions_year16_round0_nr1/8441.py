#include <iostream>
#include <set>
#include <cassert>


using namespace std;

void GetDigits(unsigned long long n, set<unsigned long long>& digits) {
	do {
		auto d = n % 10;
		if (digits.find(d) == digits.end()) {
			digits.insert(d);
		}
		n = n / 10;
	} while (n > 0);
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 1; i <= numCases; ++i) {
		unsigned long long n = 0;
		cin >> n;

		cout << "Case #" << i << ": ";
		if (n == 0) {
			cout << "INSOMNIA";
		}
		else {
			set<unsigned long long> digits;
			auto answer = n;
			unsigned long long mul = 1;
			do {
				answer = n * (mul++);
				GetDigits( answer, digits );
				assert((n * mul) < (n * (mul + 1)));
			} while (digits.size() < 10);

			cout << answer;
		}

		cout << endl;
	}

    return 0;
}

