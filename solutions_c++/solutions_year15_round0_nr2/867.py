#include<climits>
#include<cstdio>
static inline int max(int a,int b) {return a<b?b:a;}
static inline void miz(int &a,int b) {if(b<a)a=b;}

int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		int N,A[1000];
		scanf("%d",&N);
		for(int i=0;i<N;i++)scanf("%d",A+i);
		int a=INT_MAX;
		for(int m=1;m<=1000;m++) {
			int s=0;
			for(int i=0;i<N;i++)s+=max((m-1+A[i])/m-1,0);
			miz(a,s+m);
		}
		printf("Case #%d: %d\n",t,a);
	}
	return 0;
}
