#include<stdio.h>

bool check[10];

bool check_num(long long int x){
	while (x != 0){
		check[x % 10] = true;
		x /= 10;
	}
	for (int i = 0; i < 10; i++)if (check[i] == 0)return false;
	return true;
}
int main(){
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
	long long int T, N, i;
	scanf("%lld", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%lld", &N);
		for (int i = 0; i < 10; i++)check[i] = 0;
		if (N == 0){
			printf("INSOMNIA\n");
			continue;
		}
		for (i = N; !check_num(i); i += N);
		printf("%lld\n", i);
	}
	return 0;
}