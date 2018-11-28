#include<cstdio>
#include<algorithm>
using namespace std;
int num[1003];
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) {
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d",&num[i]);
		int ans=10000007;
		for(int i=1;i<1001;i++) {
			int sum=0;
			for(int j=0;j<n;j++) {
				int tmp;
				if(num[j]%i==0) tmp=num[j]/i-1;
				else tmp=num[j]/i;
				sum+=tmp;
			}
			ans=min(ans,sum+i);
		}
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}