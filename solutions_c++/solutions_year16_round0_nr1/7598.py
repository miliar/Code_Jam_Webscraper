#include <stdio.h>
#include <iostream>
#include <bitset>
using namespace std;

int main() {

	FILE *fp = fopen("input.in", "r");
	if (!fp) {
		cout << "Cant open file" << endl;
		return 0;
	}

	int nTests = 0;
	fscanf(fp, "%d", &nTests);

	for (int i = 0; i < nTests; ++i) {
		long long num = 0;
		fscanf(fp, "%lld", &num);

		bitset<10> set;

		if (num == 0) {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}

		long long val = num;
		int counter = 1;
		do {
			if (val <= 9) {
				set.set(val, true);

			} else {
				int tmp = val;
				do {
					int dig = tmp % 10;
					if (!set[dig])
						set.set(dig, true);
					tmp /= 10;
				} while (tmp > 0);
			}
			if (set.all())
				break;
			++counter;
			val = num * counter;
		} while (true);

		cout << "Case #" << i + 1 << ": " << val << endl;
	}
	return 0;
}

