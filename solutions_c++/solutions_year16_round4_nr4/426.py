/* My Template for the Google Code Jam.
 *
 * Compile: g++ -std=c++11 -lgmp -lgmpxx
 *  - I'm probably using some C++11 features.
 *  - I might use GMP (GNU Multiple Precision Arighmetic Library) so
 *    I'm including the library in the template even if they
 *    won't be used.
 *
 * This code is ugly but it works - otherwise you wouldn't be reading
 * it, right?
 */

#include <cassert>
//#define NDEBUG

#include <cstdlib>
#include <cstdint>
#include <cmath>

#include <iomanip>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <bitset>

#include <gmpxx.h>

using namespace std;
typedef size_t szt;

typedef long long ll;
typedef unsigned long long ull;

typedef mpz_class mpz;

template<typename T>
void read_to_vector(size_t N, std::vector<T> &v) {
  for(size_t i=0; i<N; i++) {
    T tmp;
    std::cin >> tmp;
    v.push_back(tmp);
  }
}
template<typename T>
void print_vector(const std::vector<T> &v) {
  for(auto it = v.begin(); it<v.end(); it++) {
    if(it!=v.begin())
      std::cout << " ";
    std::cout << (*it);
  }
}

template<typename T>
void print_vectorn(const std::vector<T> &v) {
  for(auto it = v.begin(); it<v.end(); it++) {
    if(it!=v.begin())
      std::cout << "\n";
    std::cout << (*it);
  }
}
//Copy functions from TCR here.


template<typename T> T next_combination(T x) {
    T a = x&(x-1);
    T s = x-a;
    T u = x+s;
    T r = u&(u-1);
    T b = x-r;
    T c = b/(s*2);
    return u+c;		
}


std::vector<std::bitset<25> > t;

bool testtt(std::vector<std::bitset<25> > tt) {

  //  cout << "Testing tt\n";
  //  print_vectorn(tt);
  //  cout << endl;

  int N = tt.size();

  
  
  for (int i=0; i<N; i++) {
    if (tt[i].count()==0) { return false; }
    for (int j=0; j<N; j++) {
      if (!tt[i][j]) continue;

      auto ttt = tt;
      ttt.erase(ttt.begin()+i);
      for (auto & b : ttt) {
	b[j] = false;
      }

      if (!testtt(ttt)) return false;
    }
  }
  
  //  cout << "Valid " << tt.size() << "!\n";
  return true;
}

bool testmask(ll mask) {
  //  cout << "Mask: " << mask << endl;
  auto tt = t;
  int N = t.size();
  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      if (mask & (1<<(i*N+j))) {
	tt[i][j] = true;
      } else {
	if (tt[i][j]) return false;
      }
    }
  }

  return testtt(tt);

}

ll solve() {
  ll N;
  cin >> N;
  t.clear();
  for (int i=0; i<N; i++) {
    std::bitset<25> b(0);
    string s;
    cin >> s;
    for (int j=0; j<s.size(); j++) {
      if (s[j]=='1') b[j] = true;
    }
    t.push_back(b);
  }

  ll initprice = 0;
  for (auto b : t) {
    initprice += b.count();
  }

  ll minprice = N*N;
  for (ll mask=0; mask<(1LL<<(N*N)); mask++) {
    if (testmask(mask)) {
      if (__builtin_popcount(mask) < minprice)
      minprice = __builtin_popcount(mask);
    }
  }

  return minprice - initprice;

}

//This is executed before any input is read.
void pre_compute() {
  
}

int main() {
  std::cout << std::setprecision(15);
  std::cin.tie(0);
  pre_compute();
  size_t T;
  std::cin >> T;
  for(size_t i=1; i<=T; i++) {
    //CHOOSE A
    auto res = solve();
    std::cout << "Case #" << i << ": " << res << "\n";
  }

  return 0;
}
