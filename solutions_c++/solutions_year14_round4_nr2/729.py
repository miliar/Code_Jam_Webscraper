#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<ctime>
#include<cmath>
#include<map>
#define int64 long long
#define N 1200
using namespace std;
int T,a[N],b[N],s[N],ans,n,i,j,tim;
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	for(scanf("%d",&T);T--;){
		scanf("%d",&n);
		for(i=1;i<=n;++i)scanf("%d",&a[i]),b[i]=a[i];
		sort(b+1,b+n+1);
		for(i=1;i<=n;++i)a[i]=lower_bound(b+1,b+n+1,a[i])-b;
		for(i=1;i<=n;++i){
			s[i]=0;
			for(j=1;j<i;++j)if(a[j]>a[i])s[i]++;
		}
		for(i=1;i<=n;++i)b[a[i]]=i;
		ans=0;
		for(i=n-1;i>=1;--i)
			ans+=min(s[b[i]],n-i-s[b[i]]);
		printf("Case #%d: %d\n",++tim,ans);
	}
}
