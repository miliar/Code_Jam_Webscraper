#include <cstdio>
#include <cstring>
#include <iostream>

#define FALL_ASLEEP 0x3FF

using namespace std;

int bits[10] = {
	0x001, 0x002, 0x004, 0x008, 0x010,
	0x020, 0x040, 0x080, 0x100, 0x200,
};

int main(int argc, char** argv) {
	int T;
	int test_case;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
		int N;
		scanf("%d", &N);
		
		printf("Case #%d: ", test_case);
		if (N == 0) {
			printf("INSOMNIA\n");
		}
		else {
			int flag = 0;
			int last = 0;
			while (flag != FALL_ASLEEP) {
				last += N;
				for (int n = last; n > 0; n /= 10)
					flag |= bits[n % 10];
			}
			printf("%d\n", last);
		}
	}

	return 0;
}