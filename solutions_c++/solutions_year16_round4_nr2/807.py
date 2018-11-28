#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)

#define double long double

vector<double> p;

double memo[20][10];

int pos;
int mpos;
vector<double> com;
int k;

double solve(int n,int yes) {
	if(memo[n][yes]!=-1) return memo[n][yes];
	if(n==mpos) {
		// tie
		if(yes == 0) return memo[n][yes] = 1;
		else return memo[n][yes] = 0;
	}
	// part of com & yes
	double ans = 0;
	if(yes) ans+= solve(n+1,yes-1)*com[n];
	// part of com & no
	ans+= solve(n+1,yes)*(1-com[n]);
	return memo[n][yes] = ans;
}

double solve2(int n) {
	if(mpos==k) {
		FOR(i,k+1) FOR(j,k/2+1) memo[i][j]=-1;
		double x = solve(0,k/2);
		//FOR(i,mpos) printf("%lf ",com[i]);
		//printf("=     %Lf\n",x);
		return x;
	}
	if(n==p.size()) return 0;
	// nedaj
	double ans = 0;
	ans = max(ans,solve2(n+1));
	// daj
	com[mpos++] = p[n];
	ans = max(ans,solve2(n+1));
	--mpos;
	return ans;
}



	
	
	
	


	
int main(void) {
	int t;
	scanf("%d",&t);
	com.resize(20);
	for(int tt=1;tt<=t;++tt) {
		int n;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",tt);
		p.clear();
		FOR(i,n) {
			double x;
			scanf("%Lf",&x);
			p.push_back(x);
		}
		printf("%.20Lf\n",solve2(0));
	}
}