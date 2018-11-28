#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define fi first
#define se second
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PII;
const ll mod=1000000007;
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// head

typedef long double LD;
int sgndet(ll x,ll y,ll x1,ll y1) {
	LD p=(LD)x*y1-(LD)y*x1;
	if (p>=1e15) return 1;
	else if (p<=-1e15) return -1;
	else {
		ll q=x*y1-y*x1;
		if (q>0) return 1;
		else if (q<0) return -1;
		return 0;
	}
}
int dblcmp(LD x,LD eps) { return fabs(x)>=eps?(x>0?1:-1):0;}
struct point {
	ll x,y;
	point(){}
	point(ll _x,ll _y):
	x(_x),y(_y){};
	bool operator==(point a)const {
		return a.x==x&&a.y==y;
	}
	bool operator<(point a)const {
		return a.x==x?y<a.y:x<a.x;
	}
	point add(point p) { return point(x+p.x,y+p.y);}
	point sub(point p) { return point(x-p.x,y-p.y);}
	int det(point p) { return sgndet(x,y,p.x,p.y);}
	LD Det(point p) { return (LD)x*p.y-(LD)y*p.x;}
};
struct polygon  {
	int n;
	point p[11000];
	void add(point q) { p[n++]=q;}
	void getconvex(polygon &convex) {
		int i,j,k;
		sort(p,p+n);
		convex.n=n;
		for (i=0;i<min(n,2);i++) {
			convex.p[i]=p[i];
		}
		if (n<=2)return;
		int &top=convex.n;
		top=1;
		for (i=2;i<n;i++)
		{
			while (top&&convex.p[top].sub(p[i]).det(convex.p[top-1].sub(p[i]))<=0)
				top--;
			convex.p[++top]=p[i];
		}
		int temp=top;
		convex.p[++top]=p[n-2];
		for (i=n-3;i>=0;i--) {
			while (top!=temp&&convex.p[top].sub(p[i]).det(convex.p[top-1].sub(p[i]))<=0)
				top--;
			convex.p[++top]=p[i];
		}
	}
	int check(LD x,LD y) {
		int i,j;
		int cnt=0;
		for (i=0;i<n;i++) {
			j=(i+1)%n;
			point q=p[i].sub(p[j]);
			LD k=dblcmp((x-p[j].x)*q.y-(y-p[j].y)*q.x,1e-3);
//			int k=q.sub(p[j]).det(p[i].sub(p[j]));
			int u=dblcmp(p[i].y-y,1e-12);
			int v=dblcmp(p[j].y-y,1e-12);
			if (k>0&&u<0&&v>=0)cnt++;
			if (k<0&&v<0&&u>=0)cnt--;
		}
		return cnt!=0;
	}
};

const int N=110;
polygon T,S;
int _,n,__;
ll v,x,r[N],c[N];
ll getint() {
	double x;
	scanf("%lf",&x);
	return int(x*10000+0.1);
}
bool check(double t) {
	return T.check(v/t,x/t)!=0;
}
int main() {
//	freopen("B.in","r",stdin);
	for (scanf("%d",&_);_;_--) {
		scanf("%d",&n);
		printf("Case #%d: ",++__);
		fprintf(stderr,"%d\n",__);
		v=getint(); x=getint(); x=x*v;
		rep(i,0,n) {
			r[i]=getint(); c[i]=getint();
			c[i]=r[i]*c[i];
		}
		bool fg1=0,fg2=0;
		bool st1=0,st2=0;
		rep(i,0,n) {
			if (sgndet(v,x,r[i],c[i])<=0) fg1=1;
			if (sgndet(v,x,r[i],c[i])<0) st1=1;
			if (sgndet(v,x,r[i],c[i])>=0) fg2=1;
			if (sgndet(v,x,r[i],c[i])>0) st2=1;
		}
		if (!fg1||!fg2) { puts("IMPOSSIBLE");continue;}
		if (!st1||!st2) {
			point p(0,0);
			rep(i,0,n) if (sgndet(v,x,r[i],c[i])==0) p=p.add(point(r[i],c[i]));
			printf("%.10f\n",1.*v/p.x);
			continue;
		}
		T.n=0;
		T.add(point(0,0));
		rep(i,0,n) {
			int p=T.n;
			rep(j,0,p) T.add(T.p[j].add(point(r[i],c[i])));
			T.getconvex(S);
			T=S;
		}
		LD ans=1e9;
		point c(v,x);
		rep(i,2,T.n) {
			if (T.p[i-1].det(c)<=0&&T.p[i].det(c)>=0) {
//				ct-T.p[i-1]
				point q=T.p[i].sub(T.p[i-1]);
				LD a=c.Det(q),b=T.p[i-1].Det(q);
				ans=min(ans,a/b);
			}
		}
		printf("%.10f\n",(double)ans);
	}
}
