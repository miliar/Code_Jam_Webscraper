#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

typedef pair<int, int> PII;

int n;
int f[1005];
int T;
int a[1005];
vector<PII> v;

int calcr(int x) {
  int ret = 0;
  for (int i = x + 1; i < n; ++i) {
    if (v[i].second > v[x].second) {
      ++ret;
    }
  }
  return ret;
}

int calcl(int x) {
  int ret = 0;
  for (int i = x + 1; i < n; ++i) {
    if (v[i].second < v[x].second) {
      ++ret;
    }
  }
  return ret;
}


int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B.out", "w", stdout);
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    v.clear();
    scanf("%d", &n);
    int in = 0;
    for (int i = 0; i < n; ++i) {
      scanf("%d", &a[i]);
      v.push_back(make_pair(a[i], i));
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < n; ++i) {
      f[i] = (i == 0 ? 0 : f[i - 1]) + min(calcr(i), calcl(i));
    }
    printf("Case #%d: %d\n", test, f[n - 1]);
  }
  return 0;
}

