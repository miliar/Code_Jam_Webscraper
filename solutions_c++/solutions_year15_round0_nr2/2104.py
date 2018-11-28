#include <cstdio>
#include <queue>
#include <algorithm>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T,n,x,ans,now,tmp;
int a[1010];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		scanf("%d",&n);
		ans=1999999999;
		REP(i,n) scanf("%d",&a[i]);
		for (int tot=1;tot<=3000;++tot) {
			int tmp=0;
			REP(i,n) if (a[i]>=tot) {
				if (a[i]%tot==0) tmp+=a[i]/tot-1;
				else tmp+=a[i]/tot;
			}
			ans=min(ans,tmp+tot);
		}
		printf("Case #%d: %d\n",T_T,ans);
	}
	return 0;
}