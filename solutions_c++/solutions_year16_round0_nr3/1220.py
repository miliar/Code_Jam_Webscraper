
#include <gmpxx.h>
#include <tuple>
#include <assert.h>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

template <class T>
tuple<T,T,T> extendedEuclid(const T& a, const T& b) {
    if (a == 0)
        return  make_tuple(b,0,1);
    tuple<T,T,T> next = extendedEuclid((const T&)(b % a), a);
    return make_tuple(get<0>(next), get<2>(next) - (b/a)*get<1>(next), get<1>(next));
}

template <class T>
T gcd(const T& a, const T& b) {
    if (b==0) return a;
    T amb = a % b;
    return gcd(b, amb);
}

template <class T>
T modInv(const T& a, const T& n) {
    tuple<T,T,T> gcd = extendedEuclid(a,n);
    assert( get<0>(gcd) == 1 );
    return (get<1>(gcd) + n) % n;
}

template <class T>
T modExp(const T& a, const T& b, const T& n) {
    if (b==0)
        return 1;
    T bh = b >> 1;
    T tmp = modExp(a, bh, n);
    tmp = (tmp * tmp) % n;
    if ( (b % 2) == 1 ) tmp = (tmp * a) % n;
    return tmp;
}

template <class T>
bool isMillerRabinComposite(const T& n, const T& witness, const T& q, int k) {
    if (gcd(witness,n) != 1) return false;
    T a = modExp(witness,q,n);
    if (a==1) return false;
    for (int i=0; i<k; i++) {
        if (a == (n-1)) return false;
        a = (a*a) % n;
    }
    return true;
}

template <class T, class RandGen>
bool isProbablyPrime(const T& n, RandGen prng, int iter=10) {
    if (n==2) return true;
    if ( (n&1)==0 ) return false;

    T q = n - 1;
    int k = 0;
    while ((q & 1) == 0) {
        q >>= 1;
        ++k;
    }

    for (int it=0; it<iter; it++) {
        T a = prng(2,n);
        if (isMillerRabinComposite(n,a,q,k))
            return false;
    }
    return true;
}

template<class T>
bool isProbablyPrime(const T& n, int iter=10) {
    FILE *f = fopen("/dev/urandom","r");
    auto simplePrng = [f](const T& a, const T& b) {
        T diff = b - a;
        unsigned long x;
        fread(&x, sizeof(x), 1, f);
        T bx = x;
        return (T)( a + (bx % diff) );
    };
    bool ans = isProbablyPrime(n, simplePrng, iter);
    fclose(f);
    return ans;
}

template <class T>
char _pollardFactor(const T& n, T& factor, const T& bound, const T& base) {
    T a = base;
    for (int j=2; j<bound; j++) {
        a = modExp(a, (const T&)j, n);
        if ( (j & 0xF) == 0) {
            //Enter every 16 steps
            T d = gcd((const T&)(a-1), n);
            if (d == n || a == 0) {
                return 1; //choose different a
            } else if (d != 1) {
                factor = d;
                return 0; //success
            }
        }
    }
    return 2; //Failure: We reached the bound without luck
}

unsigned long myRand() {
    FILE *f = fopen("/dev/urandom","r");
    unsigned long ans;
    fread(&ans, sizeof(ans), 1, f);
    fclose(f);
    return ans;
}

template <class T>
bool pollardFactor(const T& n, T& factor, const T& bound=1<<20) {
    if (isProbablyPrime(n)) return false;
    char tmp = _pollardFactor(n, factor, bound, (const T&)2);
    if (tmp == 0) {
        return true;
    } else if (tmp == 1) {
      for (int i=0; i<10; i++) {
        T witness = myRand() % n;
        tmp = _pollardFactor(n, factor, bound, witness ); 
        if( tmp == 0 ) {
          return true;
        } else if (tmp == 2) {
          return false;
        }
      }
    }
    return false;
}

typedef long long int LL;

bool try_coin_jam(LL x, vector<string>& witnesses) {
  witnesses.clear();
  for (int b=2; b<=10; b++) {
    mpz_class num = 0;
    for (int i=32; i>=0; i--) {
      num *= b;
      if (x & (1LL << i)) num+=1;
    }
    mpz_class fac;
    if (!pollardFactor(num, fac)) return false;
    witnesses.push_back(fac.get_str());
  }
  return true;
}

int main() {
  int N, J;
  cin >> N >> J;
  LL x = (1LL << (N-1)) + 1;
  vector<string> witnesses;
  ofstream out("coin_jam.out");
  for (int found=0; found<J && x<(1LL << (N+1)); x+=2) {
    if (try_coin_jam(x, witnesses)) {
      found++;
      cout << found << endl;
      string coin;
      for (int i=(N-1); i>=0; i--) {
        if (x & (1LL<<i)) coin.push_back('1');
        else coin.push_back('0');
      }
      out << coin;
      for (const auto& str : witnesses) {
        out << " " << str;
      }
      out << endl;
    }
  }
  out.flush();
}
