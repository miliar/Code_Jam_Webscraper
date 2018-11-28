#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int t,tes,ans,n,k,i,j,x;
int a[1000007];

int main() {
	scanf("%d",&t);
	for (tes = 1; tes <= t; tes++) {
		scanf("%d%d",&n,&k);
		for (i=0 ; i<=700 ; i++) a[i] = 0;
		for (i=0 ; i<n ; i++) {
			scanf("%d",&x);
			a[x]++;
		}
				
		ans = 0;
		i = 700;
		while (i >= 0) {
			while (a[i] != 0) {
				ans++;
				a[i]--;
				j = k - i;
				while (j >= 0 && a[j] == 0) j--;
				if (j >= 0) a[j]--;
			}
			i--;
		}
		
		printf("Case #%d: %d\n",tes,ans);
	}
}