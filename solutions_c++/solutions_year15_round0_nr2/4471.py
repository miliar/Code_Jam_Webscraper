#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;

int p[1005];

int main(){
	freopen("B-small-o.out","w",stdout);
	int n;
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d",&n);
		for(int i=1;i<=n;i++)scanf("%d",&p[i]);
		sort(p+1,p+1+n);
		int prt=0x3f3f3f3f;
		for(int i=1;i<=p[n];i++){
			int ans=i;
			for(int j=1;j<=n;j++){
				if(p[j]<=i)continue;
				else {
					ans+=p[j]/i;
					if(p[j]%i==0)ans--;
				}
			}
			//printf("%d %d\n",i,ans);
			prt=min(prt,ans);
		}
		printf("Case #%d: %d\n",cas,prt);
	}
	return 0;
}
