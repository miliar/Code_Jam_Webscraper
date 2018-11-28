#include <iostream>
#include <bitset>

using namespace std;

int main(int argc, char const *argv[]) {
	int nTestCases;
	cin >> nTestCases;

	for (int i = 0; i < nTestCases; ++i) {
		unsigned long long int n;
		cin >> n;

		if (n == 0) {
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
			continue;				
		} 

		int k = 0;
		bitset<10> exists;
		while (exists.count() < 10) {
			k++;
			unsigned long long int temp = n*k;
			while (temp > 0) {
				int digit = temp % 10;
				exists.set(digit, 1);
				temp /= 10;
			}
		}

		cout << "Case #" << i+1 << ": " << n*k << endl;	
	}

	return 0;
}