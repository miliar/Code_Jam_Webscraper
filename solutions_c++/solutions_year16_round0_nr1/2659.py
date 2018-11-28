#include <cstdio>

int T;
int N;

int main(){
	int i;

	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++){
		scanf("%d", &N);

		if(N == 0)
			printf("Case #%d: INSOMNIA\n", tt);
		else {
			bool chk[10];
			int ct = 0;
			for(int i = 0; i <= 9; i++)
				chk[i] = false;

			int mul;
			for(mul = 1;; mul++){
				int temp = N * mul;
				while(temp > 0){
					if(!chk[temp % 10]){
						chk[temp % 10] = true;
						ct++;
					}
					temp /= 10;
				}
				if(ct == 10)break;
			}

			printf("Case #%d: %d\n", tt, N*mul);
		}
	}
}