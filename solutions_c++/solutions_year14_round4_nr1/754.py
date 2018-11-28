#include <stdio.h>
#include <algorithm>

using namespace std;

#define N 10005

int n,a[N],x;

void input()
{
	scanf("%d %d" ,&n,&x);
	for(int i=1; i<=n; i++) scanf("%d",&a[i]);
	sort(a+1,a+n+1);
}

void process()
{
	int ans=0;
	int j=1;
	for(int i=n; i>=j; i--) {
		ans++;
		if(a[j]+a[i]<=x) j++;
	}
	printf("%d",ans);
}

int main()
{
	int t,i;
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	scanf("%d",&t);
	for(int i=1; i<=t; i++) {
		printf("Case #%d: ",i);
		input();
		process();
		printf("\n");
	}
	return 0;
}