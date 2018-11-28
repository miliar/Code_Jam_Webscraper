#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
	int numTests;
	cin >> numTests;
	int i, j;
	long n;
	for (i = 1; i <= numTests; i++) {
		bool used[11] = {false};
		cin >> n;
		long m = n;
		if (n == 0) {
			cout << "Case #";
			cout << i;
			cout << ": INSOMNIA\n";
		}
		else {
			while (true) {
				// cout << "N: ";
				// cout << n << endl;
				// cout << "M: ";
				// cout << m << endl;
				used[n%10] = true;
				int tmp = n;
				while (tmp/10 != 0) {
					tmp /= 10;
					used[tmp%10] = true;
				}
				bool allUsed = true;
				for (j = 0; j < 10; j++) {
					if (!used[j]) {
						allUsed = false;
						break;
					}
				}
				if (allUsed) {
					cout << "Case #";
					cout << i;
					cout << ": ";
					cout << n << endl;
					break;
				}
				n += m;
				// cout << "=======\n";
			}
		}
	}
	return 0;
}