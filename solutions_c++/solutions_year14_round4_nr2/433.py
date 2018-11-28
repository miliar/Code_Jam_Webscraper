#include <cstdio>

int T,N;
int as[1999];
int main() {
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d",&N);
		for(int i=0;i<N;i++) scanf("%d",&as[i]);
		int sol=0;
		for(int i=0;i<N;i++) {
			int lf=0;
			int rg=0;
			for(int j=0;j<i;j++) if(as[j]>as[i]) lf++;
			for(int j=i+1;j<N;j++) if(as[j]>as[i]) rg++;
			if(lf<rg) {
				sol+=lf;
			} else {
				sol+=rg;
			}
		}
		printf("Case #%d: %d\n",ts,sol);
	}
	return 0;
}
