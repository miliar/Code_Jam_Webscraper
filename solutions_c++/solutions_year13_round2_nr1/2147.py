#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

long long f(long long& x, long long y)
{
  long long res = 0;
  if (x == 1) return 1000000000;
  while (x <= y) {
    x += (x-1);
    res++;
  }
  //cerr << x << endl;
  return res;
}

int main(void)
{
  int T;
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  cin >> T;
  for (int t = 0; t < T; t++) {
    long long a, n, res = 0;
    int A[1111];
    cin >> a >> n;
    for (int i = 0; i < n; i++) {
      cin >> A[i];
    }
    sort(A,A+n);
    for (int i = 0; i < n; i++) {
      long long x = A[i];
      //cerr << x << endl;
      if (a <= x) {
        long long xx = a;
        long long c = f(xx,x);
        //cerr << t << " " << c << endl;
        if (c >= (n-i)) {
          res += (n-i);
          break;
        } else {
          res += c;
          a = xx+x;
        }
      } else {
        a += x;
      }
    }
    cout << "Case #" << t+1 << ": " << res << endl;
  }
  return 0;
}
