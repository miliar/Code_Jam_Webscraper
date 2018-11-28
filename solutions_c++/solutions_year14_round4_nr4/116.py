#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
 
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define frr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define fr(a,b) frr(a,0,b)
#define rp fr
#define ms(a,b) memset((a), (b), sizeof(a))
#define cl ms
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

const int INF = 0x3f3f3f3f;
typedef long long ll;

using namespace std;

int m, n, ans, cnt[10], ans2;
string str[20];
vector<string> vec[10];
char ch[20];

int pref(string &a, string &b) {
  int len = min(a.size(), b.size()), ret = 0;
  while (ret < len && a[ret] == b[ret]) ret++;
  return ret;
}

void add(string s, int x) {
  if (vec[x].empty()) cnt[x] += s.size()+1;
  else cnt[x] += s.size() - pref(s, vec[x].back());
  vec[x].push_back(s);
}

void remove(int x) {
  string s = vec[x].back();
  vec[x].pop_back();
  int sz = vec[x].size();
  if (sz == 0) 
    cnt[x] -= s.size()+1;
  else cnt[x] -= s.size() - pref(s, vec[x].back());
}

void proc(int l) {
  if (l == m) {
    int opt = 0;
    fr(x, n) opt += cnt[x];
/*    if (7 <= opt) {
      fr(x, n) {
        fr(y, vec[x].size()) cerr << vec[x][y] << ' ';
        cerr << '\n';
      }
      cerr << '\n';
    }*/
    if (opt == ans) ans2++;
    else if (opt > ans) {
      ans = opt;
      ans2 = 1;
    }
    return;
  }
  fr(x, n) {
    add(str[l], x);
    proc(l+1);
    remove(x);
  }
}

int main() {
  int t, cn = 1;
  sc(t);
  while (t--) {
    sc2(m, n);
    fr(x, m) {
      scs(ch);
      str[x] = string(ch);
    }
    sort(str, str+m);
    fr(x, n) {
      vec[x].clear();
      cnt[x] = 0;
    }
    ans = -1; ans2 = 1;
    proc(0);
    printf("Case #%d: ", cn++);
    printf("%d %d\n", ans, ans2);
  }
  return 0;
}

