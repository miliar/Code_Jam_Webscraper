#include <iostream>
#include <cstring>

using namespace std;

void checkN(long long N, bool isSeen[10]) {
	if (N == 0) {
		isSeen[0] = true;
		return;
	}

	while (N > 0) {
		int lastDigit = N % 10;
		N /= 10;
		isSeen[lastDigit] = true;
	}
}

bool checkNumbersSeen(bool isSeen[10]) {
	for (int i = 0; i < 10; i++) {
		if (!isSeen[i]) {
			return false;
		}
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long N;
		cin >> N;

		bool isSeen[10];
		memset(&isSeen[0], false, 10);

		long long lastN = N;
		int i = 1;
		for (; i <= 100; i++) {
			lastN = N * i;
			checkN(lastN, isSeen);
			if (checkNumbersSeen(isSeen)) {
				
				break;
			}
		}

		if (i == 101) {
			std::cout << "Case #" << t << ": INSOMNIA" << endl;
		} else {
			std::cout << "Case #" << t << ": " << lastN << endl;
		}
		
	}
}