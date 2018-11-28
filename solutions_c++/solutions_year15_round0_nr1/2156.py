#include <cstdio>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T,n;
int now,ans;
int a[1010];

int Get() {
	char c=getchar();
	while (c<'0' || c>'9') c=getchar();
	return c-'0';
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		scanf("%d",&n);
		for (int i=0;i<=n;++i) a[i]=Get();
		now=ans=0;
		for (int i=0;i<=n;++i)
			if (now>=i) now+=a[i];
			else {
				ans+=i-now;
				now+=i-now;
				now+=a[i];
			}
		printf("Case #%d: %d\n",T_T,ans);
	}
	return 0;
}