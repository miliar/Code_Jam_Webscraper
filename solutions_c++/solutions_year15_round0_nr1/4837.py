#include <stdio.h>
#include <string.h>

int numTestCases = 0, kase = 0;

int handleQ(int au, char* shy) {
	int i = 0, j = 0, need = 0;
	int tot = shy[0]-'0';

	for (i = 1; i <= au; i++) {
		fprintf(stderr, "%d", shy[i]-'0');
		if (i > tot) {
			need += (i-tot);
			tot += (i-tot);
		}
		tot += shy[i]-'0';
	}
	fprintf(stderr, "\n");
	return need;
}

int main() {
	int au = 0, result = 0;
	char shy[1010] = {0};

	scanf("%d", &numTestCases);

	for (kase = 0; kase < numTestCases; kase++) {
		scanf("%d %s", &au, shy);

		result = handleQ(au, shy);

		printf("Case #%d: %d\n", kase+1, result);

		memset(shy, 0, sizeof(shy));
	}
}