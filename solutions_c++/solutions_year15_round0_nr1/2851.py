#include "cstdio"
using namespace std;

int main() {
	int i,j,n,ans,t,sum,need;
	scanf("%d",&t);
	for(i=1;i<=t;i++) {
		scanf("%d ",&n);
		ans=0;sum=0;
		for(j=0;j<=n;j++) {
			need=getchar()-'0';
			if(sum<j && need>0) {
				ans+=j-sum;
				sum+=j-sum;
			}
			sum+=need;
		}
		printf("Case #%d: %d\n",i,ans);
	}
}