#ifndef CSL_STD_H_
#define CSL_STD_H_ 20151122L
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef std::pair<int,int> pii;
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef std::vector<pii> vpii;

#define rep(i,a,b) for(auto i=a,i##_n=b;i<i##_n;++i)
#define per(i,a,b) for(auto i=b,i##_n=a;i-->i##_n;)
#define endl '\n'

#endif

int n, r, p, s;
int t[256];

string dfs(int l, int r, int c) {
  if (l == r) {
    return string(1, char(c));
  }
  int m = (l + r) >> 1;
  string x = dfs(l, m, c);
  string y = dfs(m + 1, r, t[c]);
  if (x > y) swap(x, y);
  return x + y;
}

bool count(string& str) {
  int rr = 0, ss = 0, pp = 0;
  int temp=str.length();
  for (int i=0;i<temp;i++) {
    char c=str[i];
    if (c == 'R') ++rr;
    if (c == 'S') ++ss;
    if (c == 'P') ++pp;
  }
  return rr == r && ss == s && pp == p;
}

string check() {
  string res = "Z";
  string x = dfs(1, 1 << n, 'R');
  if (count(x)) res = min(res, x);
  string y = dfs(1, 1 << n, 'S');
  if (count(y)) res = min(res, y);
  string z = dfs(1, 1 << n, 'P');
  if (count(z)) res = min(res, z);
  return res;
}

//@ Main Function
int main() {
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
  t['R'] = 'S'; t['S'] = 'P'; t['P'] = 'R';
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int a, b = 1;
  for(std::cin >> a; a; --a, ++b) {
    std::cout << "Case #" << b<< ": ";
    cin >> n >> r >> p >> s;
    string ans = check();
    cout << (ans == "Z" ? "IMPOSSIBLE" : ans) << endl;
  }
  return 0;
}

