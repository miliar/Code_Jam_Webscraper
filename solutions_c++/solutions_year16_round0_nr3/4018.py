#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

typedef long long ll;

int is_prime(ll n) {
  if((n&1) == 0) return 2;
  ll upper = sqrt(n);
  int div = -1;
  for(int i = 3; i <= upper; i += 2) {
    if(n % i == 0) {
      div = i;
      break;
    }
  }
  return div;
}

string bin(int y) {
  string s;
  while(y > 0){
    s = ((y&1) ? '1' : '0') + s;
    y >>= 1;
  }
  return s;
}

int main(void){
  int t;
  cin >> t;
  cout << "Case #1:" << endl;

  int n, j;
  cin >> n >> j;

  int divs[11];

  int max = 1 << n;
  for(int x = 0; x < max; ++x) {
    if((x&1) == 0 || (x&(1<<(n-1))) == 0) continue;

    bool prime = false;
    for(int b = 2; b <= 10; ++b) {
      ll num = 0;
      for(int i = n-1; i >= 0; --i) {
        num *= b;
        num += (x >> i) & 1;
      }
      //cout << "  " << b << " : " << num << endl;
      if((divs[b] = is_prime(num)) == -1) {
        //cout << "    prime: " << divs[b] << endl;
        prime = true;
        break;
      }
    }
    if(prime) continue;

    cout << bin(x);
    for(int b = 2; b <= 10; ++b)
      cout << ' ' << divs[b];
    cout << endl;

    if(--j == 0) break;
  }

  return 0;
}

