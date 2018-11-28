#include<stdio.h>

void process() {
	int N; scanf("%d", &N);
	int arr[11] = { 0, };
	int cnt = 10;

	int i;
	for (int i = 1; i < 101; i++) {
		int t = N*i;
		while (t) {
			if (arr[t % 10] == 0) {
				arr[t % 10] = 1;
				cnt--;
			}
			t /= 10;
		}
		if (cnt == 0) {
			printf("%d", N*i);
			return;
		}
	}
	printf("INSOMNIA");
	

}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int testcase; scanf("%d", &testcase);

	for (int i = 0; i < testcase; i++) {
		printf("Case #%d: ",i+1);
		process();
		printf("\n");
	}
	return 0;
}