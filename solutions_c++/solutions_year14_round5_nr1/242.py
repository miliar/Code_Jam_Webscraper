#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;++i)
typedef long long LL;
const int N=1000005;
int T,Case,n,p,q,r,s,a[N]; LL b[N],ans;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		scanf("%d%d%d%d%d",&n,&p,&q,&r,&s);
		rep(i,n) a[i]=(1LL*i*p+q)%r+s,b[i+1]=b[i]+a[i]; int j=0; ans=b[n];
		rep(i,n+1){
			while (b[j]-b[i]<b[n]-b[j])
				ans=min(ans,max(b[i],max(b[j]-b[i],b[n]-b[j]))),++j;
			ans=min(ans,max(b[i],max(b[j]-b[i],b[n]-b[j])));
		}
		printf("Case #%d: %.10lf\n",++Case,1-1.*ans/b[n]);
	}
	return 0;
}

