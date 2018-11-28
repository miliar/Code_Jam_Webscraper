#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <vector>
#include <sstream>
using namespace std;


int main() {
  freopen("C-small-attempt2.in", "r", stdin);
  freopen("file.out", "w", stdout);
  set<int> primeNumbers;
  int T, j, n;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ":\n";
    cin >> n >> j;
    int count = j;
    const long long offset = pow((double)2,n-1) + 1;
    const long long maxNum = pow((double)2,n)-1;
    for(long long num = offset; num <= maxNum && count > 0; ++num) {
      if(primeNumbers.find(num) != primeNumbers.end()) // NB!!! prime number in base 2..10
        continue;
      if(!((1 & num) && (num >> (n-1))))
        continue;
      stringstream ss;
      int nOfBasesCorrect = 0;
      for(int base = 2; base <= 10; ++base) {
        long long numBaseK = 0;
        // transform to baseK
        for(int i = n-1; i > 0; --i) {
          numBaseK = numBaseK + ((num & (1 << i)) == 0 ? 0 : 1);
          numBaseK *= base;
        }
        numBaseK += (num & 1);
        //cout << "base " << base << " " << numBaseK << endl;
        // find divisors:
        const long long sqroot = sqrt(numBaseK);
        long long i;
        for(i = 2; i <= sqroot; ++i) {
          if(numBaseK % i == 0) {
            ss << i << " ";
            ++nOfBasesCorrect;
            break;
          }
          
        }
        if (i == sqroot + 1)
          break;
      }
      if (nOfBasesCorrect == 9) {
        --count;
        for(int i = n - 1; i >= 0; --i) {
          if((num >> i) & 1) cout << 1;
          else cout << 0;
        }
        cout << " ";
        string divisors = ss.str();
        divisors.pop_back(); // remove trialing ' '
        cout << divisors << endl;
      }
    }
  }
  return 0;
}
