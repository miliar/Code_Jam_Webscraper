#include <cstdio>

void count(int k) {
	if (k == 0) {
		printf("INSOMNIA\n");
		return;
	}
	bool seen[10];
	int nbSeen = 0, total = 0;
	for (int i = 0; i < 10; i++)
		seen[i] = false;
	while (nbSeen < 10) {
		total += k;
		int p = total;
		bool print = false;
		while (p != 0) {
			if (seen[p%10] == false) {
				seen[p%10] = true;
				nbSeen++;
			}
			p /= 10;
		}
		if (nbSeen == 10)
			printf("%d\n", total);
	}
}

int main(void) {
	int nbTests;
	scanf("%d", &nbTests);
	for (int i = 1; i <= nbTests; i++) {
		int p;
		scanf("%d", &p);
		printf("Case #%d: ", i);
		count(p);
	}
	return 0;
}
	
