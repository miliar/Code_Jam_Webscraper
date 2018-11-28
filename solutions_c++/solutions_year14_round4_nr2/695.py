#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int T,N;

int main() {
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> N;
    vector<int> V(N);
    vector<pair<int,int> > P;
    int vymeny = 0;
    for(int n = 0; n < N; ++n) {
      cin >> V[n];
      P.push_back(make_pair(V[n], n));
    }
    sort(P.begin(),P.end());

    for(int i = 0; i < N - 1; ++i) {
      int v = 0;
      for(int j = 0; j < P[i].second; ++j)
        if (V[j] > P[i].first) ++v;
      vymeny += min(v, N - i - 1 - v);
    }
    cout << "Case #" << t << ": " << vymeny << endl;
  }
  return 0;
}
