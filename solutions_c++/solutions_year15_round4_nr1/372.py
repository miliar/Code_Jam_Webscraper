#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define F first
#define S second
#define SZ(a) (int)((a).size())
#define pb push_back
#define mp make_pair
#define ALL(a) (a).begin(),(a).end()
using namespace std;

typedef long long ll;
typedef pair<int,int> PI;
typedef unsigned long long ull;

#define PR(...) do{cerr << "line : " << __LINE__ << endl; pr(#__VA_ARGS__, __VA_ARGS__);}while(0);
template<class T>
void pr(const string& name, T t){
  cerr << name << ": " << t << endl;
}

template<typename T, typename ... Types>
void pr(const string& names, T t, Types ... rest) {
  auto comma_pos = names.find(',');
  cerr << names.substr(0, comma_pos) << ": " << t << ", ";
  
  auto next_name_pos = names.find_first_not_of(" \t\n", comma_pos + 1);
  pr(string(names, next_name_pos), rest ...);
}

template<class T,class U> ostream& operator<< (ostream& o, const pair<T,U>& v){return o << "(" << v.F << ", " << v.S << ")";}
template<class T> ostream& operator<< (ostream& o, const vector<T>& v){o << "{";rep(i,SZ(v)) o << (i?", ":"") << v[i];return o << "}";}
template<class T> ostream& operator<< (ostream& o, const set<T> &v){o << "{";for(auto e : v) o << e << ", ";return o << "}";}
template<class T, class U> ostream& operator<< (ostream& o, const map<T,U> &v){o << "{";for(auto e : v) o << e.F << ": " << e.S << ", ";return o << "}";}

//                < v > ^
const int dx[] = {0,1,0,-1, 1, 1, -1, -1};
const int dy[] = {-1,0,1,0, 1, -1, 1, -1};
#define endl '\n'

int n, m;
string in[1000];
int vis[200][200][4];

bool rec(int cx, int cy, int dir){
  if(cx < 0 || cy < 0 || cx >= n || cy >= m) return 0;
  if(in[cx][cy] != '.') return 1;
  if(vis[cx][cy][dir] >= 0) return vis[cx][cy][dir];
  return vis[cx][cy][dir] = rec(cx + dx[dir], cy + dy[dir], dir);
}

void solve(int ca){
  cin >> n >> m;
  memset(vis, -1, sizeof(vis));
  rep(i, n) cin >> in[i];

  cout << "Case #" << ca << ": ";
  // {
  //   bool ok = false;
  //   rep(i, n) ok |= count(ALL(in[i]), '.') < m;
  //   if(!ok){
  //     cout << "IMPOSSIBLE" << endl;
  //     return;
  //   }
  // }
  
  int di = 0;
  
  rep(i, n) rep(j, m){
    if(in[i][j] == '.') continue;
    bool ok = 0;
    rep(k, 4){
      int nx = i + dx[k];
      int ny = j + dy[k];
      bool tok = rec(nx, ny, k);
      ok |= tok;
      if("<v>^"[k] == in[i][j]) di += !tok;
    }
    if(!ok){
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  
  cout << di << endl;
}

int main(int argc, char *argv[])
{
  int t;
  cin >> t;
  rep(i, t) solve(i + 1);
  return 0;
}
