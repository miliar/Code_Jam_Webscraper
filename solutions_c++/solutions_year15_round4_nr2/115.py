#include <cstdio>
#include <cstdlib>

int T,N;
double V,X;
double EPS=0.00000000001;
double rs[108];
double cs[108];
int ovnum,udnum;
int ind[108];
int cmp(const void *ka,const void *kb) {
	int a=*(int *)ka;
	int b=*(int *)kb;
	if(cs[a]+EPS<cs[b]) return 1;
	if(cs[a]-EPS>cs[b]) return -1;
	return a-b;
}
int main() {
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d",&N);
		scanf("%lf%lf",&V,&X);
		double rsum=0;
		double allsum=0;
		for(int i=0;i<N;i++) {
			scanf("%lf%lf",&rs[i],&cs[i]);
			rsum+=rs[i];
			cs[i]-=X;
			allsum+=rs[i]*cs[i];
			ind[i]=i;
		}
		qsort(ind,N,sizeof(int),cmp);
		for(int i=0;i<N;i++) {
			if(allsum>EPS) {
				if(cs[ind[i]]>EPS) {
					if(allsum-rs[ind[i]]*cs[ind[i]]>EPS) {
						allsum-=rs[ind[i]]*cs[ind[i]];
						rsum-=rs[ind[i]];
					} else {
						rsum-=allsum/cs[ind[i]];
						allsum=0;
					}
				}
			}
			if(allsum<-EPS) {
				if(cs[ind[i]]<-EPS) {
					if(allsum-rs[ind[i]]*cs[ind[i]]<-EPS) {
						allsum-=rs[ind[i]]*cs[ind[i]];
						rsum-=rs[ind[i]];
					} else {
						rsum-=allsum/cs[ind[i]];
						allsum=0;
					}
				}
			}
		}
		if(rsum<EPS) {
			printf("Case #%d: IMPOSSIBLE\n",ts);
		} else {
			printf("Case #%d: %.12lf\n",ts,V/rsum);
		}
	}
	return 0;
}
