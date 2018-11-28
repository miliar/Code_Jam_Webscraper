#include <stdio.h>
#include <string.h>
using namespace std;

void print(int * a, int len) {
	for (int i = len -1; i >= 0; i--) {
		printf("%d", a[i]);
	}
	for (int i = 2; i <= 10; i++) {
		printf(" %d", i + 1);
	}
	printf("\n");
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int n, J;
		scanf("%d %d", &n, &J);
		int a[40];
		memset(a, 0, sizeof(a));
		int count = 0;
		printf("Case #%d:\n", t + 1);
		a[0] = a[1] = a[n - 2] = a[n - 1] = 1;
		print(a, n);
		count++;
		for (int i = 2; i + 1 < n - 2 && count < J; i++) {
			a[i] = a[i + 1] = 1;
			print(a, n);
			a[i] = a[i + 1] = 0;
			count++;
		}
		for (int i = 2; i + 1 < n - 2 && count < J; i++){
			a[i] = a[i + 1] = 1;
			for (int j = i + 2; j + 1 < n - 2 && count < J; j++) {
				a[j] = a[j + 1] = 1;
				print(a, n);
				a[j] = a[j + 1] = 0;
				count++;
			}
			a[i] = a[i + 1] = 0;
		}
		for (int i = 2; i + 3 < n - 2 && count < J; i++){
			a[i] = a[i + 1] = a[i + 2] = a[i + 3] = 1;
			for (int j = i + 4; j + 1 < n - 2 && count < J; j++) {
				a[j] = a[j + 1] = 1;
				print(a, n);
				a[j] = a[j + 1] = 0;
				count++;
			}
			a[i] = a[i + 1] = a[i + 2] = a[i + 3] = 0;
		}
	}
}