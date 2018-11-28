#include<stdio.h>
#include<stdlib.h>
#pragma warning(disable : 4996)
int main(){
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		int N, j = 1, temp;
		int num[10] = { 0, };
		scanf("%d", &N);
		if (N == 0)
			printf("Case #%d: INSOMNIA\n", i);
		else{
			while (1){
				temp = j*N;
				while (temp > 0){
					num[temp % 10]++;
					temp /= 10;
				}
				int cnt = 0;
				for (int k = 0; k < 10; k++){
					if (num[k] != 0)
						cnt++;
				}
				if (cnt == 10)
					break;
				j++;
			}
			printf("Case #%d: %d\n", i, j*N);
		}
	}
	return 0;
}