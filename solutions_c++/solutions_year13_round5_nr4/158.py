#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;
typedef vector<bool> Vb;
typedef vector<Vb> Mb;
typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<ll> Vll;
typedef vector<Vll> Mll;
typedef vector<P> Vp;
typedef vector<Vp> Mp;
typedef vector<string> Vs;
typedef vector<Vs> Ms;
typedef vector<ld> Vd;

typedef set<int> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

template <class Ta, class Tb> inline Tb cast(Ta a) { SS ss; ss << a; Tb b; ss >> b; return b; };

const double EPS = 1e-9;
const int INF = 1000000000;
const int diri[8] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dirj[8] = { 0, 1, 0, -1, 1, 1, -1, -1 };

int N;
Vd dp;

void wait_time(int mask, Vi& v) {
  v = Vi(N, 0);
  for (int i = 0; i < N; ++i) {
    while ((mask>>((i + v[i])%N))&1) ++v[i];
  }
}

ld fun(int mask) {
  if (mask == (1<<N) - 1) return 0;
  ld &res = dp[mask];
  if (res >= 0) return res;
  res = 0;
  Vi v;
  wait_time(mask, v);
  for (int i = 0; i < N; ++i) {
    res += (N - v[i] + fun(mask | (1<<((i + v[i])%N))))/N;
  }
  return res;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(12);
  
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    string s;
    cin >> s;
    N = s.size();
    int mask = 0;
    for (int i = 0; i < N; ++i) {
      if (s[i] == 'X') mask |= 1<<i;
    }
    dp = Vd(1<<N, -1);
    cout << "Case #" << cas << ": " << fun(mask) << endl;
  }
}
