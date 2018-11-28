#include <cstdio>
#define LL long long
LL k,s,realpos;
int T,c;
LL find(LL pos, int c){
	if (c==1) return pos;
	else {
		LL x = find(pos, c-1);
		//printf("%lld %d = %lld\n",pos, c, x);
		return (x-1)*k + realpos;
	}
}
int main(){
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++){
		scanf("%lld%d%lld",&k,&c,&s);
		if (s<k)printf("I don't know\n");
		else {
			printf("Case #%d:", Case);
			for (LL i=1;i<=k;i++){
				realpos=i;
				printf(" %lld",find(1LL*i,c));	
			}
			printf("\n");
		}

	}

	return 0;
}
