#include <cstdio>
#include <cstdlib>

int nb[1002];

int main(void) {
	int nbTests;
	scanf("%d", &nbTests);
	for (int iTest = 1; iTest <= nbTests; iTest++) {
		int k;
		scanf("%d", &k);
		getchar();
		for (int i = 0; i <= k; i++)
			nb[i] = getchar()-'0';
		int standing = 0, add = 0;
		for (int i = 0; i <= k; i++) {
			if (standing < i) {
				add += i-standing;
				standing = i;
			}
			standing += nb[i];
		}
		printf("Case #%d: %d\n", iTest, add);
	}
	return 0;
}
