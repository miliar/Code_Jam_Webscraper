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

int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    int i, j, N, x;
    vector<p2> list;
    cin >> N;
    fr (i, N) {
      cin >> x;
      list.pb(MP(x, i));
    }
    sort(list.begin(), list.end());
    int res = 0;
    for (i = N - 1; i >= 0; --i) {
      int a = 0, b = 0;
      for (j = i + 1; j < N; ++j) {
        if (list[i].S < list[j].S) a++;
        else b++;
      }
      res += min(a, b);
    }
    cout << "Case #" << cn << ": " << res << endl;
  }
  return 0;
}
