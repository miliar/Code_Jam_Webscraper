#include<iostream>

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("c.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int a = 1; a <= T; a++){
		int num = 0;
		int I[10];
		long long int N;
		scanf("%lld", &N);
		if (N == 0){
			printf("Case #%d: INSOMNIA\n", a);
			continue;
		}
		for (int k = 0; k < 10; k++){
			I[k] = -1;
		}
		long long int M, answer;
		int b = 1;
		while (1){
			M = N * b;
			answer = M;
			while (M >= 10){
				int temp = M % 10;
				if (I[temp] == -1){
					I[temp] = 1;
					num++;
				}
				M = M / 10;
			}
			if (I[M] == -1){
				I[M] = 1;
				num++;
			}
			if (num == 10){
				break;
			}
			b++;
		}
		printf("Case #%d: %lld\n", a, answer);
	}

}