#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<vector<int> > VVI;

bool findMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
  for (int j = 0; j < int(w[i].size()); j++) {
    if (w[i][j] && !seen[j]) {
      seen[j] = true;
      if (mc[j] < 0 || findMatch(mc[j], w, mr, mc, seen)) {
        mr[i] = j; mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int maxBipartiteMatching(const VVI &w ) {
  if ( w.empty() || w[0].empty() ) return 0;
  VI mr(w.size(),-1), mc(w[0].size(), -1);
  int ct = 0;
  for (int i = 0; i < int(w.size()); i++) {
    VI seen(w[0].size());
    if (findMatch(i, w, mr, mc, seen)) ct++;
  }
  return ct;
}

void solve ( int test ) {
  int m;
  vector<pair<string,string> > vec;
  vector<string> tmp1, tmp2;
  cin >> m;
  for ( int i = 0; i < m; ++i ) {
    string a, b;
    cin >> a >> b;
    tmp1.push_back ( a );
    tmp2.push_back ( b );
    vec.push_back ( { a, b } );
  }
  sort ( tmp1.begin(), tmp1.end() );
  sort ( tmp2.begin(), tmp2.end() );
  tmp1.resize ( unique ( tmp1.begin(), tmp1.end() ) - tmp1.begin() );
  tmp2.resize ( unique ( tmp2.begin(), tmp2.end() ) - tmp2.begin() );

  VVI g ( tmp1.size(), VI ( tmp2.size(), 0 ) );
  for ( int i = 0; i < m; ++i ) {
    int a = lower_bound(tmp1.begin(), tmp1.end(), vec[i].first) - tmp1.begin();
    int b = lower_bound(tmp2.begin(), tmp2.end(), vec[i].second) - tmp2.begin();
    g[a][b] = 1;
  }

  int mflow = maxBipartiteMatching ( g );
  int ans = m - ( tmp1.size() + tmp2.size() - mflow );
  printf ( "Case #%d: %d\n", test, ans );
}

int main() {
  int ntc;
  cin >> ntc;
  for ( int test = 1; test <= ntc; ++test ) {
    solve(test);
  }

  return 0;
}
