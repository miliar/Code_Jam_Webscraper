#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef long long ll;

#define modp(x) (((x)%P+P)%P)
#define mod(x,y) (((x)%(y)+(y))%(y))

long long lowest_rk(int n,long long a){
	if(a==0)return 0;
	if(n==0)return 0;
	return (1LL<<(n-1))+lowest_rk(n-1,(a-1)/2);
}

long long highest_rk(int n,long long a){
	return (1LL<<n)-1-lowest_rk(n,(1LL<<n)-1-a);
}

main(){
	int casenum,totcase;
	scanf("%d",&totcase);
	for(int casenum=1;casenum<=totcase;casenum++){
		printf("Case #%d: ",casenum);
		int n;
		long long p;
		scanf("%d%lld",&n,&p);
		if(p==(1LL<<n)){printf("%lld %lld\n",(1LL<<n)-1,(1LL<<n)-1);continue;}
		long long b0,b1;
		
		//guaranteed
		b0=0;b1=(1LL<<n)-1;
		for(;b1-b0>1;){
			long long mid=(b0+b1)/2;
			if(lowest_rk(n,mid)>=p)b1=mid; else b0=mid;
		}
		printf("%lld ",b0);
		//could
		b0=0;b1=(1LL<<n)-1;
		for(;b1-b0>1;){
			long long mid=(b0+b1)/2;
			if(highest_rk(n,mid)>=p)b1=mid; else b0=mid;
		}
		printf("%lld\n",b0);
	}
}