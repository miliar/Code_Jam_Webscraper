#include <cstdio>
#include <cstring>

using namespace std;

void solve(int case_num) {
	int N;
	int mult = 1;
	int visited_cnt = 0;
	int sol;
	bool visited[10] = {false};

	scanf("%d", &N);
	printf("Case #%d: ", case_num);

	if (N != 0) {
		while (visited_cnt != 10) {
			sol = mult * N;
			int tmp = sol;

			while (tmp) {
				int digit = tmp % 10;

				if (!visited[digit]) {
					visited[digit] = true;
					++visited_cnt;
				}

				tmp /= 10;
			}

			++mult;
		}

		printf("%d\n", sol);
	}
	else {
		printf("INSOMNIA\n");
	}
}

int main(void) {

	int T;

	scanf("%d", &T);

	for (int i = 0; i < T; ++i) {
		solve(i + 1);
	}

	return 0;
}