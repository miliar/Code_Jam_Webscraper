#include <iostream>
#include <vector>
using namespace std;
vector<int> primes;
int numCnt = 0;
void nextNum(vector<int> &num) {
  int n = num.size();
  int idx = n - 2;
  num[idx]++;
  while (num[idx] >= 2) {
    num[idx - 1] += num[idx] / 2;
    num[idx] %= 2;
    idx--;
  }
}
bool prime(vector<int> &num, int r, vector<int> &fac) {
  for (int i = 0; i < numCnt; i++) {
    int now = primes[i];
    long long n = num.size(), mul = 1;
    int sum = 0;
    long long diff = now;
    for (int j = n - 1; j >= 0; j--) {
      int val = num[j] * mul;
      sum = (sum + val) % now;
      mul = (mul * r) % now;
    }

    mul = 1;
    for (int j = n - 1; j >= 0; j--) {
      //diff -= num[j] * mul;
      mul = mul * r;
    }
    if (sum == 0 && diff != 0) {
      //cout << "diff = " << diff << endl;
      fac[r] = now;
      return false;
    }
  }
  return true;
}
int main() {
  int N = 100;
  vector<bool> vis(N + 1);
  for (int i = 2; i < N; i++) {
    if (!vis[i]) {
      primes.push_back(i);
      numCnt++;
      for (int j = 2; j <= N / i; j++) {
        vis[i * j] = true;
      }
    }
  }
  int tk, tk1 = 0;
  cin >> tk;
  while (tk--) {
    tk1++;
    cout << "Case #" << tk1 << ":" << endl;
    int n, k;
    cin >> n >> k;
    vector<int> num(n);
    num[0] = num[n - 1] = 1;
    while (k) {
      int npCnt = 0;
      vector<int> fac(11);
      for (int r = 2; r <= 10; r++) {
        //cout << "r = " << r << endl;
        if (!prime(num, r, fac)) {
          npCnt++;
        }
      }
      if (npCnt == 9) {
        for (int i = 0; i < n; i++) {
          cout << num[i];
        }
        for (int i = 2; i <= 10; i++) {
          cout << " " << fac[i];
        }
        cout << endl;
        k--;
      }
      nextNum(num);
    }
  }
}
