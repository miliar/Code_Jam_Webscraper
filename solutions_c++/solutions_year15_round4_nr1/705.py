//bcw0x1bd2 {{{
#include<bits/stdc++.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#ifdef ONLINE_JUDGE
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#else
#define FILEIO(name)
#endif

void RI() {}

template<typename... T>
void RI( int& head, T&... tail ) {
	    scanf("%d",&head);
			    RI(tail...);
}

mt19937 rng(0x5EED);
int randint(int lb, int ub) {
    return uniform_int_distribution<int>(lb, ub)(rng);
}
// Let's Fight! }}}

typedef pair<int,int> pii;
const int MXN = 105;
const int MX = MXN*MXN;
const int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

int R,C;
vector<pii> node;
string mp[MXN];

void input(){
  cin >> R >> C;
  for (int i=0; i<R; i++){
    cin >> mp[i];
  }
}
bool valid(int x, int y){
  return 0<=x && x<R && 0<=y && y<C;
}
int get_type(char ch){
  if (ch == '<') return 3;
  if (ch == '>') return 2;
  if (ch == '^') return 1;
  if (ch == 'v') return 0;
  assert(false);
  return -1;
}
pii get_node(int x, int y, int d){
  x += dir[d][0];
  y += dir[d][1];
  while (valid(x,y)){
    if (mp[x][y] != '.') return MP(x,y);
    x += dir[d][0];
    y += dir[d][1];
  }
  return MP(-1,-1);
}
void solve(int t){
  node.clear();
  int fail = 0;
  for (int i=0; i<R; i++){
    for (int j=0; j<C; j++){
      if (mp[i][j] != '.'){
        int ok = 0;
        for (int k=0; k<4; k++){
          if (get_node(i,j,k).F != -1){
            ok = 1;
            break;
          }
        }
        if (!ok) fail = 1;
        int d = get_type(mp[i][j]);
        if (d != -1){
          pii v = get_node(i,j,d);
          if (v.F == -1){
            node.PB(MP(i,j));
          }
        }
      }
    }
  }
  if (fail){
    cout << "Case #" << t << ": IMPOSSIBLE\n";
  } else {
    cout << "Case #" << t << ": " << node.size() << "\n";
  }
}

int main(){
  IOS;
  int nT;
  cin >> nT;
  for (int _t=1; _t<=nT; _t++){
    input();
    solve(_t);
  }
  return 0;
}

