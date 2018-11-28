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

Int a[1000009], s[1000009];

double solve() {
	Int n,p,q,r,ss;
	cin>>n>>p>>q>>r>>ss;
	FOR(i,0,n-1) {
		a[i]=(i*1LL*p+q)%r+ss;
	}
	s[0]=a[0];
	FOR(i,1,n-1) s[i]=s[i-1]+a[i];

	Int best=0;
	FOR(i,0,n-1) {
		Int all = s[n-1]-(i==0?0:s[i-1]);
		int low=i, high=n-1;
		while(low<high) {
			int mid=(low+high)/2+1;
			Int pr = s[mid]-(i==0?0:s[i-1]);
			if(2*pr<=all) low=mid;else high=mid-1;
		}

		
		int sz=0;
		if(i) a[sz++]=s[i-1];
		a[sz++]=s[low]-(i==0?0:s[i-1]);
		if(low!=n-1) a[sz++]=s[n-1]-s[low];
		sort(a, a+sz);
		best=max(best, s[n-1]-(sz<=0?0:a[sz-1]));

		if(high!=n-1) {
			++low;
			++high;
			sz=0;
			if(i) a[sz++]=s[i-1];
			a[sz++]=s[low]-(i==0?0:s[i-1]);
			if(low!=n-1) a[sz++]=s[n-1]-s[low];
			sort(a, a+sz);
			best=max(best, s[n-1]-(sz<=0?0:a[sz-1]));
		}
	}

	return best/double(s[n-1]);
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		double ans = solve();
		cout<<"Case #"<<tt<< ": ";printf("%.10lf\n", ans);
		cerr<<tt<<endl;
	}
}