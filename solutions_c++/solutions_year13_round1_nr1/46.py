#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int T;
long long r,t;

bool ab(long long k){
	long long z=(2*r-1+2*k)*k;
	if(z/k!=(2*r-1+2*k))return 0;
	return z<=t;
}

int main(){
	scanf("%d",&T);
	int h,i;
	for(h=1;h<=T;h++){
		scanf("%lld%lld",&r,&t);
		long long _l=0,_r=1e9;
		while(_l<_r){
			long long mid=(_l+_r+1)/2;
			if(ab(mid))_l=mid;
			else _r=mid-1;
		}
		printf("Case #%d: %lld\n",h,_l);
	}
	return 0;
}
