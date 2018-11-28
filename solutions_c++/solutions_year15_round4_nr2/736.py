#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define all(v) (v).begin(),(v).end()

#define VI vector<int>
#define PII pair<int,int>
#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define lint long long int

#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debug2(x,y) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y <<endl; } 
#define debug3(x,y,z) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y << ", " << #z << " = " << z <<endl; } 
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define debugt(t,n) {{cerr <<#t <<" = "; FOR(it,0,(n)) cerr <<t[it] <<", "; cerr <<endl; }}

#define make( x) int (x); scanf("%d",&(x));
#define make2( x, y) int (x), (y); scanf("%d%d",&(x),&(y));
#define make3(x, y, z) int (x), (y), (z); scanf("%d%d%d",&(x),&(y),&(z));
#define make4(x, y, z, t) int (x), (y), (z), (t); scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define makev(v,n) VI (v); FOR(i,0,(n)) { make(a); (v).pb(a);} 
#define IOS ios_base::sync_with_stdio(0)
#define HEAP priority_queue

#define read( x) scanf("%d",&(x));
#define read2( x, y) scanf("%d%d",&(x),&(y));
#define read3(x, y, z) scanf("%d%d%d",&(x),&(y),&(z));
#define read4(x, y, z, t) scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define readv(v,n) FOR(i,0,(n)) { make(a); (v).pb(a);}

using namespace std;

#define max_n 1000005

void solve(){
	make(n);
	double V,X;
	scanf("%lf %lf",&V,&X);
	vector<double> v;
	vector<double> c;
	if(n==1){
		double a,b;
		scanf("%lf %lf\n",&a,&b);
		if(b!=X) printf("IMPOSSIBLE\n");
		else printf("%.17lf\n",V/a);
		return;	
	}
	FOR(i,0,n){
		double a,b;
		scanf("%lf %lf\n",&a,&b);
		v.pb(a); c.pb(b);
	}
	if(n==2){
		if(c[0]==c[1]){
			if(c[0]!=X) printf("IMPOSSIBLE\n");
			else printf("%.17lf\n",V/(v[0]+v[1]));
		}
		else{
			double det = v[1]*v[0]*(c[1]-c[0]);
			double det1 = v[1]*V*(c[1]-X);
			double det2 = v[0]*V*(X-c[0]);
			if(det1/det >=-1e-9 && det2/det >=-1e-9){
				printf("%.17lf\n",max(det1/det,det2/det));
			}
			else printf("IMPOSSIBLE\n");
		}
	}
}


int main(){
	make(t);
	FOR(i,1,t+1){
		printf("Case #%d: ",i);
		solve();
	}
}

