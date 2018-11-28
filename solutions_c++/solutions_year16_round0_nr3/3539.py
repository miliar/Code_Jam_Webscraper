#include<iostream>

int N, J;
int arr[40];
long long int base[11];
long long int divisor[11];
int mult[11];


int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("d.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d:\n", T + 1);
		long long int S = 1;
		scanf("%d %d", &N, &J);
		for (int i = 0; i < N-1; i++){
			S *= 2;
		}
		S += 1;
		long long int now = S;
		int num = 0;
		while (num < J){
			int j = 0;
			long long int temp = now;
			while (temp > 1){
				arr[N - j - 1] = temp % 2;
				temp /= 2;
				j++;
			}
			arr[0] = temp;
			int flag = 0;
			for (int k = 2; k < 11; k++){
				if (k != 2){
					base[k] = 0;
					for (int l = 0; l < N; l++){
						base[k] = base[k] * k + arr[l];
					}
				}
				else{
					base[2] = now;
				}
				long long int l;
				for (l = 2; l*l <= base[k]; l++){
					if (base[k] % l == 0){
						divisor[k] = l;
						break;
					}
				}
				if (l*l > base[k]){
					flag = 1;
					break;
				}
			}
			if (flag != 1){
				for (int a = 0; a <N; a++){
					printf("%d", arr[a]);
				}
				for (int a = 2; a < 11; a++){
					printf(" %lld", divisor[a]);
				}
				num++;
				printf("\n");
			}
			now += 2;
		}
	}
}