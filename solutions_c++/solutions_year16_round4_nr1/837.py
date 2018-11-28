#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
typedef pair<LL, LL> PLL;

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define FF first
#define SS second
template<class S, class T>
istream& operator>>(istream& is, pair<S,T>& p){
  return is >> p.FF >> p.SS;
}

const double EPS = 1e-10;
const double PI  = acos(-1.0);
const LL MOD = 1e9+7;

int N;
string solve(int t, int ix, VI& xs, int lv){
  if(lv == N){
	xs[t]++;
	return string(1, "RPS"[t]);
  }
  string s1, s2;
  if(t == 0){
	s1 = solve(0,ix, xs, lv+1);
	s2 = solve(2, ix+(1<<(N-1-lv)), xs, lv+1);
  }
  else if(t == 1){
	s1 = solve(1,ix, xs, lv+1);
	s2 = solve(0, ix+(1<<(N-1-lv)), xs, lv+1);
  }
  else{
	s1 = solve(1,ix, xs, lv+1);
	s2 = solve(2, ix+(1<<(N-1-lv)), xs, lv+1);
  }
  if(s1 + s2 < s2 + s1) return s1+s2;
  return s2+s1;
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T; cin >> T;
  FOR(tt,1,T+1){
	cin >> N;
	VI xs(3);
	REP(i,3) cin >> xs[i];
	bool ok = false;
	string ans(1<<N, 'Z');
	REP(t,3){
	  VI tmp(3);
	  string s = solve(t,0,tmp,0);
	  if(tmp[0] == xs[0] && tmp[1] == xs[1] && tmp[2] == xs[2]){
		ok = true;
		if(ans > s) ans = s;
	  }
	}

	if(ok)
	  cout << "Case #" << tt << ": " << ans << endl;
	else
	  cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
  }
  
  return 0;
}
