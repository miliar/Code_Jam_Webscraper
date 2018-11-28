#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int n;
int a[1005];

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d",&n);
		for (int i=0; i<n; i++) scanf("%d",&a[i]);
		sort(a,a+n);
		int ret = a[n-1];
		for (int i=a[n-1]; i>0; i--) {
			int cnt = 0;
			for (int j=0; j<n; j++)
				cnt += (a[j]-1)/i;
			ret = min(ret,cnt+i);
		}
		printf("Case #%d: %d\n",t,ret);
	}
    return 0;
}
