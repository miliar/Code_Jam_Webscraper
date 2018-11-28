#include<stdio.h>

long long number,ans;
int t, n,flag,num;
int visited[10];
int main() {
	scanf("%d", &t);
	for (int k = 1; k <= t;k++) {
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", k);
			continue;
		}
		for (int i = 1; i <= 987654321;i++){
			ans=number = (long long)n*i;
			while (number) {
				num=number % 10;
				number /= 10;
				visited[num] = 1;
			}
			flag = 0;
			for (int i = 0; i <= 9; i++)
				if (visited[i] == 0) {
					flag = 1; break;
				}
			if (flag == 0) {
				printf("Case #%d: %lld\n", k, ans);
				break;
			}
		}
		for (int i = 0; i <= 9; i++)visited[i] = 0;
	}
	return 0;
}