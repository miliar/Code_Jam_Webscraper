#include <stdio.h>
#include <cstring>
using namespace std;

void fill(bool* done, unsigned long long num) {
	while (num) {
		done[num%10] = 1;
		num /= 10;
	}
}

int main() {
	int T;
	int N;
	bool done[10];

	scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		memset(done, 0, sizeof(done));

		if (!N) {
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}

		unsigned long long val = N;

		for (unsigned long long i = 1; ; ++i) {
			fill(done, i*val);
			int k;
			for (k=0;k<10;++k) {
				if (!done[k]) break;
			}
			if (k==10) {
				printf("Case #%d: %llu\n", t, i*val);
				break;
			}
		}
	}

}