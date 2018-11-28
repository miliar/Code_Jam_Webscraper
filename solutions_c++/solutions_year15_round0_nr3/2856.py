#include <iostream>
#include <string>
#include <set>

using std::cin;
using std::cout;

// Optimization note
// Keep a cumm array containing product of the first i items
// and use this array to find the ranges with product j

std::set<int> sik;

enum quaternion {
  u, mu, i, mi, j, mj, k, mk
};
static quaternion prod[8][8];

void init()
{
  prod[mi][i] = prod[mj][j] = prod[mk][k] = u;
  prod[ i][i] = prod[ j][j] = prod[ k][k] = mu;
  prod[ u][i] = prod[ j][k] = prod[mk][j] = i;
  prod[mu][i] = prod[mj][k] = prod[ k][j] = mi;
  prod[ u][j] = prod[mi][k] = prod[ k][i] = j;
  prod[mu][j] = prod[ i][k] = prod[mk][i] = mj;
  prod[ u][k] = prod[ i][j] = prod[mj][i] = k;
  prod[mu][k] = prod[mi][j] = prod[ j][i] = mk;

  prod[i][ u] = i;
  prod[j][ u] = j;
  prod[k][ u] = k;
  prod[i][mu] = mi;
  prod[j][mu] = mj;
  prod[k][mu] = mk;
  prod[i][mi] = u;
  prod[j][mi] = k;
  prod[k][mi] = mj;
  prod[i][mj] = mk;
  prod[j][mj] = u;
  prod[k][mj] = i;
  prod[i][mk] = j;
  prod[j][mk] = mi;
  prod[k][mk] = u;
}

static inline quaternion conv(char ch) {
  return ch == 'i' ?  i : (ch == 'j' ? j : k);
}

bool can_k(int idx) {
  return sik.find(idx) != sik.end();
}

bool can_jk(const std::string &s, int idx, int len) {
  quaternion v = u;
  while(idx < len - 1) {
    v = prod[v][conv(s[idx++])];
	if(v == j && can_k(idx) ) return true;
  }
  return false;
}

bool can_ijk(const std::string &s, int len) {
  quaternion v = u;

  for(int idx = 0; idx < len - 2; ++idx) {
    v = prod[v][conv(s[idx])];
	if(v == i && can_jk(s, idx + 1, len) ) return true;
  }
  return false;
}

static void exec(int tc) {
  int L, X;
  std::string str, s;

  cin >> L >> X >> str;
  s.reserve(L * X);
  while(X--) s += str;

  quaternion v = u;
  for(X = static_cast<int>( s.length() ) - 1; X > 1; --X) {
    v = prod[conv(s[X])][v];
	if(v == k) sik.insert(X);
  }

  if( can_ijk( s, static_cast<int>( s.length() ) ) ) cout << "Case #" << tc << ": YES\n";
  else cout << "Case #" << tc << ": NO\n";
  sik.clear();
}

int main()
{
  int T;
  std::ios_base::sync_with_stdio(false);
  init();
  cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    exec(tc);
  }
}

