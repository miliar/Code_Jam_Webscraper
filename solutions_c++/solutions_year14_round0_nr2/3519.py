/**
 *	Author : hkbharath
 *	Problem : https://code.google.com/codejam/contest/2974486/dashboard#s=p1
 *	Lang : C++
 */	

#include <bits/stdc++.h>

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define FOR(a,b,c) for(int a=b;a<=c;++a)
#define RFOR(a,b,c) for(int a=b;a>=c;--a)
#define LOOP(a) FOR(xx,1,a)
#define PB(b) push_back(b)
#define MP(a,b) make_pair(a,b)
#define MOD 1000000007
#define ALL(a) (a.begin(),a.end())
#define ALL(a,n) (a,a+n)

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

double r,c,f,x,best_sol,ts;

double comp(double a,double b){
	//printf("%f %f %f\n",a,b,a-b);
	return a-b;
}

void search(){
	best_sol=x/r;ts=c/r;
	r+=f;
	while(comp(ts,best_sol)<0){
		best_sol=min(best_sol,ts+x/r);
		ts+=c/r;
		r+=f;
		//printf("%f %f",ts,x/r);
	}
}

void solve(int tt){
	r=2;
	scanf("%lf %lf %lf",&c,&f,&x);
	search();
	printf("%.7lf\n",best_sol);
}

int main(){
	int t,it;
	scanf("%d",&t);
	for(it=1;it<=t;it++){
		printf("Case #%d: ",it);
		solve(it);
	}
}
