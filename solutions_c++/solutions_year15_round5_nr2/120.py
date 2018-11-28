#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";

    int N, K;
    cin >> N >> K;
    vector<int> S(N - K + 1);
    for (int i = 0; i < N - K + 1; i++) {
      cin >> S[i];
    }

    int bot = 0;
    vector<pair<int, int> > H;
    for (int i = 0; i < K; i++) {
      int x = 0;
      int mn = 0;
      int mx = 0;
      for (int j = i; j + 1 < S.size(); j += K) {
        x += S[j + 1] - S[j];
        mn = min(x, mn);
        mx = max(x, mx);
      }
      H.push_back(make_pair(mn, mx));
      bot = max(bot, mx - mn);
    }

    int lo = bot;
    int hi = 20020;
    while (lo < hi) {
      int md = (lo + hi) / 2;

      bool ok = false;
      for (int base = -10000; base <= 10000 && !ok; base++) {
        int mnv = 0;
        int mxv = 0;
        for (int i = 0; i < K; i++) {
          mnv += base - H[i].first;
          mxv += base + md - H[i].second;
        }
        ok = mnv <= S[0] && S[0] <= mxv;
      }
      if (ok) {
        hi = md;
      } else {
        lo = md + 1;
      }
    }
    cout << lo << endl;
  }
  return 0;
}
