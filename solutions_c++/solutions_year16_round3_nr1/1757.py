#include <iostream>
#include <string>
#include <algorithm>
#include <vector>


using namespace std;


int main() {
  int T, N;
  scanf("%d", &T);
  for (int qq = 1; qq <= T; qq++) {
    vector<pair<int, char> > v;
    scanf("%d", &N);
    int acc = 0;
    for (int i = 0; i < N; i++) {
      int n;
      scanf("%d", &n);
      acc += n;
      v.push_back(make_pair(n, 'A' + i));
    }
    vector<string>ans;
    sort(v.rbegin(), v.rend());
    if (acc & 1) {
      string s;
      s += v[0].second;
      ans.push_back(s);
      v[0].first -= 1;
    }
    while (1) {
      sort(v.rbegin(), v.rend());
      if (!v[0].first) break;
      string s;
      s += v[0].second;
      v[0].first -= 1;
      if (v[0].first > v[1].first) {
        s += v[0].second;
        v[0].first -= 1;
      } else {
        s += v[1].second;
        v[1].first -= 1;
      }
      ans.push_back(s);
    }
    string s;
    int i;
    for (i = 0; i < ans.size()-1; i++) {
      s += ans[i] + " ";
    }
    s += ans[i];
    printf("Case #%d: %s\n", qq, s.c_str());
  }
  return 0;
}
