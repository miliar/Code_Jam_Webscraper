/**
 * Problem: C
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <math.h>
#include <set>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <assert.h>
#include <map>

#include <sstream>

#include <stdexcept>

using namespace std;

typedef vector<string> vs;
typedef long long ll;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<ll> vll;

ll baseConversionFrom(ll nb, ll base) {
  ll r = 0;
  ll p = 1;
  while (nb != 0) {
    r += (nb % 10) * p;
    nb = nb / 10;
    p *= base;
  }
  return r;
}

ll baseConversionTo(ll nb, ll base) {
  ll r = 0;
  ll shift = 1;
  while (nb != 0) {
    r += (nb % base) * shift;
    nb = nb / base;
    shift *= 10;
  }
  return r;
}

vector<ll> primes;

int main(int argc, const char **argv) {

  int NN = 1 << 30;
  // int NN = 4294967296;
  // cout << "NN:" << NN << endl;
  bool *scieve;
  scieve = new bool[NN+2];
  for(int i = 4; i <= NN; i+=2) {
    scieve[i] = true;
  }
  for(int i = 3; i < pow(NN, 0.5); i+=2) {
    if(!scieve[i]) {
      for(int j = i*i; j<NN; j+=2*i){
        scieve[j] = true;
      }
    }
  }

  for (int i = 2; i < NN; i++) {
    if (!scieve[i]) {
      primes.push_back(i);
    }
  }

  int cases;
  string tmp;
  cin >> cases;
  ll N, J;
  int total, base, j;
  ll k;
  ll digits;
  vector<ll> dividers;
  bool divFound;
  bool isJam;
  for (int caseI = 1; caseI <= cases; caseI++) {
    total = 0;
    j = 0;
    cin >> N >> J;
    cout << "Case #" << caseI << ":" << endl;
    for (ll i = (1 << (N-1)) + 1; i< (1<<N); i++) {
      isJam = true;
      dividers.clear();
      digits = baseConversionTo(i, 2);
      if (digits%10 == 0) {
        continue;
      }

      for (base = 2; base <= 10; base++) {
        divFound = false;
        // If no divider found, continue with another i
        k = baseConversionFrom(digits, base);
        // cout << "k:" << k << endl;
        // cout << "base:" << base << endl;
        std::vector<ll>::iterator it;
        for (it = primes.begin(); it != primes.end(); ++it) {
          // cout << "*it:" << *it << endl;
          if (k%*it == 0) {
            if (k == *it) {
              isJam = false;
            }
            dividers.push_back(*it);
            divFound = true;
            break;
          }
        }
        if (!divFound) { break; }
      }
      if (!isJam) {
        continue;
      }
      if (divFound) {
        cout << digits;
        std::vector<ll>::iterator it;
        for (it = dividers.begin(); it != dividers.end(); ++it) {
          cout << " " << *it;
        }
        cout << endl;
        j++;
      }
      if (j == J) {
        break;
      }
    }
  }

  return 0;
}
