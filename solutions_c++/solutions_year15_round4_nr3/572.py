#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;
typedef long long i64;
typedef i64 nkr_int;
typedef pair<i64, i64> pi;

typedef vector<nkr_int> vi;
typedef vector<vi> vvi;
#define pb push_back
#define iter(T) T::iterator
#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define present(c, x) ((c).find(x) != (c).end())
#define cpresent(c, x) (find(all(c), x) != (c).end())
#define REP(s, e, n)  for(n = (s); n < (e); ++n)

class Solver {
public:
  Solver() {}
  ~Solver() {}

  void solve();
};

void Solver::solve() {
  i64 N;
  cin >> N;

  map<string, int> wmap;
  vvi words(N);
  i64 i,j;
  getchar();
  REP(0, N, i) {
    string line;
    getline(cin, line);
    string w = "";
    REP(0, sz(line), j) {
      if(line[j] == ' ') {
	if(wmap.find(w) == wmap.end()) {
	  wmap.insert(pair<string, int>(w, sz(wmap)));
	  words[i].pb(sz(wmap)-1);
	}
	else {
	  words[i].pb(wmap[w]);
	}
	w = "";
      }
      else {
	w.append(1, line[j]);
      }
    }

    if(wmap.find(w) == wmap.end()) {
      wmap.insert(pair<string, int>(w, sz(wmap)));
      words[i].pb(sz(wmap)-1);
    }
    else {
      words[i].pb(wmap[w]);
    }
    sort(all(words[i]));
    words[i].erase(unique(all(words[i])), words[i].end());    
  }

  vi com_flag0(sz(wmap), 0);
  vi Ewords = words[0], Fwords = words[1];
  REP(0, sz(Ewords), i) {
    if(binary_search(all(Fwords), Ewords[i])) {
      com_flag0[Ewords[i]] = 1;
    }
  }

  vvi Ecom(N - 2), Fcom(N - 2);
  REP(2, N, i) {
    REP(0, sz(words[i]), j) {
      if(!com_flag0[words[i][j]]) {
	if(binary_search(all(Fwords), words[i][j])) {
	  Fcom[i-2].pb(words[i][j]);
	}
      }
    }
    REP(0, sz(words[i]), j) {
      if(!com_flag0[words[i][j]]) {
	if(binary_search(all(Ewords), words[i][j])) {
	  Ecom[i-2].pb(words[i][j]);
	}
      }
    }
  }

  i64 ii;
  vector<vvi> Ccom(N - 2, vvi(N - 2));
  REP(2, N, i) {
    REP(i+1, N, ii) {
      REP(0, sz(words[i]), j) {
	if(!com_flag0[words[i][j]]) {
	  if(binary_search(all(words[ii]), words[i][j])) {
	    Ccom[i-2][ii-2].pb(words[i][j]);
	    Ccom[ii-2][i-2].pb(words[i][j]);
	  }
	}
      }
    }
  }
  
  unsigned int F = 0, Fmax = 1 << (N - 2);
  i64 ans = Ewords.size() + Fwords.size();
  while(F < Fmax) {
    vi com_flag = com_flag0;
    REP(2, N, i) {
      if((F & ((1u << (i - 2)))) != 0) {
	REP(0, sz(Fcom[i-2]), j) {
	  if(!com_flag[Fcom[i-2][j]]) {
	    com_flag[Fcom[i-2][j]] = 1;
	  }
	}
      }
      else {
	REP(0, sz(Ecom[i-2]), j) {
	  if(!com_flag[Ecom[i-2][j]]) {
	    com_flag[Ecom[i-2][j]] = 1;
	  }
	}
      }

      i64 ii;
      REP(i+1, N, ii) {
	bool f1 = (F & ((1u << (i - 2)))) != 0;
	bool f2 = (F & ((1u << (ii - 2)))) != 0;
	if(f1 != f2) {
	  REP(0, sz(Ccom[i-2][ii-2]), j) {
	    if(!com_flag[Ccom[i-2][ii-2][j]]) {
	      com_flag[Ccom[i-2][ii-2][j]] = 1;
	    }
	  }
	}
      }
    }

    i64 ans0 = 0;
    REP(0, sz(com_flag), i) {
      ans0 += com_flag[i];
    }

    ans = min(ans, ans0);
    F++;
  }

  cout << ans << endl;
}

int main(int argc, char *argv[]){

  i64 N;
  cin >> N;
  i64 n;

  Solver s;

  REP(0, N, n) {
    cout << "Case #" << n + 1 << ": ";

    s.solve();
  }

  return 0;
}

