#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool complete;

long long pow(long long base, int n) {
  long long ans = 1;
  while (n) {
    if (n & 1) {
      ans *= base;
    }

    base *= base;
    n /= 2;
  }

  return ans;
}

long long Check(long long j, int k) {
  long long num = 0;
  long long base = 1;
  while (j > 0) {
    num += (j % 10) * base;
    base *= k;
    j /= 10;
  }

  for (int i = 3; i <= sqrt(num); i += 2) {
    if (num % i == 0) return i;
  }

  return -1;
}

void FindNum(long long int value, int N, int *J) {
  if (complete) return;
  if (N == 1) {
    value = value * 10 + 1;
    vector<long long> ans;
    bool find = true;
    for (int k = 10; k >= 2; --k) {
      int ret = Check(value, k);
      if (ret == -1) {
        find = false;
        break;
      }
      ans.push_back(ret);
    }

    if (find) {
//      cout << *J << " " << value;
      cout << value;
      for (int i = 8; i >= 0; --i) {
        cout << " " << ans[i];
      }
      cout << endl;
      if (--(*J) == 0) {
        complete = true;
      }
    }

    return;
  }

  for (int j = 0; j <= 1; ++j) {
    if (complete) break;
    FindNum(value * 10 + j, N - 1, J);
  }
}

int main() {
  int t;
  cin >> t;
  for (int ci = 1; ci <= t; ++ci) {
    int N, J;
    cin >> N >> J;
    cout << "Case #" << ci << ":" << endl;
    complete = false;
    FindNum(1, N - 1, &J);
  }

  return 0;
}
