#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int N;
int pos[1001];

int memo[1001][1001];
int doit(int a, int b) {
  int& ret = memo[a][b];
  if (ret >= 0) return ret;
  int cur = min(a,b)-1;
  if (cur < 0) return ret = 0;
  ret = min(doit(cur, b) + pos[cur],
            doit(a, cur) + N-cur-1-pos[cur]);
  //cout << a << ' ' << b << ' ' << pos[cur] << ' ' << ret << endl;
  return ret;
}

main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    vector<int> v = A;
    sort(v.begin(), v.end());
    for (int i = 0; i < N; i++)
      A[i] = find(v.begin(), v.end(), A[i]) - v.begin();
    for (int i = 0; i < N; i++) {
      pos[i] = 0;
      for (int j = 0; A[j] != i; j++)
        if (A[j] > i) pos[i]++;
    }
    memset(memo, -1, sizeof(memo));
    cout << "Case #" << prob++ << ": " << doit(N-1, N-1) << endl;
  }
}
