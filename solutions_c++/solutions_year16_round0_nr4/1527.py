#include <iostream>

using namespace std;

int64_t getNumber(int64_t i, int64_t k, int64_t c)
{
	int64_t sum = 0;
	int64_t base = 1;
	for (int j=0; j<c; ++j) {
		sum += i*base;
		base *= k;
	}
	return sum + 1;
}

void compute(int k, int c)
{
	for (int i=0; i<k-1; ++i) {
		cout << getNumber(i, k, c) << " ";
	}
	cout << getNumber(k-1, k, c);
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; ++i) {
		int k; int c; int s;
		cin >> k;
		cin >> c;
		cin >> s;
		if (k==s) {
			cout << "Case #" << i+1 << ": ";
			compute(k, c);
			cout << endl;
		}
	}
}