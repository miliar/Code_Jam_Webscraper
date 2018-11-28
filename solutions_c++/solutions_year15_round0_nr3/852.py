#include<cstdio>
#define long long long
static const int NMAX=10000;

static int tbl[8][8]={{0,1,2,3},{1,4,3,6},{2,7,4,1},{3,2,5,4}};

static int N;
static long R;
static int A[NMAX];

static int solveL() {
	int now=0,k=0;
	for(int i=1;i<=10*N;i++) {
		now=tbl[now][A[k]];
		if(now==1)return i;
		if(++k==N)k=0;
	}
	return 0;
}

static int solveR() {
	int now=0,k=N;
	for(int i=1;i<=10*N;i++) {
		if(--k<0)k+=N;
		now=tbl[A[k]][now];
		if(now==3)return i;
	}
	return 0;
}

static int mypow(int b,long e) {
	int r=0;
	for(;e!=0;e>>=1) {
		if((e&1)!=0)r=tbl[r][b];
		b=tbl[b][b];
	}
	return r;
}

static int all() {
	int b=0;
	for(int i=0;i<N;i++)b=tbl[b][A[i]];
	return mypow(b,R);
}

static bool solve() {
	if(R*N<3)return false;
	if(all()!=4)return false;
	const int a=solveL();
	if(a==0)return false;
	const int b=solveR();
	return b!=0&&a+b<R*N;
}

static void input() {
	scanf("%d%lld ",&N,&R);
	for(int i=0;i<N;i++)A[i]=getchar()-'h';
}

static void build() {
	for(int i=0;i<8;i++) {
		for(int j=0;j<8;j++) {
			tbl[i][j]=tbl[i&3][j&3];
			if(i>=4)tbl[i][j]^=4;
			if(j>=4)tbl[i][j]^=4;
		}
	}
}

int main() {
	build();
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		input();
		printf("Case #%d: %s\n",t,solve()?"YES":"NO");
	}
	return 0;
}
