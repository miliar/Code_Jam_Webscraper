#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <cstdlib>
#include <utility>

using namespace std;

#define MOD 1000002013

int main() {
  int T; cin >> T;
  for(int tt = 1; tt <= T; tt++) {
    int NN, M; cin >> NN >> M;

    vector<int> xs;
    vector<pair<pair<int, int>, int> > A(M);
    for(int i = 0; i < M; i++) {
      cin >> A[i].first.first >> A[i].first.second >> A[i].second;
      xs.push_back(A[i].first.first);
      xs.push_back(A[i].first.second);
    }
    sort(xs.begin(), xs.end());
    xs.resize(unique(xs.begin(), xs.end()) - xs.begin());

    for(int i = 0; i < M; i++) {
      A[i].first.first = lower_bound(xs.begin(), xs.end(), A[i].first.first) -
                              xs.begin();
      A[i].first.second = lower_bound(xs.begin(), xs.end(), A[i].first.second) -
                              xs.begin();
    }
    sort(A.begin(), A.end());

    int N = xs.size();
    vector<int> CNT(N, 0);
    for(int i = 0; i < M; i++) {
      for(int j = A[i].first.first; j < A[i].first.second; j++) {
        CNT[j] += A[i].second;
      }
    }

    int result = 0;
    for(int i = 0; i < M; i++) {
      int len = xs[A[i].first.second] - xs[A[i].first.first];
      result += A[i].second *
           (NN * (NN + 1) / 2 - (NN - len) * (NN - len + 1) / 2);
    }
    
    for(int i = 0; i < N; i++) {
      int lj = i;
      int mxv = CNT[i];
      for(int j = i + 1; j < N; j++) {
        if(CNT[j] < mxv) {
          int len = xs[j] - xs[i];
          result -= (mxv - CNT[j]) * (
               NN * (NN + 1) / 2 - (NN - len) * (NN - len + 1) / 2);
          for(int k = lj; k < j; k++) {
            CNT[k] -= mxv;
          }
          lj = j;
          mxv = CNT[j];
        }
      }
    }

    cout << "Case #" << tt << ": " << result << endl;
  }
  return 0;
}
