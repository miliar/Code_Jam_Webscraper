#include <bits/stdc++.h>

#define For(i,a,b) for (int i = (a); i <= (b); i++)
#define Ford(i,a,b) for (int i = (a); i >= (b); i--)
#define Rep(i,a) for (int i = 0; i < (a); i++)
#define Repd(i,a) for (int i = (int)(a) - 1; i >=0; i--)
#define PI (acos(0.0) * 2)
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PII pair<int, int>
#define PIII pair<PII, int>
#define VI vector<int>
#define sz(a) ((int)a.size())
#define oo 1000000000
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(a,u,v) {cout << #a << " = "; For(_,u,v) cout << a[_] << ' '; cout << endl;}
typedef long long LL;
using namespace std;

int ntest;
double X,C;
int n;
double v[200], r[200];
double t1,t2;

void solve(double x, double y){
	
	t2 = (C-y)/(x-y);
	t1= 1-t2;
}

void solve(int test){
	printf("Case #%d: ",test+1);
	scanf("%d %lf %lf",&n,&X,&C);
	double td=0,vd=0;
	double ta=0, va=0,vb=0;
	
	for(int i=0; i<n; i++){
		scanf("%lf %lf",&v[i],&r[i]);
		if(r[i]==C){
			vb += v[i];
		}
		else if(r[i] < C){
			ta += v[i]*r[i];
			va += v[i];
		}else{
			td += v[i]*r[i];
			vd += v[i];
		}
	}
	if(vd==0 || va==0){
		if(vb==0)
			cout << "IMPOSSIBLE" << endl;
		else 
			printf("%.6lf\n",X/vb);
		return;
	}
	double tempd = td/vd;
	double tempa = ta/va;
	//cout << tempd << " "<<  tempa << endl;
	solve(tempd,tempa);
	//cout << (C-tempa)/(tempd-tempa) << " " << t1 << " " << t2 << endl;
	//cout << vd << " "<< va << endl;
	
	
	t1= X*t1/va;
	t2= X*t2/vd;
	double Xt = max(t1,t2)*vb;
	t1 = t1*X/(X+Xt);
	t2 = t2*X/(X+Xt);
	printf("%.7lf\n",max(t1,t2));
}
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
