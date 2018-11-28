#include<cstdio>
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) {
		int n,sum,a;
		scanf("%d",&n);
		scanf("%1d",&sum);
		int ans=0;
		for(int i=1;i<=n;i++) {
			scanf("%1d",&a);
			if(sum<i&&a) {
				ans+=(i-sum);
				sum+=(i-sum);
			}
			sum+=a;
		}
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}