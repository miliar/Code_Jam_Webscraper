#include <algorithm>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <iostream>
#include <tuple>

using namespace std;

int nums[26], n;

bool check() {
  int sum = 0;
  for (int i = 0; i < n; ++i)
    sum += nums[i];
  for (int i = 0; i < n; ++i) {
    if (nums[i] > sum / 2) {
      // printf("fuck %d, %c, total: %d\n", nums[i], 'A' + i, sum);
      return false;
    }
  }
  return true;
}

int main(void) {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tc;
  scanf("%d", &tc);
  for (int cas = 1; cas <= tc; ++cas) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
      scanf("%d", &nums[i]);
    vector<string> answer;
    while (1) {
      if (!check()) {
        printf("error case %d\n", cas);
        break;
      }
      vector<pair<int, int> > items;
      for (int i = 0; i < n; ++i) {
        if (nums[i] > 0)
          items.push_back(make_pair(nums[i], i));
      }
      int m = items.size();
      if (m == 0)
        break;
      sort(items.begin(), items.end());
      string w = "";
      int index = items[m - 1].second;
      w += 'A' + index;
      nums[index]--;
      if (m >= 2) {
        index = items[m - 2].second;
        nums[index]--;
        if (check())
          w += 'A' + index;
        else
          nums[index]++;
      }
      answer.push_back(w);
    }
    printf("Case #%d:", cas);
    for (int i = 0; i < answer.size(); ++i)
      printf(" %s", answer[i].c_str());
    printf("\n");
  }
  return 0;
}
