#include <bits/stdc++.h>
using namespace std;

int  main() {
	long long int  t,c,n;
	scanf("%lld", &t);

	for(long long int  k=1; k<=t; k++) {
		long long int  a[12];
		memset(a, 0, sizeof(a));
		scanf("%lld", &n);

		if(n==0) {
			printf("Case #%lld: INSOMNIA\n", k);
			continue;
		}
		long long int  f=0,ind=2;
		long long int  num=n,ans=0;
		while(1) {
			ans=num;
			while(num) {
				a[num%10]=1;
				num/=10;
			}
			c=0;
			for(long long int  i=0; i<10; i++) {
				if(a[i]==1)	c++;
			}
			if(c==10) {
				f=1;
				break;
			}
			num = ind*n;
			ind++;
		}
		if(f==1) {
			printf("Case #%lld: %lld\n", k,ans);
		}
	}
	return 0;
}
