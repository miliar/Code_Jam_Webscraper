#include <bits/stdc++.h>
 
using namespace std;
 
//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
 
//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
 
//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define FF first
#define SS second
 
//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);


int N, NN;
bool dfs(int n, VVI& table, VVI& xs, vector<bool>& used){
  if(n == N) return true;
  
  int mn = 1e6;
  REP(i,NN) if(!used[i] && xs[i][n] < mn) mn = xs[i][n];
  VI idx;
  REP(i,NN) if(!used[i] && xs[i][n] == mn)
	idx.PB(i);
  if(SZ(idx) > 2 || SZ(idx) == 0)
	return false;

  if(SZ(idx) == 2){
	REP(it,2){
	  bool ok = true;
	  if(n > 0){
		REP(k,N) if(table[n-1][k] != -1 && xs[idx[0]][k] <= table[n-1][k]) ok = false;
		REP(k,n) if(table[n][k] != -1 && xs[idx[0]][k] != table[n][k]) ok = false;
		REP(k,N) if(table[k][n-1] != -1 && xs[idx[1]][k] <= table[k][n-1]) ok = false;
		REP(k,n) if(table[k][n] != -1 && xs[idx[1]][k] != table[k][n]) ok = false;
	  }
	  if(ok){
		used[idx[0]] = used[idx[1]] = true;
		auto prv = table;
		REP(k,N) table[n][k] = xs[idx[0]][k];
		REP(k,N) table[k][n] = xs[idx[1]][k];
		if(dfs(n+1, table, xs, used)) return true;
		table = prv;
		used[idx[0]] = used[idx[1]] = false;
	  }
	
	  swap(idx[0], idx[1]);
	}
  }
  else{
	used[idx[0]] = true;
	bool ok = true;
	if(n > 0){
	  REP(k,N) if(xs[idx[0]][k] <= table[n-1][k]) ok = false;
	  REP(k,n) if(xs[idx[0]][k] != table[n][k]) ok = false;
	}
	auto prv = table;
	if(ok){
	  REP(k,N) table[n][k] = xs[idx[0]][k];
	  if(dfs(n+1, table, xs, used)) return true;
	  table = prv;
	}

	ok = true;
	if(n > 0){
	  REP(k,N) if(xs[idx[0]][k] <= table[k][n-1]) ok = false;
	  REP(k,n) if(xs[idx[0]][k] != table[k][n]) ok = false;
	}
	if(ok){
	  REP(k,N) table[k][n] = xs[idx[0]][k];
	  if(dfs(n+1, table, xs, used)) return true;
	  table = prv;
	}
	used[idx[0]] = false;
  }
  return false;
}
  
int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T; cin >> T;
  FOR(t,1,T+1){
	cin >> N;
	NN = 2*N-1;
	VVI xs(NN, VI(N));
	REP(i,NN) REP(x,N)
	  cin >> xs[i][x];

	VVI table(N, VI(N,-1));
	vector<bool> used(NN, false);
	dfs(0,table,xs,used);

	map<VI,int> cnt;
	REP(y,N) cnt[table[y]]++;
	REP(x,N){
	  VI tmp; REP(y,N) tmp.PB(table[y][x]);
	  cnt[tmp]++;
	}
	REP(i,NN) cnt[xs[i]]--;

	VI ans(N,-1);
	for(auto& p: cnt) if(p.second > 0) ans = p.first;

	cout << "Case #" << t << ":";
	REP(i,N) cout << " " << ans[i];
	cout << endl;
  }
  
  return 0;
}
