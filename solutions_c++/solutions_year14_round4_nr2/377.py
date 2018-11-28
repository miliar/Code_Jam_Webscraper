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
    if(it==v.begin())
      std::cout << " ";
    std::cout << (*it);
  }
}

//Copy functions from TCR here.



//Solution:

ll solve2() {
  szt N;
  std::cin >> N;
  vector<ll> a;
  read_to_vector(N, a);

  vector<int> incs(N, 0);
  vector<int> decs(N, 0);

  for(szt i=0; i<N; i++) {
    for(szt j=i+1; j<N; j++) {
      if(a[i]<a[j]) 
	incs[i]++;
      else
	decs[j]++;
    }
  }

  ll sum=0;
  for(szt i=0; i<N; i++) {
    sum += incs[i];
    sum += decs[i];
  }
  //  cerr << sum-(N*(N-1)/2) << "\n";

  ll min=N*N+1;
  
  for(szt m=0; m<=N; m++) {
    ll swaps = 0;
    for(szt i=0; i<m; i++) 
      swaps += decs[i];
    for(szt i=m; i<N; i++)
      swaps += incs[i];

    if(swaps<min)
      min = swaps;
  }

  return min;
}

ll solve() {
  szt N;
  std::cin >> N;
  vector<ll> a;
  read_to_vector(N, a);

  int ia=0;
  int ib=N-1;

  ll res = 0;
  for(szt i=0; i<N; i++) {
    //smallest
    szt smalli= ia;
    for(szt ii = ia; ii <= ib; ii++ )
      if(a[ii] < a[smalli]) 
	smalli = ii;
    
    ll resstart = smalli - ia;
    ll resend = ib - smalli;
    if(resstart < resend) {
      for(szt ii = smalli; ii > ia; ii-- ) {
	swap(a[ii], a[ii-1]);
	res++;
      }
      ia ++;
    } else {
      for(szt ii = smalli; ii < ib; ii++) {
	swap(a[ii], a[ii+1]);
	res++;
      }
      ib --;
    }
    
  }

  return res;

}

//This is executed before any input is read.
void pre_compute() {
  
}

int main() {
  std::cout << std::setprecision(15);
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
