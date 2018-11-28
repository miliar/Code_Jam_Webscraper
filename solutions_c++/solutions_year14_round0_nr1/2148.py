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

int a[55][55][55];
int r[3];

void get() {
	vector<int> ans;ans.clear();
	FOR(it,1,2) {
		cin>>r[it];
		FOR(i,1,4)FOR(j,1,4) cin>>a[it][i][j];
	}
	FOR(i,1,16) {
		if(a[1][r[1]][1]==i || a[1][r[1]][2]==i ||
			a[1][r[1]][3]==i || a[1][r[1]][4]==i) {

				if(a[2][r[2]][1]==i || a[2][r[2]][2]==i ||
			a[2][r[2]][3]==i || a[2][r[2]][4]==i) ans.pb(i);
		
		}
	}
	if(sz(ans)==1) cout<<ans[0]<<endl;else
		if(sz(ans)>1) cout<<"Bad magician!"<<endl;else
			cout<<"Volunteer cheated!"<<endl;
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		cout<<"Case #"<<tt<<": ";
		get();
	}
}