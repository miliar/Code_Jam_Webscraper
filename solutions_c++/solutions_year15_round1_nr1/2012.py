#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <functional>
#include <cmath>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define rep(i, m, n) for(int i = m; i < n; i++)
#define repr(i, n, m) for(int i = n; i >= m; i--)
#define rep1(i, x) for(int i = 0; i < (int)(x).size(); i++)
#define mkp(v,x,y) for(int i=0;i<(int)(x).size();i++)v.push_back(make_pair(x[i],y[i]))
#define pb push_back
#define mp make_pair
#define si(x) ((int)(x).size())
#define al(x) x.begin(), x.end()
#define x first
#define y second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int, int> PII;

const int INF = 1 << 31;
const int MOD = 1000000007;

int m[10001];

int main(){
  int T; cin >> T;
  LL ans1, ans2;
  rep(case_loop, 1, T+1){
    int N; cin >> N;
    rep(i, 0, N) scanf("%d", m+i);
    ans1 = 0;
    rep(i, 0, N-1){
      if(m[i] > m[i+1]) ans1 += m[i] - m[i+1];
    }
    double slope = 0;
    rep(i, 0, N-1){
      slope = max(slope, (m[i] - m[i+1]) / 10.0);
    }
    ans2 = 0;
    rep(i, 0, N-1){
      ans2 += min((LL)m[i], (LL)(slope * 10));
    }
    printf("Case #%d: %lld %lld\n", case_loop, ans1, ans2);
  }
  return 0;
}
