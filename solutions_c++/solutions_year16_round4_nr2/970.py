#include <cstdio>
#include <cstdlib>

double probx[208][208];
double proby[208][208];
double est[208];
void init(int N) {
	for(int i=0;i<=N;i++) {
		for(int j=0;j<=N;j++) {
			probx[i][j]=0;
			proby[i][j]=0;
		}
	}
	probx[0][0]=1;
	proby[0][0]=1;
	for(int i=0;i<N;i++) {
		for(int j=0;j<=N;j++) {
			probx[i+1][j]+=probx[i][j]*(-est[i]+1);
			probx[i+1][j+1]+=probx[i][j]*est[i];
			proby[i+1][j]+=proby[i][j]*(-est[N-1-i]+1);
			proby[i+1][j+1]+=proby[i][j]*est[N-1-i];
		}
	}
}
int cmp(const void *ka,const void *kb) {
	double a=*(double *)ka;
	double b=*(double *)kb;
	if(a<b) return -1;
	if(a>b) return 1;
	return 0;
}
int main() {
	int T,N,K;
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d%d",&N,&K);
		for(int i=0;i<N;i++) scanf("%lf",&est[i]);
		qsort(est,N,sizeof(double),cmp);
		init(N);
		double sol=0;
		for(int X=0;X<=K;X++) {
			double ksol=0;
			for(int y=0;y<=K/2;y++) ksol+=probx[X][y]*proby[K-X][K/2-y];
			if(sol<ksol) sol=ksol;
		}
		printf("Case #%d: %.12lf\n",ts,sol);
	}
	return 0;
}
