#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

int main() {
  int T, C = 1;
  scanf("%d", &T);
  while (T--) {
    printf("Case #%d: ", C++);
    int N;
    scanf("%d", &N);
    vector<string> cars;
    vector<int> index;
    for (int i = 0; i < N; i++) {
      char temp[999];
      scanf("%s", temp);
      string s;
      for (int j = 0; temp[j]; j++) {
        if (!j || temp[j] != temp[j - 1]) {
          s.insert(s.end(), temp[j]);
        }
      }
      cars.push_back(s);
      index.push_back(i);
    }
    long long ans = 0;
    do {
      int last = -1;
      bool check[26] = {}, gg = false;
      for (int i = 0; i < index.size() && !gg; i++) {
        for (int j = 0; cars[index[i]][j] && !gg; j++) {
          int c = cars[index[i]][j] - 'a';
          if (c != last) {
            if (check[c]) {
              gg = true;
            }
            check[c] = true;
          }
          last = c;
        }
      }
      ans += !gg;
    } while (next_permutation(index.begin(), index.end()));
    printf("%lld\n", ans);
  }
  return 0;
}
