#include <cstdio>

int N, P;

int calc1(int x, int n){
	if(x == 0) return 1;
	return (n / 2 + calc1((x - 1) / 2, n / 2));
}
int calc2(int x, int n){
	if(x == n- 1) return n;
	int rest = n - x - 1;
	return calc2(n/2 - (rest-1)/2 - 1, n / 2);
}

int main(){
	for(int t = 1, T, zzz = scanf("%d", &T); t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%d %d", &N, &P);
		int a, b;
		for(int i = 0, ii = (1 << N); i < ii; i++){
			if(calc1(i, (1 << N)) <= P){
				a = i;
			}
			if(calc2(i, (1 << N)) <= P){
				b = i;
			}
		}
		printf("%d %d\n", a, b);
	}
	return 0;
}
