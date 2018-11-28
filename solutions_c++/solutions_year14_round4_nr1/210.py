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

int a[10009];
bool used[10009];

int get() {
	int n,x;cin>>n>>x;
	FOR(i,1,n)cin>>a[i];
	sort(a+1, a+n+1);
	int ans=0;
	memset(used, false, sizeof(used));
	for(int i=n; i>=1; --i) if(!used[i]) {
		int j;
		for(j=i-1; j>=1; --j) if(!used[j]) if(a[i]+a[j]<=x) break;
		ans++;
		used[i]=used[j]=true;
	}
	return ans;
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		cout<<"Case #"<<tt<<": ";
		cout<<get()<<endl;
	}
}