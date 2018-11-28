#include<iostream>
#include<set>
#include<algorithm>
#include<vector>
#include<queue>

using namespace std;

int N,X,T;

int main() {
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    int pocet = 0;
    cin >> N >> X;
    vector<int>S(N);
    priority_queue<int> R;
    for(int n = 0; n < N; ++n) {
      cin >> S[n];
    }
    sort(S.begin(),S.end());
    reverse(S.begin(),S.end());
    for(int i = 0; i < (int)S.size(); ++i) {
      if (R.empty() || R.top() < S[i]) {
        ++pocet;
        if (X - S[i] > 0) R.push(X - S[i]);
      } else {
        R.pop();
      }
    }
    cout << "Case #" << t << ": " << pocet << endl;
  }
}
