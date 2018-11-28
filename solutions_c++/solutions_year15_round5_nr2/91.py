#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int main()
{
  int tcase = 0;
  ifstream fin("z.in");
  ofstream fout("z.out");
  fin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    int i,j;
    //istringstream strin();
    int n, k;
    int sum[1001];
    fin >> n >> k;
    for (i = 0; i <= n-k; i++) fin >> sum[i];
    int low[100] = {};
    int high[100] = {};
    int s0 = sum[0];
    int ans = 0;
    for (i = 0; i < k; i++) {
      int cul = 0;
      for (j = i; j+1 <= n-k; j += k) {
        cul += sum[j+1]-sum[j];
        if (cul < low[i]) low[i] = cul;
        if (cul > high[i]) high[i] = cul;
      }
      //cerr << i << ' ' << low[i] << ' ' << high[i] << endl;
      high[i] -= low[i];
      s0 += low[i];
      if (high[i] > ans) ans = high[i];
    }
    s0 %= k;
    if (s0 < 0) s0 += k;

    int extra = 0;
    for (i = 0; i < k; i++) {
      extra += ans - high[i];
    }
    cerr << tind << ": prelim ans " << ans << " extra " << extra << " s0rem "
         << s0 << endl;
    if (extra < s0) ans++;
    fout << "Case #" << tind << ": " << ans << endl;
  }
  return 0;
}
