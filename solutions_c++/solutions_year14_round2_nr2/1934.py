#include <iomanip>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>

#define FR(i,en) for(int i=0; i<(en); i++)
#define FRR(i,en) for(int i=(en-1); i>=0; i--)
#define FOR(i,st,en) for(int i=(st); i<(en); i++)
#define FORR(i,st,en) for(int i=(en-1); i>=(st); i--)
#define FRI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define ALL(c) (c).begin(), (c).end()
#define SZ(i) i.size()
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define PI 3.1415926535897932384626433832795

typedef long long ll;
using namespace std;

int main()
{
  cout << setiosflags(ios::fixed) << setprecision(10);  //correct double
  int tcn, N, A, B, K;
  long long res;
  string s;
  cin >> tcn;
  FR(tc,tcn) {
    cout << "Case #" << tc + 1 << ": ";
    cin >> A >> B >> K;
    res=0;
    FR(i,A) FR(j,B) FR(k,K) res+=(i&j)==k;
    cout << res<<endl;
  }
}
