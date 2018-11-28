#include<bits/stdc++.h>
using namespace std;
typedef long long int64;

const int MAX = 10000000;

struct CoinJam
{
  int prime[MAX + 1];

  inline int64 Convert(int64 value, const int d) // 2 base -> d base 
  {
    if(value == 0) {
      return(0);
    } else {
      return(Convert(value >> 1LL, d) * d + value % 2);
    }
  }

  void MakePrime()
  {
    memset(prime, 0, sizeof(prime));
    for(int i = 2; i * i <= MAX; i++) {
      if(prime[i] == 0) {
        for(int j = i + i; j <= MAX; j += i) prime[j] = i;
      }
    }
  }
  int64 isPrime(int64 val)
  {
    if(val <= MAX) return(prime[val]);
    for(int64 i = 2; i * i <= val; i++) {
      if(val % i == 0) return(i);
    }
    return(0);
  }

  CoinJam()
  {
    MakePrime();

    int N, J;
    cin >> N >> J;

    for(int64 i = (1LL << (N - 1)) + 1; J > 0 && i < (1LL << N); i += 2) {
      bool failed = false;
      for(int64 j = 2; j <= 10; j++) {
        if(isPrime(Convert(i, j)) == 0) {
          failed = true;
          break;
        }
      }
      if(!failed) {
        for(int64 j = N - 1; j >= 0; j--) {
          cout << (int)((i >> j) & 1);
        }
        for(int64 j = 2; j <= 10; j++) {
          cout << " " << isPrime(Convert(i, j));
        }
        cout << endl;
        --J;
      }
    }
  }
};


int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ":" << endl;
    new CoinJam();
  }
  return(0);
}
