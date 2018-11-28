#include <stdio.h>

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d",&test);

	for(int t=1; t<=test; t++) {
		long long n;
		scanf("%lld",&n);

		if(n==0) {
			printf("Case #%d: INSOMNIA\n",t);
			continue;
		}

		bool done = false;
		int dig[10] = {0};
		long long temp = n;
		while(!done) {
			long long tmp = n;
			//printf("%lld\n",tmp);
			while(tmp>0) {
				dig[tmp%10]++;
				tmp/=10;
			}
			done = true;
			for(int i=0; i<10; i++) {
				if(dig[i]<=0) done = false;
			}

			if(done) break;
			n += temp;
			if(n<0) break;
		}
		if(done)
			printf("Case #%d: %lld\n",t,n);
		else 
			printf("Case #%d: INSOMNIA\n",t);
	}
	return 0;
}