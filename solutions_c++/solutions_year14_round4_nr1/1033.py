#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 10005;
int n,k,a[maxn];
void init()
{
	scanf("%d%d",&n,&k);
}
void solve()
{
	for(int i = 0; i < n; ++i) scanf("%d",&a[i]);
	sort(a,a + n);
	int ans = n;
	for(int i = 0,j = n - 1; i < j; ++i){
		while(a[i] + a[j] > k && i < j){
			--j;
		}
		if(i < j){
			--ans;
			--j;
		}
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 1; i <= T; ++i){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}

