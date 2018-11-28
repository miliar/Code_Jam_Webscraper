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

vector<double> A,B;
int X[10000];
int C;
int te;
void test(){
	DBG(te);
	A.clear();
	B.clear();
	double x;
	int n;
	scanf("%d",&n);
	FOR(i,n) {
		scanf("%lf",&x);
		A.pb(x);
	}
	FOR(i,n) {
		scanf("%lf",&x);
		B.pb(x);
	}
	sort(A.begin(),A.end());
	sort(B.begin(),B.end());
	
	int ans = 0;
	do{
		int l = 0;
		C++;
		FOR(i,A.size()){
			int g;
			for(int j = SZ(B)-1; j >=0 ; j--) if(X[j] != C) g = j;
			for(int j = SZ(B)-1; j >=0 ; j--) if(X[j] != C && B[j] > A[i]) g = j;
			if(B[g] < A[i]) l++;
			X[g] = C;
		}
		ans = max(ans,l);
	}while(0);
	sort(A.begin(),A.end());
	
	int b = 0;
	int odp = 0;
	FOR(a,SZ(A)){
		if(A[a] > B[b]) {
			b++;
			odp++;
		}
	}
	
	printf("Case #%d: %d %d\n",++te,odp,ans);
}

int main () {
	int t;
	scanf("%d",&t);
	while(t--) test();
}
/*
10
0.88 0.08 0.46 0.22 0.60 0.74 0.82 0.54 0.12 0.26
0.76 0.16 0.96 0.30 0.06 0.80 0.44 0.38 0.42 0.50
10
0.043 0.896 0.948 0.583 0.374 0.696 0.243 0.217 0.339 0.252
0.226 0.122 0.748 0.174 0.078 0.322 0.148 0.870 0.783 0.304
10
0.70 0.90 0.03 0.77 0.53 0.47 0.20 0.40 0.57 0.67
0.23 0.17 0.87 0.33 0.97 0.30 0.50 0.07 0.10 0.37
10
0.389 0.735 0.239 0.637 0.212 0.823 0.726 0.717 0.743 0.619
0.292 0.566 0.009 0.142 0.460 0.965 0.973 0.301 0.788 0.283
8
0.21 0.79 0.10 0.75 0.37 0.96 0.58 0.98
0.25 0.65 0.06 0.77 0.94 0.71 0.92 0.02

*/
