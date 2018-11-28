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

int Board[100][100];
int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    int i, j, k, R, C;
    cin >> R >> C;
    fr (i, R) fr (j, C) cin >> Board[i][j];
    bool valid = true;
    fr (i, R) fr (j, C) {
      bool row = true, col = true;
      fr (k, C) if (Board[i][j] < Board[i][k]) row = false;
      fr (k, R) if (Board[i][j] < Board[k][j]) col = false;
      if (!row && !col) valid = false;
    }
    cout << "Case #" << cn << ": " << (valid ? "YES" : "NO") << endl;
  }
  return 0;
}
