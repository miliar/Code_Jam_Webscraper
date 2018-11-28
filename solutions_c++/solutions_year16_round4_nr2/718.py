#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

vector<int> convert(int index, int K)
{
  vector<int> ans;
  for (int i = 0; i < K; i++) {
    if ((index & (1 << i)) != 0) {
      ans.push_back(i);
    }
  }
  return ans;
}

long double Ptie(int N, int K, vector<long double> P, vector<int> index)
{
  //cout << "Ptie\n";
  //cout << N << "\n" << K << "\n";
  //for (int i = 0; i < P.size(); i++) {
  //  cout << P[i] << "\t";
  //}
  //cout << "\n";
  //for (int i = 0; i < index.size(); i++) {
  //  cout << index[i] << "\t";
  //}
  //cout << "\n";
  long double ans = 0;
  for (int i = 0; i < (1 << K); i++) {
    vector<int> i2 = convert(i, K);
    if (i2.size() == K / 2) {
      long double temp = 1;
      for (int j = 0; j < K; j++) {
        if ((i & (1 << j)) != 0) {
          temp *= P[index[j]];
        }
        else {
          temp *= (1 - P[index[j]]);
        }
      }
      ans += temp;
    }
  }
  //cout << ans << "\n";
  return ans;
}

long double solve(int N, int K, vector<long double> P, vector<int> index)
{
  if (index.size() == K) {
    return Ptie(N, K, P, index);
  }
  int begin = 0;
  if (!index.empty()) {
    begin = index[index.size() - 1] + 1;
  }
  long double ans = 0;
  for (int i = begin; i < N; i++) {
    index.push_back(i);
    ans = max(ans, solve(N, K, P, index));
    index.pop_back();
  }
  return ans;
}

long double solve(int N, int K, vector<long double> P)
{
  vector<int> index;
  return solve(N, K, P, index);
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, K;
    cin >> N >> K;
    vector<long double> P;
    for (int i = 0; i < N; i++) {
      long double p;
      cin >> p;
      P.push_back(p);
    }
    cout << "Case #" << t << ": " << solve(N, K, P) << "\n";
  }
  return 0;
}

