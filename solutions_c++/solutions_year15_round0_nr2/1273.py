

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

using namespace std;

typedef long long int LL;

template<class T>
ostream& operator<<(ostream& a, const vector<T>& v) {
    a << "{";
    if (v.size()>0) a << v[0];
    for (int i=1; i<v.size(); i++) a << ", " << v[i];
    a << "}";
    return a;
}

int bestPossible(int height, const vector<int>& heights) {
  LL min_ans = 0;
  int max_height = 0;
  for (int i=0; i<heights.size(); i++) {
    int nsplits = ((heights[i]-1) / height);
    if (nsplits > 0) {
      min_ans += nsplits;
      int curr_h = ((heights[i]-1) / (nsplits+1)) + 1;
      max_height = max(max_height, curr_h);
    } else {
      max_height = max(max_height, heights[i]);
    }
  }
  min_ans += max_height;
  return min_ans;
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    cin.tie(NULL);
    int TC,N;
    cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
      cin >> N;
      vector<int> heights(N);
      rep(i,N) cin >> heights[i];
      int ans = 10000001;
      for (int h=1; h<=1000; h++) {
        int curr_ans = bestPossible(h, heights);
        //cout << h << " " << curr_ans << endl;
        ans = min(ans, curr_ans);
      }
      cout << "Case #" << tc << ": " << ans << endl;
    }
}
