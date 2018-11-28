#include <bits/stdc++.h>

using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define FOR(i,n) REP(i,0,(int)n-1)
#define mp make_pair
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define VI vector<int>
#define fi first
#define se second
#define pss pair<short int, short int>

set<int> getDig(int x) {
	set<int> res;
	if(x == 0) res.insert(0);
	while(x>0) {
		res.insert(x%10);
		x/=10;
	}
	return res;
}

void solve(int x) {
	set<int> S;
	int val=x;
	while(1) {
		set<int> temp = getDig(val);
		for(set<int>::iterator it=temp.begin(); it!=temp.end(); it++) S.insert(*it);
		if(S.size()==10) {
			cout<<val<<"\n";
			return;
		}
		val+=x;
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int i=1; i<=t; i++) {
		cout<<"Case #"<<i<<": ";
		int x;
		cin>>x;
		if(x==0)cout<<"INSOMNIA\n";
		else solve(x);
	}
	return 0;
}