#define _CRT_SECURE_NO_WARNINGS

#include <cstring>
#include <algorithm>

bool check(bool arr[]) {
	for (int i = 0; i < 10; i++) {
		if (!arr[i])
			return false;
	}

	return true;
}

int main(void) {
	int n;
	scanf("%d", &n);
	FILE * fp = fopen("output.txt", "w");

	for (int i = 1; i <= n; i++) {
		long x;
		scanf("%d", &x);

		bool output[10] = { 0 };
		memset(&output, 0, sizeof(output));
		
		int k = 0;
		bool result = false;
		while (!result && x > 0) {
			long a = x * (++k);
			while (a >= 1) {
				output[a % 10] = true;
				a /= 10;
			}
			result = check(output);
		}

		

		fprintf(fp, "Case #%d: ", i);

		if (result)
			fprintf(fp, "%ld\n", x * k);
		else
			fprintf(fp,"INSOMNIA\n");
	}

	return 0;
}