#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>

using namespace std;

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); k++)
#define FORE(k,a,b) for(typeof(a) k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define EXIST(s,e) ((s).find(e)!=(s).end())

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1e+9;
const double EPS = 1e-10;
const double PI = acos(-1.0);

double solve(double C, double F, double X) {
  if(X <= C) return X / 2.0;

  double res = X / 2.0;
  int nfarm = 1;
  while(true) {
    double time = 0.0;
    REP(i, nfarm) {
      time += C / (2.0 + i * F);
    }
    time += X / (2.0 + nfarm * F);

    if(time < res) res = time;
    else break;

    nfarm++;
  }

  return res;
}


int main()
{
  int T; cin >> T;
  REP(tcase, T) {
    double C, F, X;
    cin >> C >> F >> X;

    printf("Case #%d: %.7f\n", tcase + 1, solve(C, F, X));
  }
  
  return 0;
}
