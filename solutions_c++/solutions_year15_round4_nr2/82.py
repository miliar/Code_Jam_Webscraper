#include<bits/stdc++.h>
#define int64 long long
#define sqr(x) (x)*(x)
#define mk make_pair
#define pb push_back
#define fi first
#define se second
#define rep(i,x,y) for(int i=(x);i<=(y);++i)
#define VI vector<int>
#define VI64 vector<int64>
#define VS vector<string>
#define PII pair<int,int>
#define PDD pair<double,double>
#define VPII vector< PII >
#define SZ(x) ((int)(x).size())
#define N 120
using namespace std;
const double pi=acos(-1);
struct point{
	double x,y;
}P[2*N];
int T,n,id[N],tim;
double X,V,R[N],C[N];
bool cmp(const int a,const int b){
	return C[a]>C[b];
}
long double det(point a,point b,point c,point d){
	return (long double)(b.x-a.x)*(d.y-c.y)-(long double)(b.y-a.y)*(d.x-c.x);
}
bool check(double mid){
	point O={0,0};
	int tot=0;
	rep(i,1,n){
		if(C[i]==V && mid*R[i]>=X)return 1;
	}
	if(V==C[1] || V==C[n])return 0;
	if(n==1)return 0;
	rep(_,1,n){
		int i=id[_];
		double maxx=mid*R[i];
		O.x+=maxx;
		O.y+=maxx*C[i];
		P[++tot]=O;
	}
	rep(_,1,n){
		int i=id[_];
		double maxx=mid*R[i];
		O.x-=maxx;
		O.y-=maxx*C[i];
		P[++tot]=O;
	}
	point aim={X,V*X};
	P[tot+1]=P[1];
	rep(i,1,tot){
		if(det(P[i],P[i+1],P[i],aim)>0)return 0;
	}
	return 1;
}
void prep(){
	rep(i,1,n){
		rep(j,1,i-1)if(C[i]==C[j]){
			R[j]+=R[i];
			C[i]=-10;
			break;
		}
	}
	int m=n;
	n=1;
	rep(i,2,m)if(C[i]!=-10){
		R[++n]=R[i];
		C[n]=C[i];
	}
}
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	for(scanf("%d",&T);T--;){
		scanf("%d%lf%lf",&n,&X,&V);
		rep(i,1,n)scanf("%lf%lf",&R[i],&C[i]),id[i]=i;
		prep();
		sort(id+1,id+n+1,cmp);
	//	if(tim==75)printf("%lf %lf %lf %lf %lf %lf\n",R[1],C[1],R[2],C[2],X,V);
		double L=0,R=2e6,mid;
		rep(_,1,130){
			mid=(L+R)/2;
			if(check(mid))R=mid;
			else L=mid;
		}
		printf("Case #%d: ",++tim);
		if(R>1e6)printf("IMPOSSIBLE\n");
		else printf("%.8lf\n",R);
	}
}
