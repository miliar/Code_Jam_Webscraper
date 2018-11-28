#include <iostream>
#include <algorithm>
#include <limits>
#include <vector>
#include <map>

#define rep(i,m,n) for(int i = m; i < (int)n; i++)
#define REP(i,n) rep(i,0,n)

using namespace std;

typedef pair<double, string> P;

const int MAXN = 1000;
int N;
double naomi[MAXN], ken[MAXN];

void input() {
  cin >> N;
  REP(i,N){ cin >> naomi[i];}
  REP(i,N){ cin >> ken[i];}
}

void solve() {
  vector<P> v;
  REP(i, N) v.push_back(make_pair(naomi[i], "n"));
  REP(i, N) v.push_back(make_pair(ken[i], "K"));
  
  sort(v.begin(), v.end());

  int y = 0, z = 0;
  bool used_ken[v.size()];
  REP(i, v.size()) used_ken[i] = false;

  REP(i, v.size()) {
    if (v[i].second == "n") {
      for (int j = i+1; j < v.size(); ++j) {
	if (v[j].second == "K" && !used_ken[j]) {
	  used_ken[j] = true;
	  z += 1;
	  break;
	}
      }
    }
  }
  z = N - z;


  REP(i, v.size()) used_ken[i] = false;
  for(int i = v.size()-1; i >= 0; --i) {
    if (v[i].second == "n") {
      for (int j = i-1; j >= 0; --j) {
	if (v[j].second == "K" && !used_ken[j]) {
	  used_ken[j] = true;
	  y += 1;
	  break;
	}
      }
    }
  }

  cout << y << " " << z << endl;
  return;
}

int main() {
  int T;
  cin >> T;
  REP(t, T) {
    input();
    cout << "Case #" << t+1 << ": ";
    solve();
  }
  return 0;
}
