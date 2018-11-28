#include <bits/stdc++.h>
using namespace std;


int main() {
  cout << fixed << setprecision(6);

  int num_cases;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    
    int n, k;
    cin >> n >> k;
    vector<int> S(n - k + 1);
    for (int i = 0; i < n - k + 1; ++i)
      cin >> S[i];

    vector<pair<int, int>> intervals;
    for (int start = 0; start < k; ++start) {
      int lo = 0, hi = 0, curr = 0;
      for (int i = start + k; i < n; i += k) {
        curr = curr + S[i - k + 1] - S[i - k];
        lo = min(lo, curr);
        hi = max(hi, curr);
      }
//      cout << lo << " " << hi << endl;
      intervals.emplace_back(lo, hi);
    }

    int needsplus = (S[0] % k + k) % k;

    
    for (int i = 0; i < needsplus; ++i) {
      ++intervals[i].first;
      ++intervals[i].second;
    }
    //*/

    int maxlo = intervals[0].first;
    for (int i = 0; i < k; ++i)
      maxlo = max(maxlo, intervals[i].first);
    
    long long added = 0;
    long long canadd = 0;
    int maxl = 0;
    for (int i = 0; i < k; ++i) {
  //    cout << maxl << " " << intervals[i].second << " " << intervals[i].first << endl;
      maxl = max(maxl, intervals[i].second - intervals[i].first);
      added += maxlo - intervals[i].first;
    }
    for (int i = 0; i < k; ++i) 
      canadd += maxl - (intervals[i].second - intervals[i].first);
    int toadd = (k - (added % k) ) % k;
  
    assert(0 <= toadd and toadd < k);
    assert(0 <= canadd and canadd <= 2e9);

    if (toadd > canadd)
      maxl++;

    cout << "Case #" << case_num << ": ";
    cout << maxl << endl;
  }
}
