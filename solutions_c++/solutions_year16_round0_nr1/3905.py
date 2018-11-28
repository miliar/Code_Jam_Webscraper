#include <cstdio>

bool flag[10];

bool check(long long unsigned N)
{
	while(N != 0) {
		flag[N % 10] = true;
		N /= 10;
	}

	for(int i = 0; i < 10; ++i) {
		if(flag[i] == false)
			return false;
	}

	return true;
}

int main()
{
	int T;

	scanf(" %d", &T);
	for(int caseId = 1; caseId <= T; ++caseId) {
		long long unsigned N;

		scanf(" %llu", &N);

		if(N == 0) {
			printf("Case #%d: INSOMNIA\n", caseId);
			continue;
		}

		for(int i = 0; i < 10; ++i) {
			flag[i] = false;
		}

		for(long long unsigned i = 0; i < 0xFFFFFFFFFFFFFFFF; ++i) {
			if(check(N * i)) {
				printf("Case #%d: %llu\n", caseId, N * i);
				break;
			}
		}
	}

	return 0;
}
