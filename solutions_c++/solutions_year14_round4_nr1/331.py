#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;++i)
typedef long long LL;
int T,Case,n,m,ans,a[10005];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		scanf("%d%d",&n,&m),ans=0;
		rep(i,n) scanf("%d",a+i); sort(a,a+n);
		for (int i=n-1,j=0;j<=i;--i,++ans)
			if (a[i]+a[j]<=m) ++j;
		printf("Case #%d: %d\n",++Case,ans);
	}
	return 0;
}

