#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;++i)
typedef long long LL;
const int N=1005;
int T,Case,n,ans,a[N],b[N],p[N];
bool cmp(const int i,const int j){return a[i]>a[j];}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		scanf("%d",&n),ans=0;
		rep(i,n) scanf("%d",a+i),b[i]=0,p[i]=i; sort(p,p+n,cmp);
		rep(i,n){
			int c=0; rep(j,p[i]) c+=b[j];
			ans+=min(c,i-c),b[p[i]]=1;
		}
		printf("Case #%d: %d\n",++Case,ans);
	}
	return 0;
}

