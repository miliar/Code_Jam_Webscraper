#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int ttt,tt,i;
long long n,m,k,kk,s1,s0,a[5],b[5];

long long sum0(long long n, long long m){
	if ((n&1) && (m&1))
		return n*(m/2)+n/2;
	return m*n/2;
}
long long sum1(long long n, long long m){
	if ((n&1) && (m&1))
		return n*(m/2)+(n+1)/2;
	return m*n/2;
}

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d: ",tt);
		scanf("%lld%lld%lld\n", &n, &m, &k);
		if (n>m) swap(n,m);
		if (k<=sum1(n,m)) {
			printf("0\n");
			continue;
		}
		k=n*m-k;
		s0=s1=(n-1)*m+n*(m-1);
		
		if (n==1){
			a[4]=b[4]=0;
			a[3]=b[3]=0;
			a[2]=max(0ll, (m-2)/2);
			b[2]=max(0ll, (m-1)/2);
			if (m&1) a[1]=2; else a[1]=1;
			if (m&1) b[1]=0; else b[1]=1;
		} else {
			a[4]=sum1(n-2, m-2);
			a[3]=(n-2)/2 + (m-2)/2;
			if (n&1)
				a[3]+=(m-2)/2;
			else
				a[3]+=(m-1)/2;
			if (m&1)
				a[3]+=(n-2)/2;
			else
				a[3]+=(n-1)/2;
			if ((n&1) && (m&1)) a[2]=4;
			else a[2]=2;
			
			b[4]=sum0(n-2, m-2);
			b[3]=(n-1)/2 + (m-1)/2;
			if (n&1)
				b[3]+=(m-1)/2;
			else
				b[3]+=(m-2)/2;
			if (m&1)
				b[3]+=(n-1)/2;
			else
				b[3]+=(n-2)/2;
			if ((n&1) && (m&1)) b[2]=0;
			else b[2]=2;
			a[1]=b[1]=0;
		}
		kk=k;
		for (i=4; i>=1; --i){
			s0-=min(k, a[i])*i;
			k-=min(k, a[i]);
		}
		k=kk;
		for (i=4; i>=2; --i){
			s1-=min(k, b[i])*i;
			k-=min(k, b[i]);
		}
		printf("%lld\n", min(s0, s1));
		//printf("\n");
	}
	return 0;
}
