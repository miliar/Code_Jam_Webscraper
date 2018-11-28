#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

string rec(int N, int R, int P, int S){
	if(N == 0){
		if(R < 0 || P < 0 || S < 0)
			return "IMPOSSIBLE";
		if(R)
			return "R";
		if(P)
			return "P";
		return "S";
	}
	int r=(R+S-P)/2;
	int s=(S+P-R)/2;
	int p=(P+R-S)/2;
	if(r < 0 || s < 0 || p < 0)
		return "IMPOSSIBLE";
	string res=rec(N-1, r, p, s);
	if(res == "IMPOSSIBLE")
		return res;
	vector<string> ret;
	rep(i,0,res.size()){
		if(res[i] == 'R')
			ret.push_back("RS");
		if(res[i] == 'S')
			ret.push_back("PS");
		if(res[i] == 'P')
			ret.push_back("PR");
	}
	string finalRet="";
	rep(i,0,ret.size())
		finalRet += ret[i];
	return finalRet;
}

void solve(){
	int N, R, P, S;
	scanf("%d%d%d%d", &N, &R, &P, &S);
	string ans=rec(N, R, P, S);
	if(ans != "IMPOSSIBLE"){
	rep(i,0,N){
		for(int j=0; j < ans.size(); j += (2<<i)){
			if(ans.substr(j+(1<<i),(1<<i)) < ans.substr(j,(1<<i))){
				rep(k,0,(1<<i))
					swap(ans[j+k], ans[j+k+(1<<i)]);
			}
		}
	}
	}
	printf("%s\n", ans.c_str());
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=1; i <= T; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}
