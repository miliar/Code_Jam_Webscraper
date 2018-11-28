#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

long long findMax(int N, long long P)
{
  long long j = 0;
  long long k = (1LL << N) - 1;
  long long a = 1;
  for (int i = N - 1; i >= 0; i--) {
    if ((P - 1) & (1LL << i)) {
      a *= 2;
      j += a;
    } else {
      break;
    }
  }
  return (j >= k) ? k : j;
}

long long findMin(int N, long long P)
{
  long long j = (1LL << N) - 1;
  long long a = 1;
  for (int i = N; i >= 0; i--) {
    if (P >= (1LL << i)) { 
      break;
   } else {
      j -= a;
      a *= 2;
    }
  }
  return j;
}

int main()
{
  int T;

  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    int N;
    long long P;

    cin >> N >> P;

    cout << "Case #" << cas << ": " << findMax(N, P) << " " << findMin(N, P) << endl;
  }

  return 0;
}

