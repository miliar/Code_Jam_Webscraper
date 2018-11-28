#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 2500;
int cnt[maxn+1];
int n;

int main() {
  int tc;
  scanf("%d", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    memset(cnt, 0, sizeof cnt);
    scanf("%d", &n);
    for(int i = 0; i < 2 * n - 1; i++) {
      for(int j = 0; j < n; j++) {
	int num;
	scanf("%d", &num);
	cnt[num]++;
      }
    }
    vector<int> ans;
    for(int i = 1; i <= maxn; i++) {
      if(cnt[i] & 1)
	ans.push_back(i);
    }
    sort(ans.begin(), ans.end());
    printf("Case #%d:", kase);
    for(int i = 0; i < ans.size(); i++) {
      printf(" %d", ans[i]);
    }
    printf("\n");
  }
  return 0;
}
