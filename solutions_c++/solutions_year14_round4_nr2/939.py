#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int n,ans;
int a[1010];

int main() {
	int t,tt,i,j,x,y;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++) {
		ans=0;
		scanf("%d",&n);
		for (i=0;i<n;i++) scanf("%d",&a[i]);
		for (i=0;i<n;i++) {
			x=y=0;
			for (j=0;j<i;j++) if (a[j]>a[i]) x++;
			for (j=i+1;j<n;j++) if (a[j]>a[i]) y++;
			ans+=x>y?y:x;
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
