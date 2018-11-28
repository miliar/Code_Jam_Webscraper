#include <bits/stdc++.h>

using namespace std;
#define MP make_pair
#define PB push_back
#define LL long long
#define int LL
#define st first
#define nd second
#define FI st
#define SE nd
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define RE(i,n) FOR(i,1,n)
#define REP(i, n) FOR(i, 0, (int)(n)-1)
#define R(i,n) REP(i,n)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PII pair<int,int>
#define VI vector<int>
template<class C> void mini(C&a, C b){a=min(a,b);}
template<class C> void maxi(C&a, C b){a=max(a,b);}

template<class TH> void _dbg(const char* sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char* sdbg, TH h, TA... t){
  while(*sdbg!=',')cerr<<*sdbg++; cerr<<"="<<h<<","; _dbg(sdbg+1, t...);
}

#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#define cerr if(0) cout
#endif

struct Test {
  vector<vector<int>> adj;
  map<string, int> ids;
  
  string shorten(string s) {
    string res;
    char last = 0;
    for (char ch : s) {
      if (ch != last) { last = ch; res += ch; }
    }
    return res;
  }

  void addStr(string s) {
    int sz = SZ(ids);
    ids[s] = sz;
    adj.emplace_back();

    for (int left = 1; left <= SZ(s); left++) {
      string ns(s);
      reverse(ns.begin(), ns.begin() + left);
      for (int i = 0; i < left; i++) { ns[i] ^= ('-' ^ '+'); }
      ns = shorten(ns);

      if (ids.count(ns)) {
        adj[ids[s]].push_back(ids[ns]);
        adj[ids[ns]].push_back(ids[s]);
      }
    }
  }

  void preproc(int N) {
    for (int i = 1; i <= N; i++) {
      string A, B;
      for (int j = 0; j < i; j++) {
        A.push_back(j % 2 ? '+' : '-');
        B.push_back(j % 2 ? '-' : '+');
      }
      addStr(A);
      addStr(B);
    }
  }

  void run() {
    string test;
    cin >> test;

    preproc(SZ(test));

    int from = ids[shorten(test)], to = ids["+"];
    vector<int> dists(SZ(ids));
    fill(ALL(dists), 1e9);
    dists[from] = 0;

    queue<int> Q;
    Q.push(from);
    while (!Q.empty()) {
      int v = Q.front(); Q.pop();
      for (int s : adj[v]) {
        if (dists[s] > dists[v] + 1) {
          dists[s] = dists[v] + 1;
          Q.push(s);
        }
      }
    }

    cout << dists[to] << "\n";
  }
};

#undef int
int main(){
#define int LL
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;

  for (int id = 1; id <= T; id++) {
    cout << "Case #" << id << ": ";
    Test test;
    test.run();
  }

  return 0;
}
