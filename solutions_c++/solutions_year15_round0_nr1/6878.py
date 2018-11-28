#include <algorithm>
#include <array>
#include <complex>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

inline bool valid(const int x, const int r) { return 0 <= x && x < r; }

void initIOStream() {
  ios::sync_with_stdio(false); // stdinなどと同期しない
  cin.tie(0); // cinの前にflushしない
  cout.setf(ios::fixed);
  cout.precision(10); // 四捨五入して指定桁数表示
}

int main() {
  initIOStream();

  int T;
  cin >> T;

  for(int t = 0; t < T; ++t) {
    int N;
    cin >> N;

    int sum = 0, ans = 0;
    for(int i = 0; i <= N; ++i) {
      char c;
      cin >> c;
      int x = c - '0';
      if(sum < i){
        ans += i - sum;
        sum = i;
      }
      sum += x;
    }
    cout << "Case #" << t + 1 << ": " << ans << endl;
  }
}
