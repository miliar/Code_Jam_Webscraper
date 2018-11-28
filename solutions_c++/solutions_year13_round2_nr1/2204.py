#include <iostream>
#include <algorithm>

using namespace std;

int dp[1000002][102], a[102], A, n;
bool use[1000002][102];

int f(int k, int x){
	if(x == n) return 0;
	if(use[k][x]) return dp[k][x];
	use[k][x] = true;
	dp[k][x] = 1 + f(k, x+1);
	if(k > a[x])
		dp[k][x] = min(dp[k][x], f(k+a[x], x+1));
	if(k <= a[n-1])
		dp[k][x] = min(dp[k][x], 1 + f(k+ min(k-1, a[x]), x));
	return dp[k][x];
}

inline void Read(){
	scanf("%d %d\n", &A, &n);
	for(int i=0;i<1000002;i++)
		for(int j=0;j<102;j++)
			use[i][j] = false;
	for(int i=0;i<n-1;i++)
		scanf("%d ", a+i);
	scanf("%d\n", a+n-1);
	sort(a+0, a+n);
}

int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int T;
 	scanf("%d\n", &T);
 	for(int i=1;i<=T;i++){
		Read();
        printf("Case #%d: %d\n", i, f(A, 0));		
	}
	return 0;
}
