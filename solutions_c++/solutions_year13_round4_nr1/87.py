#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

#define MOD 1000002013LL

pair<PII, int> A[1010];

Int F(Int st, Int e, Int k, Int N) {
  Int d = e-st;
  Int res = (2*N+1-d) * d / 2;
  res = ((res%MOD)*k) % MOD;
  return res;
}

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    int N, M;
    scanf("%d%d", &N, &M);
    vector<int> Stops;
    Int reso = 0;
    for (int i = 0; i < M; ++i) {
      int o, e, p;
      scanf("%d%d%d", &o, &e, &p);
      A[i].first.first = o;
      A[i].first.second = e;
      A[i].second = p;
      Stops.PB(o);
      Stops.PB(e);
      reso += F(o, e, p, N);
      while (reso >= MOD)
	reso -= MOD;
    }
    sort(A, A+M);

    Stops.PB(1);
    Stops.PB(N);
    sort(ALL(Stops));
    Stops.resize(unique(ALL(Stops)) - Stops.begin());

    priority_queue<PII> Qin;
    priority_queue<PII, vector<PII>, greater<PII> > Qout;
    Int res = 0;
    int p = 0;
    for (int i = 0; i < Stops.size(); ++i) {
      while (p < M && A[p].first.first == Stops[i]) {
	Qin.push(PII(A[p].first.first, A[p].second));
	Qout.push(PII(A[p].first.second, A[p].second));
	++p;
      }

      while (!Qout.empty() && Qout.top().first == Stops[i]) {
	int k = Qout.top().second;
	Qout.pop();
	while (k > 0) {
	  int ki = Qin.top().second;
	  int st = Qin.top().first;
	  Qin.pop();
	  int kk = min(ki, k);
	  ki -= kk;
	  k -= kk;
	  if (ki > 0)
	    Qin.push(PII(st, ki));
	  int e = Stops[i];
	  res += F(st, e, kk, N);
	  while (res >= MOD)
	    res -= MOD;
	}
      }
    }

    //    cout << "reso = " << reso << endl;
    //    cout << "res = " << res << endl;


    Int rr = ((reso - res) % MOD + MOD) % MOD;
    printf("Case #%d: %lld\n", t+1, rr);

  }


  return 0;
};
