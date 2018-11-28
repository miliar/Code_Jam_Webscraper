#include<cstdio>
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) {
		long long p,q;
		int x=0;
		scanf("%lld/%lld",&p,&q);
		printf("Case #%d: ",t+1);
		for(int i=0;p;i++) {
			//printf("%lld %lld %lf\n",p,q,(double)p/(double)q);
			if((double)p/(double)q>=1) {
					p-=q;
					if(x==0) x=i+1;
					continue;
			} 
			if(q%2==0) {
				q/=2;
			} else {
				if(p>=q) {
					p-=q;
				} else {
					x=0;
					break;
				}
			}
		}
		//printf("%d\n",x);
		if(x==0) printf("impossible\n");
		else if(p==0) printf("%d\n",x-1);
		else printf("impossible\n");
	}
	return 0;
}