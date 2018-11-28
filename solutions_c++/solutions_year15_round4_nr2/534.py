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
    if(it!=v.begin())
      std::cout << " ";
    std::cout << (*it);
  }
}

//Copy functions from TCR here.



//Solution:


bool possible(double t, vector<pair<double,double> > CR, double V) {
  int N = CR.size();

  cerr << "\nTesting: " << t << " " << V << " " << N << "\n";
  for(int i=0; i<N; i++) {
    CR[i].second *= t;
    cerr << "Stream: " << CR[i].second << " temp " << CR[i].first << "\n";
  }

  for(int i=N-1; i>=0; i--) {
    if(CR[i].first == 0) {
      V -= CR[i].second;
      CR.erase(CR.begin()+i);
      N--;
    }
  }

  int i = 0;
  int j = N-1;
  while(i<j && V>0 ) {
    
    if(CR[i].first > 0 || CR[j].first < 0) {
      return false;
    }
    if((CR[i].first * CR[i].second + CR[j].first * CR[j].second) > 0) {
      //Too hot
      double uj = - CR[i].second * CR[i].first / CR[j].first;
      assert(uj>0);
      cerr << "Adding cold: " << CR[i].second << " temp: " << CR[i].first << "\n";
      cerr << "Adding hot: " << uj << " temp: " << CR[j].first << "\n";
      V -= CR[i].second;
      CR[j].second -= uj;
      V -= uj;
      i ++;
    } else {
      double ui = - CR[j].second * CR[j].first / CR[i].first;
      assert(ui>0);
      cerr << "Adding cold: " << ui << " temp: " << CR[i].first << "\n";
      cerr << "Adding hot: " << CR[j].second << " temp: " << CR[j].first << "\n";
      V -= CR[j].second;
      CR[i].second -= ui;
      V -= ui;
      j --;
    }

    cerr << "Volume remaining: " << V << "\n";
    for(int ii=i; ii<=j; ii++) {
      cerr << "Stream: " << CR[ii].second << " temp " << CR[ii].first << "\n";
    }
  }

  return (V<=0);
  
}

double solve() {
  int N;
  double V, X;
  cin >> N;

  cin >> V >> X;

  if(N == 1) {
    double r, c;
    cin >> r >> c;
    if(c != X) { 
      return -1;
    } else {
      return V/r;
    }
  }

  vector<pair<double,double> > CR;
  for(int i=0; i<N; i++) {
    double r, c;
    cin >> r >> c;
    CR.push_back(pair<double,double>(c-X,r));
  }

  sort(CR.begin(), CR.end());


  if(CR[0].first > 0 || CR[N-1].first < 0) {
    return -1;
  }


  double lower = 0;
  double upper =  1e12;

  while((upper-lower > 1e-9)) {// && (upper-lower)/(upper+lower) > 1e-9) {
    double test = (upper+lower)/2;
    if (possible(test, CR, V)) {
      upper = test;
    } else {
      lower = test;
    }
  }

  return (upper+lower)/2;
  
}

//This is executed before any input is read.
void pre_compute() {
  
}

int main() {
  std::cout << std::setprecision(15);
  cout << fixed;
  pre_compute();
  size_t T;
  std::cin >> T;
  for(size_t i=1; i<=T; i++) {
    //CHOOSE A
    auto res = solve();
    if(res>=0) {
      std::cout << "Case #" << i << ": " << res << "\n";
    } else {
      std::cout << "Case #" << i << ": IMPOSSIBLE\n";
    }
  }

  return 0;
}
