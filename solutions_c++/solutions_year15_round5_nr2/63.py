#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define N 1010
#define int64 long long
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,te,T,K,an;
int ma[N],mi[N],sum[N],zhi[N];
inline bool ju(int an) {
	int i,j;
	int64 l=0,r=0;
	For(i,1,K) {
		l+=-mi[i];
		r+=an-ma[i];
	}
	int64 A=l/K;
	l-=A*K,r-=A*K;
	return l<=sum[1]&&sum[1]<=r||l-K<=sum[1]&&sum[1]<=r-K;
}
int main() {
	freopen("win.in","r",stdin);
	freopen("win.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		scanf("%d%d",&n,&K);
		m=n-K+1;
		For(i,1,m) scanf("%d",&sum[i]);
		For(i,1,K) mi[i]=ma[i]=zhi[i]=0;
		int _=1;
		For(i,1,m-1) {
			int A=sum[i+1]-sum[i];
			zhi[i+K]=zhi[i]+A;
			ma[_]=max(ma[_],zhi[i+K]);
			mi[_]=min(mi[_],zhi[i+K]);
			_++;
			if (_>K) _=1;
		}
		an=0;
		For(i,1,K) an=max(an,ma[i]-mi[i]);
		sum[1]%=K;
		if (sum[1]<0) sum[1]+=K;
		int l=an,r=1e8,mid;
		for (;l<=r;) {
			mid=(l+r)/2;
			if (ju(mid)) r=mid-1;
			else l=mid+1;
		}
		an=r+1;
		printf("Case #%d: %d\n",te,an);
	}
	return 0;
}
