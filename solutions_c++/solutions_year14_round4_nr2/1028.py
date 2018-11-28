#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 1005;
const int INF = ~0u >> 1;
int n,a[maxn];
void init()
{
	scanf("%d",&n);
	for(int i = 0; i < n; ++i) scanf("%d",&a[i]);
}
void solve()
{
	int l = 0,r = n - 1,cnt = 0,ans = 0;
	while(1){
		++cnt;
		int tmp = 0,res = INF;
		for(int i = l; i <= r; ++i)
			if(a[i] < res){
				res = a[i];
				tmp = i;
			}
		if(tmp - l >= r - tmp){
			while(tmp != r){
				swap(a[tmp],a[tmp + 1]);
				++ans;
				++tmp;
			}
			--r;
		}
		else{
			while(tmp != l){
				swap(a[tmp],a[tmp - 1]);
				++ans;
				--tmp;
			}
			++l;
		}
		if(cnt == n) break;
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int ca = 1; ca <= T; ++ca){
		printf("Case #%d: ",ca);
		init();
		solve();
	}
	return 0;
}

