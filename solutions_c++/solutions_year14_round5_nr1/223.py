/* Opgave: A */
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <tuple>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;


long long ss(long long a, long long b, long long c) {
  if(a > b && a > c)
    return b + c;
  return b > c ? (a + c) : (a + b);
}
void doit(int casenum) {
  long long N, p, q, r, s;
  cin >> N >> p >> q >> r >> s;
  std::vector<long long> v(N);
  for(int i = 0; i < N; ++i) {
    v[i] = (i * p + q) % r + s;
  }
  std::vector<long long> sum(N+1);
  for(int i = 0; i < N; ++i)
    sum[i+1] = sum[i] + v[i];
  double P = 0;
  for(int a = 0; a < N; ++a) {
   /* if(sum[a] * 2 > sum[N]) {
      P = max(P, (sum[N] - sum[a])/(double)sum[N]);
      continue;
    }*/
    long long t = sum[N] - sum[a];
    int b = a - 1;
    int c = N;
    while(c - b > 1) {
      int mid = (b + c) / 2;
      if(b >= N || c > N)
        std::abort();
//       std::cout << a << " " << b << " " << c << " " << (sum[mid+1] - sum[a]) << " " << t << "\n";
      if( (sum[mid+1] - sum[a]) > (mid < N ? sum[N] - sum[mid+1] : 0) && sum[mid + 1] - sum[a] > sum[a])
        c = mid;
      else
        b = mid;
    }

    if(b >= N || c > N)
      std::abort();
      //std::cout << a << " " << b << "  "<< c <<  " " << N << "\n";
    long long left0 = sum[a];
    long long mid0 = sum[b+1] - sum[a];
    long long right0 = sum[N] - sum[b+1];
    long long left1 = sum[a];
    long long mid1 = c < N ? sum[c+1] - sum[a] : sum[c] - sum[a];
    long long right1 = c < N ? sum[N] - sum[c+1] :  0;
    if(left0 + mid0 + right0 != sum[N])
      std::abort();
    if(left1 + mid1 + right1 != sum[N])
      std::abort();
    long long ll = std::max(b >= a ? ss(left0, mid0, right0) : 0, ss(left1, mid1, right1));
     // std::cerr << " " << ll << "\n";
     // std::cerr << "B: " << left0 << " " << mid0 << " " << right0 << "\n";
     // std::cerr << "C: " << left1 << " " << mid1 << " " << right1 << " : "<< sum[c+1] << " " << " " << sum[a] <<  "\n";
    if(ll > sum[N])
      std::abort();
    P = max(P, ll/(double)sum[N]);

  }
  cout.setf(ios::fixed);
  cout.precision(10);
  std::cout << "Case #" << casenum << ": " << P << "\n";
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
    doit(i);
  return 0;
}
/* Opgave: A */
