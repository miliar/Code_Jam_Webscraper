#include<stdio.h>
char aa[1001];
char ans[2100];
int front, rear;
int main() {
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		printf("Case #%d: ",i);
		scanf("%s", aa);
		front = 1000;
		rear = 1001;
		ans[front--] = aa[0];
		for (int j = 1; aa[j]; j++) {
			if (ans[front +1] <= aa[j]) {
				ans[front--] = aa[j];
			}
			else ans[rear++] = aa[j];
		}
		for (int j = front + 1; ans[j]; j++) {
			printf("%c", ans[j]);
			ans[j] = 0;
		}
		printf("\n");
	}
	return 0;
}