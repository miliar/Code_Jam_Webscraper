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

double a[1011], b[1011];
int n;
//int dp[1<<10][1<<10];

int getbits(int n) {
	int ans=0;
	while(n) {
		ans+=n%2;
		n/=2;
	}
	return ans;
}


int get3() {
	for(int win=n; win>=0; --win) {
		bool can=true;
		FOR(i,n-win,n-1) if(a[i]<b[i-(n-win)]) can=false;
		if(can) return win;
	}
}

bool used[11111];
int get2() {
	memset(used, false, sizeof(used));
	int ret=0;
	for(int i=n-1; i>=0; --i) {
		int s=-1;
		for(int j=n-1;j>=0;--j) if(!used[j] && b[j]>a[i])s=j;
		if(s==-1)
			for(int j=n-1;j>=0;--j) if(!used[j])s=j;
		ret+=(b[s]<a[i]);
		used[s]=true;
	}
	return ret;
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		cin>>n;
		FOR(i,0,n-1) cin>>a[i];
		FOR(i,0,n-1) cin>>b[i];
		
		sort(a, a+n);
		sort(b, b+n);

		//FOR(i,0,n-1) cout<<a[i]<<" ";cout<<endl;
		//FOR(i,0,n-1) cout<<b[i]<<" ";cout<<endl;
		cout<<"Case #"<<tt<<": "<<get3()<<"";
		cout<<" "<<get2()<<endl;
	}
}