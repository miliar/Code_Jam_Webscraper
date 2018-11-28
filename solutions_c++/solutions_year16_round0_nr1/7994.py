#include <stdio.h>

int pow(int i) {
	if (i == 0)
		return 1;
	
	return 10 * pow(i - 1);
}

int num_counts(int n) {
	for (int i=1; ; i++) {
		if (n / pow(i) == 0) {
			return i;
		}
	}
}

int main() {
	int c;
	scanf("%d", &c);
	for (int t = 0; t < c; t++) {
		int i;
		scanf("%d", &i);
		{
			int set[10] = { 0, };
			int count = 0;
			bool suc = false;
			int j;
			for (j = 1; j <= 10000; j++) {
				int r = i*j;

				for (int k = 0; k < num_counts(r); k++) {
					int n = (r / pow(k)) % 10;
					if (set[n] == 0) {
						set[n] = 1;
						count++;
						if (count == 10) {
							suc = true;
							break;
						}
					}
				}

				if (suc)
					break;

			}

			if (suc) {
				printf("Case #%d: %d\n", t+1, i*j);
			}
			else {
				printf("Case #%d: INSOMNIA\n", t+1);
			}
		}
	}
}