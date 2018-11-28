#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
	int T;
	scanf("%d", &T);

	for (int w = 0; w < T; w++) {
		int N;
		scanf("%d", &N);

		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", w + 1);
			continue;
		}

		int cnt = 1, cur = N;
		int digit[12] = { 0, };
		char buf[200];
		while (true) {
			sprintf(buf, "%d", cur);

			for (int i = 0; i < strlen(buf); i++) {
				digit[buf[i] - '0'] = 1;
			}

			bool flag = true;
			for (int i = 0; i < 10; i++) {
				if (!digit[i]) {
					flag = false;
					break;
				}
			}
			if (flag)
				break;

			cnt++;
			cur += N;
		}

		printf("Case #%d: %d\n", w + 1, cur);


	}

	return 0;
}