#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 1011
int n;
double a[MAX],b[MAX];
int cmp(const void *p1,const void *p2){
	return (*(double*)p1-*(double*)p2)>0?1:-1;
}
int solve2(){
	int cnt,i,j;
	for(cnt=0,i=j=0;i<n&&j<n;){
		if(a[i]<b[j])
		++cnt,++i,++j;
		else 
		++j;
	}
	return n-cnt;
}
int solve1(){
	int cnt,tail1,tail2,i,j;
	for(i=0,tail2=n-1;tail2>=0&&b[tail2]>a[n-1];--tail2,++i)
	;
	for(cnt=0,j=0;i<n&&j<=tail2;){
		if(a[i]>b[j])
		++cnt,++i,++j;
		else
		++i;
	}
	return cnt;
}
int main(){
	int i,t,j;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		scanf("%d",&n);
		for(j=0;j<n;++j)
		scanf("%lf",a+j);
		for(j=0;j<n;++j)
		scanf("%lf",b+j);
		qsort(a,n,sizeof(double),cmp);
		qsort(b,n,sizeof(double),cmp);
		printf("Case #%d: %d %d\n",i,solve1(),solve2());
	}
	return 0;
}
