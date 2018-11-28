#include <cstdio>

long long run(int n){
	int i = 1;
	int vis = 0;
	while (true){
		long long r = (long long) n * i;
		while (r){
			vis |= 1<<(r%10);
//			printf("%d %d\n", r, vis);
			r /= 10;

		}
		if (vis == 1023){
			return n*i;
		}
		i++;
		if (i > 100000){
			break;
		}
	}
	return -1;
}

int main(){

/*
	for (int i=0; i<=1000000; i++){
		if (run(i)==-1)
		printf("%d %d\n", i, run(i));
	}
	return 0;
*/

	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++){
		int n;
		scanf("%d", &n);

//		printf("yo %d\n", n);
		long long ans = run(n);	
		printf("Case #%d: ", t);
		if (ans == -1){
			printf("INSOMNIA\n");
		}else{
			printf("%lld\n", ans);
		}
	}
	return 0;
}
