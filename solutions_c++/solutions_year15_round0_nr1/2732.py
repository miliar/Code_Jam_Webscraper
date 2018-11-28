#include <stdio.h>
#include <string.h>
#include <algorithm>
using std::min;
using std::max;
const int N = 1e3 + 11;
int f[N], sum[N];
char s[N];
int main()
{
	// freopen("A-large.in", "r", stdin);
	// freopen("ou.txt", "w", stdout);
	int t, kase=0;
	int m;
	scanf("%d", &t);
	while(t--){
		scanf("%d%s", &m, s);
		memset(sum, 0, sizeof(sum));
		sum[0] = s[0]-'0';
		for(int i=1; i<=m; i++){
			sum[i] = sum[i-1] + s[i] - '0';
		}
		f[0] = 0;
		for(int i=1; i<=m; i++){
			f[i] = m;
			for(int j=0; j<i; j++){
				int t = max(0, i-f[j]-sum[j] + f[j]);
				f[i] = min(f[i], t);
			}
		}
		int ans = 0;
		for(int i=0; i<=m; i++){
			ans = max(ans, f[i]);
		}
		printf("Case #%d: %d\n", ++kase, ans);
	}
	return 0;
}