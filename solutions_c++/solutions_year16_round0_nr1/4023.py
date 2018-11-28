#include <iostream> 
#include <stdlib.h>

using namespace std;

bool f[10];
int c = 0;

void mark(long x) {
	while (x > 0) {
		long p = x % 10;
		if (!f[p]) {
			++c;
			f[p] = true;
		}
		x /= 10;
	}
}

int main() {
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		long n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << "\n";
			continue;
		}
		
		for (int j = 0; j < 10; j++) {
			f[j] = false;
		}
		c = 0;

		long result;
		result = n;
		while (1) {
			mark(result);
			if (c == 10) {
				break;
			} else {
				result += n;
			}
		}

		cout << "Case #" << i + 1 << ": " << result << "\n";
	}
	return 0;
}