#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#pragma warning(disable : 4996)


int main(){

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T, B;
	long long int M;
	scanf("%d", &T);
	for (int Q = 1; Q <= T; Q++){
		scanf("%d %lld", &B, &M);
		printf("Case #%d: ", Q);
		int map[55][55] = { 0, };
		long long int max=1;
		for (int i = 1; i <= B - 2; i++)
			max *= 2;
		if (M > max)
			printf("IMPOSSIBLE\n");
		else{
			for (int i = 0; i < B; i++){
				for (int j = i; j < B; j++){
					map[i][j] = 1;
					if (i == j)
						map[i][j] = 0;
				}
			}
			long long int temp = max-M;
			int B_temp = 1;
			while (temp != 0){
				if (temp % 2 == 1){
					map[B_temp][B-1] = 0;
				}
				B_temp++;
				temp /= 2;
			}
			printf("POSSIBLE\n");
			for (int i = 0; i < B; i++){
				for (int j = 0; j < B; j++)
					printf("%d", map[i][j]);
				printf("\n");
			}
		}
	}
	return 0;
}
	