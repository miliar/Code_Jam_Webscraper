#include<stdio.h>
#include<string.h>

int check[10];

bool isCheck(){
	for (int i = 0; i < 10; i++){
		if (check[i] != 1)
			return false;
	}
	return true;
}
void solve(FILE *fp){
	memset(check, 0, sizeof(check));

	long long N;
	scanf("%lld", &N);

	if (N == 0){
		fprintf(fp,"INSOMNIA\n");
		return;
	}
	int i = 1;
	while (1){
		long long tmp = N*i;
		while (tmp > 0){
			int rest = tmp % 10;
			tmp = tmp / 10;
			check[rest] = 1;
		}
		if (isCheck())
			break;
		i++;
	}
	fprintf(fp,"%lld\n", i*N);
}
int main(void){
	FILE *fp;
	fp = fopen("output.txt", "w");
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++){
		fprintf(fp,"Case #%d: ", i + 1);
		solve(fp);
	}
}