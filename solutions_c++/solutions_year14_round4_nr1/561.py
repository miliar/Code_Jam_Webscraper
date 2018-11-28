#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long

int n,m,a[1005],x;

int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
    	scanf("%d%d",&n,&m);
    	memset(a,0,sizeof(a));
    	for (int i=0; i<n; i++) {
			scanf("%d",&x);
			a[x]++;
    	}
    	int ans = 0;
    	for (int i=m; i>=1; i--) {
			for (int j=m-i; j>=1; j--) {
				if (a[i] <= 0) break;
				int add = min(a[i],a[j]);
				if (i == j) {
					add = a[i]/2;
				}
				ans += add;
				a[i] -= add;
				a[j] -= add;
				//printf("%d %d\n",i,j);
			}
			ans += a[i];
			a[i] = 0;
    	}
    	printf("Case #%d: %d\n",t,ans);
    }
	return 0;
}
