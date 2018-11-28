#include <stdio.h>
#include <set>
using namespace std;

int digits[10];
int count = 0;

void split(int n) {
	while (n > 0) {
		int key = n % 10;
		n /= 10;
		if (digits[key]++ == 0)
			++count;
	}
}

int main() {
	int T, n;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		scanf("%d", &n);

		for (int i = 0; i < 10; ++i)
			digits[i] = 0;
		count = 0;

		set<int> nums;
		bool findIt = true;
		int now = 0;
		while (true) {
			now += n;
			if (nums.find(now) != nums.end()) {
				findIt = false;
				break;
			}
			nums.insert(now);
			split(now);
			if (count >= 10)
				break;
		}

		if (findIt)
			printf("Case #%d: %d\n", t, now);
		else
			printf("Case #%d: INSOMNIA\n", t);

	}

	return 0;
}