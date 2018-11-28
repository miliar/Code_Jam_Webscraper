#include<cstdio>

static inline void MAZ(int &a,int b) {
	if(a<b)a=b;
}

static inline int min(int a,int b) {
	return b<a?b:a;
}

int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		int N,A[1000];
		scanf("%d",&N);
		for(int i=0;i<N;i++)scanf("%d",A+i);
		int ans1=0,ans2=0,lb=0;
		for(int i=1;i<N;i++) {
			const int d=A[i-1]-A[i];
			if(d>0) {
				ans1+=d;
				MAZ(lb,d);
			}
		}
		for(int i=1;i<N;i++) {
			const int d=A[i-1]-A[i];
			ans2+=min(A[i-1],lb);
		}
		printf("Case #%d: %d %d\n",t,ans1,ans2);
	}
	return 0;
}
