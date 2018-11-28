#include <stdio.h>

int prime[100000];
long long len = 0;

void initPrim() {
	for (long long i = 3; i < 100000; i += 2 ) {
		long long j;
		for (j = 2; j*j <= i; ++j) {
			if (i%j == 0) {
				break;
			}
		}
		if (j*j > i) prime[len++] = j;
	}
}

long long verify(long long v) {
	for (long long i = 0; i < len; ++i) {
		if (prime[i] < v && v%prime[i] == 0)  return prime[i];
	}
	return 0;
}

long long getNum(long long v,long long base) {
	long long n = 1;
	long long res = 0;
	while (v) {
		res += (v%2)*n;
		n*=base;
		v/=2;
	}	
	return res;
}

void enumerate(int w, int v) {
	
	//prlong longf("%d\n",getNum(5,2));
	for (long long i = w; i <= w; ++i) {
		long long num = 0;
		long long one = 1;
		//printf("------%I64d %I64d\n", i, one<<(i-1) );
		for (long long j = (one<<(i-1))+1; j < (one<<i); j += 2) {
			long long isok = 1;
			//printf("------%d\n",i);
			for (long long k = 2; k <= 10; ++k) {
				long long val = getNum(j,k);
				long long num = verify(val);
				if (num == 0) {
					isok = 0;
					break;
				}
			}
			if (isok) {
				for (long long d = w-1; d >= 0; --d) {
					if ( (one << d) & j) {
						printf("1");
					}
					else {
						printf("0");
					}
				}
				for (int d = 2; d <= 10; ++d) {
					long long val = getNum(j,d);
					printf(" %lld", verify(val)); 
				}
				printf("\n");
				num++;
				if (num >= v) {
					break;
				}
			}
			
		}
	}
}

int main() {
	initPrim();
	int n;
	freopen("C-small-attempt3.in","r",stdin);
	freopen("C-small-attempt3.out","w",stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		int w, v;
		scanf("%d %d",&w,&v);	
		printf("Case #%d:\n",i+1);
		enumerate(w,v);	
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
