#include<stdio.h>

int T, p, N, A[2000], cnt, aud,i;
char C[2000];

int main(){
	freopen("input.txt", "r", stdin),freopen("output.txt","w",stdout);
	scanf("%d", &T);
	for (p = 1; p <= T; p++){
		scanf("%d %s", &N, C);
		for (i = 0; i <= N; i++)A[i] = C[i] - '0';
		cnt = 0;
		aud = A[0];
		for (i = 1; i <= N; i++){
			if (aud < i){
				cnt += (i - aud);
				aud = i;
			}
			aud += A[i];
		}
		printf("Case #%d: %d\n", p, cnt);
	}
	return 0;
}