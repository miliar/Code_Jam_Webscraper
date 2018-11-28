#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<cstring>
#include<cstdlib>
#include<cassert>

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;

#define mp make_pair
#define pb push_back

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

int n;
ll p;

pair<ll,ll> solve(int n, ll p){
	if(n==1){
		if(p==1) return mp(0,0);
		else return mp(1,1);
	}
	pair <ll, ll> a;
	if(p <= (1LL<<(n-1))){
		a = solve(n-1, p);
		return mp(0,2*a.second);
	}else{
		a = solve(n-1, p-(1LL<<(n-1)));
		ll c = min(a.first * 2 + 2, (1LL<<n)-1);
		ll d = (1LL<<n)-2;
		if(a.second == (1LL<<(n-1))-1) d++;
		return mp(c,d);
	}
}

int main(){
	int casenum; cin >> casenum;
	rep(cas, casenum){
		cin >> n >> p;
		pair<ll,ll> ans = solve(n,p);
		printf("Case #%d: %lld %lld\n", cas+1, ans.first, ans.second);
	}
	return 0;
}

