#define A
#ifdef A
#include <iostream>
#include <cstdint>

using namespace std;

uint16_t getMask(uint64_t num) {
	uint16_t mask = 0;
	while (num > 0) {
		mask |= (1 << (num % 10));
		num /= 10;
	}
	return mask;
}

uint64_t lastNumber(uint64_t num) {
	if (!num) return num; // 0 case
	uint16_t results = 0;
	uint16_t good = 0b1111111111;

	uint64_t currNum = 0;
	do {
		currNum += num;
		results |= getMask(currNum);
	} while (results != good);

	return currNum;
}

int main() {
	int cases;
	uint64_t trial;

	cin >> cases;
	for (int i = 1; i <= cases; i++) {
		cin >> trial;
		uint64_t end = lastNumber(trial);

		cout << "Case #" << i << ": ";
		if (end == 0)
			cout << "INSOMNIA";
		else
			cout << end;

		cout << endl;
	}

	return 0;
}

#endif