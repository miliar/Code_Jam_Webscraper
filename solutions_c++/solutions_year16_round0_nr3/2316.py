#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int fac(long long int n) {
  long long int i = 3;
  while(i * i <= n) {
    if(n % i == 0) return static_cast<int>(i);
    i += 2;
  }
  return 0; 
}

int attempt(int n) {
  string s(16, '0');
  for(int i = 0, ii = n; i < 16; ++i) {
    s[15-i] = "01"[ii & 1];
	ii /= 2;
  }
  int factors[10], i = 0;
  int f = fac(n); if(f) factors[i++] = f; else return 0;
  for(int k = 3; k <= 10; ++k) {
    f = fac(stoll(s, 0, k)); if(f) factors[i++] = f; else return 0;
  }
  cout << s;
  for(int j = 0; j < i; ++j) cout << ' ' << factors[j];
  cout << '\n';
  return 1;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << "Case #1:\n";
  int start = 0x8001;
  int cnt = 50;
  while(cnt) {
    cerr << "Testing " << start << ", cnt = " << cnt << '\n';
    cnt -= attempt(start);
    start += 2;
  }
}
