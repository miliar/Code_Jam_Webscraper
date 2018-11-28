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
class UnionFind{
private:
  vector<int> par, rank;
public:
  UnionFind(int n){
	par.assign(n, 0);
	rank.assign(n, 0);
	for(int i=0;i<n;++i)
	  par[i] = i;
  }

  //find root of x
  int find(int x){
	if(par[x] == x)
	  return x;
	return (par[x] = find(par[x]));
  }

  void unite(int x, int y){
	x = find(x);
	y = find(y);
	if(x == y) return;

	if(rank[x] < rank[y])
	  par[x] = y;
	else{
	  par[y] = x;
	  if(rank[x] == rank[y])
		++rank[x];
	}
  }

  bool same(int x, int y){
	return find(x) == find(y);
  }
};


int R, C;
int dx[] = {0,1,0,-1};
int dy[] = {-1,0,1,0};
int tonum(int ix){
  int tx, ty, d;
  if(ix <= C)
	tx = ix-1, ty = 0, d = 0;
  else if(ix <= C+R)
	tx = C-1, ty = ix-C-1, d = 1;
  else if(ix <= C+C+R)
	tx = C-1-(ix-1-R-C), ty = R-1, d = 2;
  else
	tx = 0, ty = R-1-(ix-1-C-R-C), d = 3;
  return (ty*C+tx)*4+d;
}
bool check(VS& vs, VI& cont){
  UnionFind uf(4*R*C);
  REP(y,R) REP(x,C){
	int ix = y*C+x;
	if(vs[y][x] == '/'){
	  uf.unite(ix*4, ix*4+3);
	  uf.unite(ix*4+1, ix*4+2);
	}
	else{
	  uf.unite(ix*4, ix*4+1);
	  uf.unite(ix*4+2, ix*4+3);
	}
	REP(d,4){
	  int tx = x + dx[d], ty = y + dy[d];
	  if(tx < 0 || C <= tx || ty < 0 || R <= ty) continue;
	  int tix = ty*C+tx;
	  uf.unite(ix*4+d, tix*4+(d+2)%4);
	}
  }

  for(int i=0;i<SZ(cont);i+=2){
	if(!uf.same(tonum(cont[i]), tonum(cont[i+1]))){
	  return false;
	}
  }	
  return true;
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T; cin >> T;
  FOR(tt,1,T+1){
	cin >> R >> C;
	VI cont(2*(R+C));
	REP(i,2*(R+C)) cin >> cont[i];
	//for(int x: cont) cout << tonum(x) << endl;
	bool ok = false;
	VS ans(R, string(C,'x'));
	for(int b=0;b<(1<<(R*C));++b){
	  REP(y,R) REP(x,C){
		ans[y][x] = ((b>>(y*C+x)&1)?'/':'\\');
	  }
	  if(check(ans,cont)){
		ok = true;
		break;
	  }
	}
	if(!ok){
	  ans.clear();
	  ans.PB("IMPOSSIBLE");
	}
	cout << "Case #" << tt << ":" << endl;
	for(auto& s: ans) cout << s << endl;
  }
  
  return 0;
}
