#include <cstdio>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int s_max;
		scanf("%d", &s_max);
		int needed = 0, current = 0;
		for (int i = 0; i <= s_max; i++) {
			char count_digit;
			scanf(" %c", &count_digit);
			int count = count_digit - '0';
			while (current < i) {
				needed++;
				current++;
			}
			current += count;
		}
		printf("Case #%d: %d\n", t, needed);
	}
	return 0;
}
