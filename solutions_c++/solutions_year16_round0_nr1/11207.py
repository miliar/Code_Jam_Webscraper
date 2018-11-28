#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

void
addDigits(vector<int>* digits, unsigned long int n, int* count)
{
	while (n > 0) {
		int d = n % 10;
		n = n/10;
		if ((*digits)[d] == 0) {
			(*count)++;
			(*digits)[d] = 1;
		}
	}
}

void
checkNum(unsigned long int n, int i)
{
	if (n == 0) {
    cout << "Case #" << i << ": " << "INSOMNIA" << endl;
	} else {
		vector<int> digits(10, 0);
		int count = 0;
		unsigned long int name = n;
		for (int g = 1; count < 10; ++g) {
			n = name*g;
			addDigits(&digits, n, &count);
			//cout << "n: " << n << endl;
			//for (auto const& c : digits) cout << c << ' ';
		}
    cout << "Case #" << i << ": " << n << endl;

	}
}

int main() {
  int t;
	unsigned long int n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
		checkNum(n, i);
  }

	return 0;
}
