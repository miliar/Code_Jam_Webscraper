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

#define MOD 1000002013

int n;
int m;
ll o[1010];
ll e[1010];
ll p[1010];

#define tp(a,b,c) mp(a,mp(b,c))
pair<ll,pair<int,ll> > st[2010];

inline ll unt(ll k){return (ll)k*(2*n-k+1)/2 % MOD;}

int solve(){
	ll exped = 0;
	rep(i,m){
		exped += unt(e[i]-o[i])*p[i];
		exped %= MOD;
	}
	sort(st,st+2*m);

//rep(i,2*m) cout << st[i].first << " " << st[i].second.first << " " << st[i].second.second << endl;
	vector<pair<ll,ll> > enst(1010);
	int pp=-1;

	ll jissai=0;
	for(int i=2*m-1;i>=0;--i){

//cout << "  i = " << i << endl;
		if(st[i].second.first==0){
			while(1){
			if(enst[pp].second >= st[i].second.second){
//cout << "hoge" <<endl;
				jissai += unt(enst[pp].first-st[i].first)*st[i].second.second;
				jissai %= MOD;
				enst[pp].second -= st[i].second.second;
				break;
			}else{
//cout << "piy" << endl;
				jissai += unt(enst[pp].first-st[i].first)*enst[pp].second;
				jissai %= MOD;
				st[i].second.second -= enst[pp].second;
			}
			pp--;
			}
		}else{
//cout << "aaaaaa" << endl;
			enst[++pp] = mp(st[i].first, st[i].second.second);
		}
	}
	return (exped - jissai + 2*MOD) % MOD;
}

int main(){
	int casenum; cin >> casenum;
	rep(cas, casenum){
//cout << "case " << cas << endl;
		cin >> n >> m;
		rep(i,m){
			cin >> o[i] >> e[i] >> p[i];
			st[2*i]   = tp(o[i],0,p[i]);
			st[2*i+1] = tp(e[i],1,p[i]);
		}
		printf("Case #%d: %d\n", cas+1, solve());
	}
	return 0;
}

