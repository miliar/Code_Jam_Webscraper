#include<cstdio>
#include<string>
#include<set>
#include<vector>
using namespace std;

int m, n;
char s[1005][1005];
string S[1005];
int mm, cnt;

void calc(vector<int>& v) {
  int ret = 0;
  vector<string> V[10];
  for (int i = 0; i < m; ++i) {
    V[v[i]].push_back(S[i]);
  }
  for (int i = 0; i < n; ++i) {
    if (V[i].empty()) {
      continue;
    }
    set<string> SS;
    for (int j = V[i].size() - 1; j >= 0; --j) {
      string ss = V[i][j];
      for (int k = ss.length(); k >= 0; --k) {
        SS.insert(ss.substr(0, k));
      }
    } 
    ret += SS.size();
  }
  if (ret == mm) {
    ++cnt;
  } else if (ret > mm) {
    mm = ret;
    cnt = 1;
  }
}

void dfs(vector<int>& v, int now) {
  if (now == m) {
    calc(v);
    return;
  }
  for (int i = 0; i < n; ++i) {
    v[now] = i;
    dfs(v, now + 1);
  }
}

int T;

int main() {
  freopen("D-small-attempt2.in", "r", stdin);
  freopen("D.out", "w", stdout);
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    fprintf(stderr, "%d\n", test);
    mm = cnt = 0;
    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; ++i) {
      scanf("%s", s[i]);
      S[i] = s[i];
    }
    vector<int> v(m);
    dfs(v, 0);
    printf("Case #%d: %d %d\n", test, mm, cnt);
  }
  return 0;
}

