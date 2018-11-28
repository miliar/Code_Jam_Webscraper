#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int t,n,i,j,left,right,tes,ans1,ans2,mem[1007][1007];
double a[1007],b[1007];

int DP(int left, int right) {
	int pos = n-1 - (right - left);
	
	if (mem[left][right] != -1) return mem[left][right];
	if (pos >= n) return 0;
	
	int ans = DP(left,right-1);
	if (a[pos] >= b[left]) ans = max(ans, 1 + DP(left+1,right));
	
	return mem[left][right] = ans;
}

int main() {
	scanf("%d",&t);
	for (tes=1 ; tes<=t ; tes++) {
		scanf("%d",&n);
		for (i=0 ; i<n ; i++) scanf("%lf",&a[i]);
		for (i=0 ; i<n ; i++) scanf("%lf",&b[i]);
	
		sort(a,a+n);
		sort(b,b+n);
		
		for (i=0 ; i<n ; i++)
			for (j=0 ; j<n ; j++)
				mem[i][j] = -1;
		
		ans1 = DP(0,n-1);
		ans2 = 0;
		
		left = 0;
		right = n-1;
		
		for (i=n-1 ; i>=0 ; i--) {
			if (a[i] > b[right]) {
				ans2++;
				left++;
			} else {
				right--;
			}
		}
		
		printf("Case #%d: %d %d\n",tes,ans1,ans2);
	}
}