#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <cstring>
#include <stack>
#include <bitset>

using namespace std;

#define NMAX 2147483647
#define LMAX 9223372036854775807LL
#define pb push_back
#define pob pop_back
#define mp make_pair
#define st first
#define nd second
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(a);i>(b);--i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)

int mapa[5][5];
int f[10001][10001];

bool solve(int N) {
  for (int i = 1; i < N - 1; i++) {
    for (int j = i + 1; j < N; j++) {
      if (f[0][i - 1] == 2 && f[i][j-1] == 3 && f[j][N-1] == 4) return true;
    }
  }
  return false;
}

int main() {
  freopen("input.txt","r",stdin);
  freopen("out.txt","w",stdout);
  // define shit
  // i = 2, j = 3, k = 4
  mapa[1][1] = 1;
  mapa[1][2] = 2;
  mapa[1][3] = 3;
  mapa[1][4] = 4;

  mapa[2][1] = 2;
  mapa[2][2] = -1;
  mapa[2][3] = 4;
  mapa[2][4] = -3;

  mapa[3][1] = 3;
  mapa[3][2] = -4;
  mapa[3][3] = -1;
  mapa[3][4] = 2;

  mapa[4][1] = 4;
  mapa[4][2] = 3;
  mapa[4][3] = -2;
  mapa[4][4] = -1;

  int L, X, TS;
  string S, s;
  cin >> TS;
  for (int ts = 1; ts <= TS; ts++) {
    memset(f,0,sizeof(f));
    cin >> L >> X >> s;
    S = "";
    for (int i = 0; i < X; i++) S += s;
    for (int i = 0; i < S.length(); i++)
      if (S[i] == '1') S[i] = 1;
      else if(S[i] == 'i') S[i] = 2;
      else if(S[i] == 'j') S[i] = 3;
      else S[i] = 4;
    for (int i = 0; i < S.length(); i++) {
      for (int j = i; j < S.length(); j++) {
        if (i == j) f[i][j] = S[i];
        else {
          f[i][j] = mapa[abs(f[i][j - 1])][S[j]];
          if (f[i][j - 1] < 0) f[i][j] *= -1;
        }
      }
    }
    string ans = (solve(S.length()) ? "YES" : "NO");
    cout << "Case #" << ts << ": " << ans << endl;
  }

  return 0;
}
