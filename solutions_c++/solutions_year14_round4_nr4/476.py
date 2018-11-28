#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef long double ld;

int M, N, Nodes;
ll Cnt;
int Idx[8];
vector<string> S;
void dfs(int x, int nodes, int bits) {
  if (x == M) {
    if (bits != (1<<N) - 1) return;
    if (nodes > Nodes) {
      Nodes = nodes;
      Cnt = 0;
    }
    if (nodes == Nodes) Cnt++;
    return;
  }

  int i, j, k;
  fr (i, N) {
    int overlap = 0;
    fr (j, x) if(Idx[j] == i) {
      int len = min(SZ(S[j]), SZ(S[x]));
      fr (k, len) if (S[j][k] != S[x][k]) break;
      overlap = max(overlap, k);
    }
    Idx[x] = i;
    dfs(x + 1, nodes + SZ(S[x]) - overlap, bits | (1 << i));
  }
}

int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    int i;
    S.clear();
    cin >> M >> N;
    fr (i, M) {
      string s;
      cin >> s;
      S.pb(s);
    }
    Nodes = 0;
    Cnt = 0;
    dfs(0, 0, 0);
    cout << "Case #" << cn << ": " << Nodes + N << " " << Cnt << endl;
  }
  return 0;
}
