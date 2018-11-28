#include<stdio.h>
#include<stdlib.h>

int comp(const void* a, const void* b) {
	double _a = *(double*) a;
	double _b = *(double*) b;

	if (_a > _b)
		return 1;
	else if (_a < _b)
		return -1;
	else
		return 0;
}

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("out.txt","w",stdout);

			int T;
			scanf("%d",&T);
			for(int x=1;x<=T;x++) {
				int N;
				scanf("%d",&N);

				double *n = (double*)malloc(N*sizeof(double));
				double *k = (double*)malloc(N*sizeof(double));

				for(int i=0;i<N;i++)scanf("%lf",&n[i]);
				for(int i=0;i<N;i++)scanf("%lf",&k[i]);

				qsort(n,N,sizeof(double),comp);
				qsort(k,N,sizeof(double),comp);

				int nf=0,nb = N-1;
				int kf=0,kb = N-1;

				while(nb >= nf){
						while(n[nb] > k[kb] && nb >= nf){
							nb--;
							kb--;
						}
						if(nb >= nf){
							nf++;
							kb--;
						}
				}
				int y = N-nf;

				nf=0;
				kf=0;
				while(nf < N && kf < N) {
					while(n[nf] > k[kf] && kf < N)kf++;
					if(kf < N) {
						nf++;
						kf++;
					}
				}
				int z = N-nf;

				printf("Case #%d: %d %d\n",x,y,z);
				free (n);
				free (k);
			}
		}
