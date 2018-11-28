#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T;
double C, F, X;

int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    cin >> C >> F >> X;
    double res = 0;
    int k = 0;
    while (1.0 - C/X >= (2 + k*F) / (2 + (k+1)*F)) {
      res += C / (2 + k*F);
      k++;
    }
    res += X / (2 + k*F);
    printf("Case #%d: %.7lf\n", cs, res);
  }
	return 0;
}
