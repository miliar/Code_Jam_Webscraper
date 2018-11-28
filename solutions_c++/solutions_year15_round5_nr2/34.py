#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  long long T, N, K, prob=1;
  for (cin >> T; T--;) {
    cin >> N >> K;
    vector<long long> v(N), vs(N-K+1);
    for (long long i = 0; i < N-K+1; i++) cin >> vs[i];
    v[K-1] = vs[0];
    for (long long j = K; j < N; j++) v[j] = vs[j-K+1]-vs[j-K] + v[j-K];
//for (long long i = 0; i < N; i++) cout << v[i] << ' ';
//cout << endl;

    long long ret = 0;
    for (long long i = 0; i < K; i++) {
      long long curmn = 0, curmx = 0;
      for (long long j = i+K; j < N; j += K) {
        curmx = max(curmx, v[j]-v[i]);
        curmn = min(curmn, v[j]-v[i]);
      }
      ret = max(ret, curmx - curmn);
    }

    long long md = 0;
    for (long long i = 0; i < K; i++) md += v[i];
    md = (md%K+K)%K;

    long long minmd = 0, maxmd = 0;
    for (long long i = 0; i < K; i++) {
      long long curmn = 0, curmx = 0;
      for (long long j = i+K; j < N; j += K) {
        curmx = max(curmx, v[j]-v[i]);
        curmn = min(curmn, v[j]-v[i]);
      }
      minmd += -curmn;
      maxmd += -curmn + (ret - (curmx-curmn));
    }

    while (minmd >= K) {minmd -= K; maxmd -= K;}
//cout << ret << ' ' << md << ": " << minmd << " to " << maxmd << endl;
    if (maxmd < md || minmd > md && maxmd < md+K) ret++;
    cout << "Case #" << prob++ << ": " << ret << endl;
  }
}
