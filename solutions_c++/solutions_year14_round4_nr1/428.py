#include <cstdio>
#include <cstdlib>

int T,N,X;
int ss[19999];
int cmp(const void *ka,const void *kb) {
	int a=*(int *)ka;
	int b=*(int *)kb;
	return a-b;
}
int main() {
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d%d",&N,&X);
		for(int i=0;i<N;i++) scanf("%d",&ss[i]);
		qsort(ss,N,sizeof(int),cmp);
		int sol=0;
		int minv=0;
		int maxv=N-1;
		while(minv<=maxv) {
			while(1) {
				if(minv==maxv) break;
				if(ss[minv]+ss[maxv]<=X) break;
				sol++;
				maxv--;
			}
			sol++;
			minv++;
			maxv--;
		}
		printf("Case #%d: %d\n",ts,sol);
	}
	return 0;
}
