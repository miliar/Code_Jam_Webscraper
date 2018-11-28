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

const int MOD = 1000000007;

int main(){
  int T; cin >> T;
  rep(case_loop, 1, T+1){
    int mx; string s; cin >> mx >> s;
    int cnt = 0, acc = 0;
    rep(i, 0, si(s)){
      int num = (int)(s[i] - '0');
      if(acc >= i) acc += num;
      else {
	cnt += i - acc;
	acc = i + num;
      }
    }
    printf("Case #%d: %d\n", case_loop, cnt);
  }
  return 0;
}
