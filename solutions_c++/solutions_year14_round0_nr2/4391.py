#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define SORT(X) sort(X.begin(),X.end())
#define fi first
#define se second

int te;

void test(){
	double C,F,X,S = 2.0;
	scanf("%lf%lf%lf",&C,&F,&X);
	double ans = X/S;
	double tim = 0;
	FOR(i,100000000){
		tim += C/S;
		S += F;
		ans = min(ans,tim+X/S);
	}
	printf("Case #%d: ", ++te);
	printf("%.10lf\n",ans);
}

int main () {
	int t;
	scanf("%d",&t);
	while(t--) test();
}

