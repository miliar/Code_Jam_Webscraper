#include <bits/stdc++.h>
using namespace std;


int main() {
  cout << fixed << setprecision(6);

  int num_cases;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    int n, d;
    
    cin >> n >> d;
    vector<int> S(n), M(n);

    int as, cs, rs, am, cm, rm;
    cin >> S[0] >> as >> cs >> rs;
    cin >> M[0] >> am >> cm >> rm;
    for (int i = 1; i < n; ++i) {
      S[i] = (S[i - 1] * as + cs) % rs;
      M[i] = (M[i - 1] * am + cm) % rm;
    }
    for (int i = 1; i < n; ++i)
      M[i] %= i;


    vector<int> Slo = S, Shi = S;
    for (int i = 1; i < n; ++i) {
      Slo[i] = min(Slo[M[i]], Slo[i]);
      Shi[i] = max(Shi[M[i]], Shi[i]);
    }

    vector<pair<int, int>> events;

    for (int i = 0; i < n; ++i) {
      int minmin = Shi[i] - d;
      int maxmin = Slo[i];
      if (minmin <= maxmin) {
        events.emplace_back(minmin, 0);
        events.emplace_back(maxmin, 1);
      }
    }

    /*
    for (int i = 0; i < n; ++i) {
      cout << M[i] <<  " " << S[i] << " " << Slo[i] << " " << Shi[i] << endl;
    }
    */

    sort(events.begin(), events.end());

    int count = 0, best = 0;
    for (auto e : events) {
      // cout << "event " << e.first << " " << e.second << endl;
      if (e.second == 0)
        ++count;
      else
        --count;
      best = max(best, count);
    }


    cout << "Case #" << case_num << ": ";
    cout << best << endl;
  }
}
