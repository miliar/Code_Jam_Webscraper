#include <cstdio>
#define LL long long
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T;
LL n,p,ans1,ans2;

LL Best(LL tot,LL rank) {
	if (tot==1) return 1;
	if (rank==tot) return tot;
	return Best(tot/2,rank/2+1);
}

LL Bad(LL tot,LL rank) {
	if (tot==1) return 1;
	if (rank==1) return 1;
	return tot/2+Bad(tot/2,(rank-2)/2+1);
}

int main() {
	freopen("2.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		scanf("%I64d%I64d",&n,&p);
		n=(1ll<<n);
		ans1=ans2=0;
		for (LL c=n;c;c>>=1)
			if ((ans1+c<=n)&&(Bad(n,ans1+c)<=p)) ans1+=c;
		for (LL c=n;c;c>>=1)
			if ((ans2+c<=n)&&(Best(n,ans2+c)<=p)) ans2+=c;
		printf("Case #%d: %I64d %I64d\n",T_T,ans1-1,ans2-1);
	}
	return 0;
}
