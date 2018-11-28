#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

typedef pair<int, pair<int,int> > PII;

const int maxn = 2000 + 10;
const long long MOD = 1000002013;

int n, m;
vector<PII> info;

int ans;
long long cost, new_cost;
vector<pair<int,int> > st, en;

void init() {
  info.clear();
  cost = 0;
  scanf("%d%d", &n, &m);
  for (int i = 0; i < m; ++i) {
    int o, e, p;
    scanf("%d%d%d", &o, &e, &p);
    info.push_back(make_pair(o, make_pair(e, p)));
    long long single_cost = (2LL * n - (e-o+1) + 2) * ((e-o+1) - 1) / 2 % MOD;
    cost = (cost + single_cost * p) % MOD;
  }
}

void add_new() {
  sort(en.begin(), en.end());
  /*for (int i = 0; i < st.size(); ++i)
    cout << "st " << st[i].first << " " << st[i].second << endl;
  for (int i = 0; i < en.size(); ++i)
    cout << "en " << en[i].first << " " << en[i].second << endl;*/
  
  int len = st.size();
  for (int j = 0; j < len; ++j) {
    int i;
    for (i = 0; i < len; ++i)
      if (i == len - 1 || st[i + 1].first > en[j].first)
        break;
    while (en[j].second > 0) {
      int k = en[j].first - st[i].first + 1;
      long long single_cost = (2LL * n - k + 2) * (k - 1) / 2 % MOD;
      int p = min(st[i].second, en[j].second);
      new_cost = (new_cost + single_cost * p) % MOD;
      //cout << "match " << st[i].first << " "<< en[j].first << " "<< p << endl;
      st[i].second -= p;
      en[j].second -= p;
      while (st[i].second == 0)
        --i;
    }
  }
}

void solve() {
  sort(info.begin(), info.end());
/*  for (int i = 0; i < m; ++i)
    cout << info[i].first << " "<< info[i].second.first << " " << info[i].second.second << endl;*/
  new_cost = 0;
  for (int i = 0, last = -1; i < m; ++i) {
    int o = info[i].first;
    int e = info[i].second.first;
    int p = info[i].second.second;
    if (last < o) {
      if (last != -1) {
        add_new();
      }
      st.clear();
      en.clear();
    }
    st.push_back(make_pair(o, p));
    en.push_back(make_pair(e, p));
    last = max(last, e);
  }
  add_new();
  ans = (cost - new_cost + MOD) % MOD;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tcase;
  scanf("%d", &tcase);
  for (int t = 1; t <= tcase; ++t) {
    init();
    solve();
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
