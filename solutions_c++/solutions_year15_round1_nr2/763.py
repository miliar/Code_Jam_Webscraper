#include<cstdio>
#define long long long

static const int NMAX=1000;

static int N,K,T[NMAX];

static long count(long t) {
	long r=N;
	for(int i=0;i<N;i++)r+=t/T[i];
	return r;
}

static int solve() {
	long _l=0,_r=K*(long)100000;//1e14
	while(_l<_r) {
		const long _m=_l+_r>>1;
		if(count(_m)<K) {
			_l=_m+1;
		} else {
			_r=_m;
		}
	}
	const long c=count(_l);
	int n=0,a[NMAX];
	for(int i=0;i<N;i++)if(_l%T[i]==0)a[n++]=i;
	return a[K-c+n-1];
}

static void input() {
	scanf("%d%d",&N,&K);
	for(int i=0;i<N;i++)scanf("%d",T+i);
}

int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		input();
		printf("Case #%d: %d\n",t,solve()+1);
	}
	return 0;
}
