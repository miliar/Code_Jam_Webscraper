#include <bitset>
#include <iostream>
#include <string>

using namespace std;

bool isPrime(long long n) {
  for(long long i = 2; i * i <= n; ++i)
    if(n % i == 0) return false;
  return true;
}

long long divisor(long long n) {
  for(long long i = 2; i * i <= n; ++i)
    if(n % i == 0) return i;
  return 0;
}

int main() {
  const int n = 16;
  const int j = 50;
  cout << "Case #1:\n";
  int cnt = 0;
  for(int i = (1 << (n - 1)) + 1; cnt < j && i < (1 << n); i += 2){
    bool good = true;
    string num = bitset < n > (i).to_string();
    for(int j = 2; good && j <= 10; ++j){
      good &= !isPrime(stol(num, 0, j));
    }
    if(!good) continue;
    cout << num;
    for(int j = 2; good && j <= 10; ++j){
      cout << ' ' << divisor(stol(num, 0, j));
    }
    cout << endl;
    ++cnt;
  }
}
