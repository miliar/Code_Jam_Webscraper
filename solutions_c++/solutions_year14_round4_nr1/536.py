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
    int N, X, i, x;
    cin >> N >> X;
    vi list;
    fr (i, N) {
      cin >> x;
      list.pb(x);
    }
    sort(list.begin(), list.end());
    int res = 0, st = 0, en = N - 1;
    while (st <= en) {
      if (st == en) {
        res++;
        break;
      }
      
      if (list[st] + list[en] > X) {
        en--;
        res++;
      } else {
        res++;
        en--;
        st++;
      }
    }
    cout << "Case #" << cn << ": " << res << endl;
  }
  return 0;
}
