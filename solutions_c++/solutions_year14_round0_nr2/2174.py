#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<queue>
#include<sstream>
#include<ctime>
using namespace std;

typedef long long Int;
#define FOR(i,a,b) for(int i=(a); i<=(b);++i)
#define mp make_pair
#define pb push_back
#define sz(s) (int)((s).size())
const int inf = 1000000000;
const int MOD = 1000000007;
const double pi=acos(-1.0);

double get() {
	double c, f, x;
	cin>>c>>f>>x;
	double ans=1e+18;
	double can=2;
	double t=0;
	FOR(it,1,10000000) {
		ans=min(ans, t+x/can);
		t+=c/can;
		can+=f;
	}
	return ans;
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		cout<<"Case #"<<tt<<": ";
		printf("%.10lf\n",get());
	}
}