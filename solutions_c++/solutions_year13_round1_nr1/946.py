#include <stdio.h>
inline long long f(long long r,long long n){
	return n*(2*n+2*r-1);
}
int solve(long long r,long long t){
	int left=1;
	int right = 2;
	for(;;){
		if(f(r,right)<=t)
			right*=2;
		else
			break;
	}
	int mid;
	while(right-left>1){
		mid = (left+right)/2;
		if(f(r,mid)>t)
			right=mid;
		else
			left=mid;
	}
	return left;
}
int main(){
	int T,i;
	long long r,t;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		scanf("%lld%lld",&r,&t);
		printf("Case #%d: %d\n",i,solve(r,t));
	}
}
