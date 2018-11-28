#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#include <cmath>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define db double
#define lb long double
#define N 1000
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
struct ww {
	lb x,y,z,a;
	void read() {
		db A,B;
		scanf("%lf%lf",&A,&B);
		x=A,y=B*A; a=B;
	}
	ww operator - (const ww &A) {
		return (ww){x-A.x,y-A.y};
	}
	ww operator + (const ww &A) {
		return (ww){x+A.x,y+A.y};
	}
	lb operator * (const ww &A) {
		return x*A.y-y*A.x;
	}
} a[N],O,b[N],c[N];
const ww yuan={-123211.12312312121,-454354.12321311};
int i,j,k,n,m,T,te;
inline bool cc1(const ww &a,const ww &b) {
	return a.z<b.z;
}
inline bool cross(ww a,ww b,ww c,ww d) {
	return ((c-a)*(b-a))*((d-a)*(b-a))<0&&((a-c)*(d-c))*((b-c)*(d-c))<0;
}
inline bool ju(db x) {
	int i,j;
	For(i,1,n) {
		b[i]=a[i];
		b[i].x*=x,b[i].y*=x;
		b[i].z=atan2(b[i].y,b[i].x);
	}
	sort(b+1,b+n+1,cc1);
	int t=1,ge=0;
	c[1]=(ww){0,0};
	For(i,1,n) {
		++t;
		c[t]=c[t-1]+b[i];
	}
	For(i,1,n) {
		++t;
		c[t]=c[t-1]-b[i];
	}
	t--;
	For(i,1,t) ge+=cross(O,yuan,c[i],c[i+1]);
	return ge==1;
}
int main() {
	freopen("pool.in","r",stdin);
	freopen("pool.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		scanf("%d",&n); O.read();
		For(i,1,n) a[i].read();
		lb l=0,r=1e9,mid;
		{
			lb s=0;
			For(i,1,n) if (O.a==a[i].a) s+=a[i].x;
			if (s) r=min(r,O.x/s);
		}
		for (;l+1e-8<r;) {
			mid=(l+r)/2;
			if (ju(mid)) r=mid;
			else l=mid;
		}
		printf("Case #%d: ",te);
		if (r>1e8) printf("IMPOSSIBLE\n");
		else printf("%.12lf\n",(db)r);
	}
	return 0;
}
