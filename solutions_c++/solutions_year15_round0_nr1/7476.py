#include<bits/stdc++.h>
using namespace std;
int main() {
	long long t,s;
	scanf("%lld",&t);
	for(long long j=1;j<=t;j++) {
	
		scanf("%lld",&s);
		long long f=0,a[s+1];
		char n[s+3];
		scanf("%s",n);
		for(long long i=0;i<=s;i++) {
			a[i]=0;
		}
		a[1]=n[0]-48;
		for(long long i=2;i<=s;i++) {
			a[i]=a[i-1]+n[i-1]-48;
		}
		for(long long i=1;i<=s;i++) {
			if(i>(a[i]+f)) {
				f=f+(i-a[i]-f);
			}
		}
		
		printf("Case #%ld: %ld\n",j,f);
	}
	return 0;
}
