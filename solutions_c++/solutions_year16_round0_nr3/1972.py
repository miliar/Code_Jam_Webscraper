#include<stdio.h>
#include<string.h>
FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");
#define Limit 2000
int N, K,cnt=0, L = Limit;
char D[100];

int dfs(int x) 
{
	if (x == 0) {
		int i, j, k = 1, sum = 0, temp = 1, b;
		int A[14] = { 0, };
		for (b = 2; b <= 10; b++) {

			for (j = 2; j<L; j += 2) { // j 인자로 D가 나뉘어지는지 확인
				sum = 0; temp = 1;
				for (i = N - 1; i >= 0; i--) {
					if (D[i] == '1') {
						sum += temp;
						sum %= j;
					}
					temp = (temp*b) % j;
				}
				if (sum == 0) {
					A[b] = j;
					break;
				}
				if (j == 2) j++;
			}

			if (sum != 0) break;
		}
		if (sum == 0) {
			fprintf(out,"%s ", D); // 정답 출력
			for (i = 2; i <= 10; i++) {
				fprintf(out, "%d ", A[i]);
			}
			K--;
			fprintf(out, "\n");
		}
		return 0;
	}
	D[x] = '1';
	if(K!=0) dfs(x - 1);
	D[x] = '0';
	if(K!=0) dfs(x - 1);
	return 0;
}

int A()
{
	fscanf(in,"%d%d", &N, &K);
	D[0] = '1'; D[N - 1]='1';

	int i;
	for (i = 1; i < N - 1; i++) {
		D[i] = '0';
	}
	
	dfs(N-2);
	


	return 0;
}

int main()
{
	int T,i=1; fscanf(in,"%d",&T);

	while (T--) {
		fprintf(out,"Case #%d: \n",i++);
		A();
	}

	return 0;
}