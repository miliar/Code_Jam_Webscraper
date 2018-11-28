#include <bits/stdc++.h>
using namespace std;

typedef  long long ll;

int main() {
  cout << fixed << setprecision(6);

  int num_cases;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    
    int n;
    cin >> n;
    vector<pair<ll, ll>> f(n);
    for (int i=0; i<n; ++i)
      cin >> f[i].first;
    for (int i=0; i<n; ++i)
      cin >> f[i].second;
  
    long long zerosetsum;

    vector<long long> result;
    while (true) {
      /*
      long long sum = 0;
  
      for (auto e : f) {
        cout << e.first << " " << e.second << endl;
        sum += e.second;
      }
      cout << sum << endl;
      */
      if (f[0].second > 1) {
        result.push_back(0);
        for (auto & p : f) {
          assert(p.second % 2 == 0);
          p.second /= 2;
        }
        continue;
      }
      if (f.size() == 1) {
        // assert(f[0].first == 0);
        zerosetsum = f[0].first;
        assert(f[0].second == 1);
        break;
      }
      assert(f.size() > 1);
      long long smallest = f[1].first - f[0].first;
      
      /*
      if (f[0].first < 0)
        result.push_back(-smallest);
      else
      */
      result.push_back(smallest);

      //cout << "next elem: " << smallest << endl;

      map<ll, ll> m1, m2;
      for (int i = 0; i < f.size(); ++i) {
        assert(f[i].second >= m2[f[i].first]);
        f[i].second -= m2[f[i].first];
        if (f[i].second > 0) {
          m1[f[i].first] += f[i].second;
          m2[f[i].first + smallest] += f[i].second;
        }
      }
      //for (auto e : m1) cout << "m1 " << e.first << " " << e.second << endl;
      //for (auto e : m2) cout << "m2 " << e.first << " " << e.second << endl;

      //if (f[0].first < 0) swap(m1, m2);
      f.clear();
      for (auto e : m1)
        if (e.second > 0) f.push_back(e);
    }

    

    assert(zerosetsum <= 0);

    zerosetsum = -zerosetsum;
  
    sort(result.begin(), result.end());
    
    vector<map<ll, ll>> dp(result.size() + 1);
    dp[0][0] = 1;
    for (int i = 0; i < result.size(); ++i) {
      dp[i + 1] = dp[i];
      for (auto e : dp[i])
        dp[i + 1][e.first + result[i]] += e.second;
    }

    vector<ll> rresult;
    for (int i = result.size() - 1; i >= 0; --i) {
      ll cand = result[i];
      assert(dp[i+1][zerosetsum] > 0);
      if (dp[i][zerosetsum - cand] > 0) {
        zerosetsum -= cand;
        rresult.push_back(-cand);
      } else {
        rresult.push_back(cand);
      }
    }


        
    sort(rresult.begin(), rresult.end()); 
    
    cout << "Case #" << case_num << ":";
    for (ll x : rresult)
      cout << " " << x;
    cout <<  endl;
  }
}
