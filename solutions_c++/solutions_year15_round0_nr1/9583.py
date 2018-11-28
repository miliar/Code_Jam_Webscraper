#include <cstdio>

const int MAX_S = 1005;

int S;
char shyness[MAX_S];

void solve_case(int test_case) {
	scanf("%d %s", &S, shyness);
	int people = 0, invite = 0;

	for (int i = 0; i <= S; i++) {
		int current = shyness[i] - '0';

		if (people < i) {
			invite += i - people;
			people = i;
		}

		people += current;
	}

	printf("Case #%d: %d\n", test_case, invite);
}

int main() {
	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		solve_case(tc);
	}

	return 0;
}