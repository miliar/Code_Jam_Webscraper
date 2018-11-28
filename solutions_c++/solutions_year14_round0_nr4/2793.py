#include<cstdio>
#include<cstdlib>
int cmp(const void *a,const void *b) {
	if(*(double *)a>*(double *)b) return -1;
	else return 1;
}
void solve(int t) {
	int n;
	double A[1000],B[1000];
	scanf("%d",&n);
	for(int i=0;i<n;i++) scanf("%lf",&A[i]);
	for(int i=0;i<n;i++) scanf("%lf",&B[i]);
	qsort(A,n,8,cmp);
	qsort(B,n,8,cmp);
	int ma=0,ans=0;
	for(int i=0;i<n;i++) {
		if(B[i]<A[ma]) {
			ma++;
			ans++;
		}
	}
	printf("Case #%d: %d ",t,ans);
	ma=0;ans=0;
	for(int i=0;i<n;i++) {
		if(B[ma]<A[i]) ans++;
		else ma++;
	}
	printf("%d\n",ans);
	//for(int i=0;i<n;i++) printf("%lf ",A[i]); printf("\n");
	//for(int i=0;i<n;i++) printf("%lf ",B[i]); printf("\n");
}
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) solve(t+1);
	return 0;
}