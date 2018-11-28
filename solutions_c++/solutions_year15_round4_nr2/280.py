#include<stdio.h>
#include<string.h>
#define fi first
#define se second
#define M 222
#include<algorithm>
#include<cassert>
#define ll long long
using namespace std;
typedef pair<double,double> dd;
int n , T;
double V;
dd t[M];
double X;
double cc(double x){
	if(x >= 0) return x;
	return -x;
}
bool ok(double mid){
	double res = 0;
	for(int i = 1 ; i <= n ; i++)	res+=mid*t[i].se;
	if(res < V) return false;
	double curr = V;
	double left = 0;
	for(int i = 1 ; i <= n ; i++)
		if(curr >= mid*t[i].se) {
			curr-=mid*t[i].se;
			left+=mid*t[i].se*t[i].fi;
		}
		else{
			left+=curr*t[i].fi;
			break;
		}
	double right = 0;
	curr = V;
	for(int i = n ; i >= 1 ; i--)
		if(curr >= mid*t[i].se) {
			curr-=mid*t[i].se;
			right+=mid*t[i].se*t[i].fi;
		}
		else{
			right+=curr*t[i].fi;
			break;
		}
	if(X*V >= left  && X*V <= right ) return true;
	return false;
}
main(){
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	int nT = 1;
	while(T > 0){
		scanf("%d %lf %lf",&n,&V,&X);
		for(int i = 1 ; i <= n ; i++)	
			scanf("%lf %lf",&t[i].se,&t[i].fi);
		sort(t + 1 , t + 1 + n);
		if(X < t[1].fi || X > t[n].fi) printf("Case #%d: IMPOSSIBLE\n",nT);
		else{
			double lo = 0;
			double hi = 1e8;
			int tt = 0;
			while(true){
				tt++;
				double mid = (lo + hi)/2;
				if(tt >= 500) break;
				if(ok(mid)) hi = mid;
				else lo = mid;
			}
			double tot = 0;
			if(t[1].fi == t[n].fi){
				for(int i = 1 ; i <= n ; i++)	tot+=t[i].se;
				lo = V / tot;
			}
			printf("Case #%d: %.10f\n",nT,lo);
		}
		T--;
		nT++;
	}
}

