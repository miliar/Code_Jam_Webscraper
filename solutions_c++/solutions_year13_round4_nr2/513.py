#include <iostream>
#include <cstdio>

using namespace std;

long long ans1,ans2,p;
int n;

long long power(int a,int b) {
	long long ans=1;
	while (b>0) {
		ans*=a;
		b--;
	}
	return ans;
}

long long cal(int n,long long p) {
	long long ans=0;
	long long ansp=1;
	int k=1;
	n--;
	while (p>ansp) {
		ans+=power(2,n);
		n--;
		ansp+=power(2,k);
		k++;
	}
	return ans;
}

int main() {
	int t,tt;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++) {
		scanf("%d%lld",&n,&p);
		if (p==power(2,n)) {
			ans1=power(2,n)-1;
			ans2=ans1;
		} else {
			ans2=cal(n,p);
			ans1=power(2,n)-2-cal(n,power(2,n)-p);
		}
		printf("Case #%d: %lld %lld\n",tt,ans1,ans2);
	}
	return 0;
}
