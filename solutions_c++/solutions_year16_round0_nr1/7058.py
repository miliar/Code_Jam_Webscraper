#include <stdio.h>
#include <string.h>

int resolve(int num) {
	if (num == 0) return -1;
	int cont = 0x3FF;
	int t, tmp_num, r;
	t = num;
	while (cont) {
		tmp_num = t;
		while (tmp_num && cont) {
			r = tmp_num % 10;
			tmp_num /= 10;
			cont = cont & (~(1<<r));
		}
		if (cont) t += num;
	}
	return t;
}

int main() {
	int T, idx = 0, num = 0;
	scanf("%d", &T);
	while (idx < T) {
		scanf("%d", &num);
		// printf("%s\n", stack);
		int res = resolve(num);
		if (res == -1) {
			printf("Case #%d: INSOMNIA\n", idx+1);
		} else {
			printf("Case #%d: %d\n", idx+1, res);
		}
		++idx;
	}

	return 0;
}