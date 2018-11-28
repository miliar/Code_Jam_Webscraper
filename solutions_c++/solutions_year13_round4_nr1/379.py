#include <cstdio>
#include <map>
#include <algorithm>
#include <cstring>
#define LL long long
#define REP(i,n) for (int i=1;i<=n;++i)
#define FOR(i,n) for (__typeof(n.begin())i=n.begin();i!=n.end();++i)
using namespace std;

const LL MO=1000002013;
const LL INF=1999999999999999999ll;
map<int,int> mp;
int T,n,m,tot,a[1010][3],pos[4040];
LL ans,last,peo[4040];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		memset(peo,0,sizeof(peo));
		mp.clear();
		tot=ans=0;
		scanf("%d%d",&n,&m);
		for (int i=1;i<=m;++i) {
			scanf("%d%d%d",&a[i][0],&a[i][1],&a[i][2]);
			if (a[i][0]>=a[i][1]) continue;
			++a[i][0];
			mp[a[i][0]]=1;
			mp[a[i][1]]=1;
			(ans-=(LL)(a[i][1]-a[i][0])*(LL)(a[i][1]-a[i][0]+1)/2ll%MO*(LL)a[i][2])%=MO;
		}
		last=-INF;
		FOR(i,mp) {
			if (last+1!=i->first) ++tot;
			i->second=++tot;
			last=pos[tot]=i->first;
		}
		for (int i=1;i<=m;++i)
			for (int j=mp[a[i][0]];j<=mp[a[i][1]];++j) peo[j]+=(LL)a[i][2];
		while (1) {
			int l=0,r=0;
			LL c=INF;
			for (int i=1;i<=tot;++i)
				if (peo[i]) {l=i;break;}
			if (!l) break;
			r=l;
			while (peo[r+1]) ++r;
			for (int i=l;i<=r;++i) c=min(c,peo[i]);
			(ans+=(LL)(pos[r]-pos[l])*(LL)(pos[r]-pos[l]+1)/2ll%MO*(LL)c)%=MO;
			for (int i=l;i<=r;++i) peo[i]-=c;
		}
		printf("Case #%d: %I64d\n",T_T,ans);
	}
	return 0;
}
