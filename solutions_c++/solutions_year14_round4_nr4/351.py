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
int commonprefix(const string s0, const string s1) {
  int i=0;
  for(i=0; i<min(s0.length(), s1.length()); i++)
    if(s0[i] != s1[i]) break;
  return i;
}

ll countnodes(const vector<string> & S) {
  ll res = 1;
  res += S[0].length();

  for(int i=1; i<S.size(); i++) {
    res += S[i].length() - commonprefix(S[i], S[i-1]);
  }

  return res;
}

ll countnodes(const vector<vector<string> > & Ts) {
  ll res = 0;
  for(auto & S : Ts) {
    res += countnodes(S);
  }
  return res;
}

void solve() {

  int M, N;
  cin >> M;
  cin >> N;

  vector<string> S;
  read_to_vector(M, S);

  sort(S.begin(), S.end());

  int maxa = 1;
  for(int i=0; i<M; i++)
    maxa *= N;

  ll count  = 0;
  ll max = 0;

  for(int a=0; a<maxa; a++) {
    
    vector<vector<string> > Ts (N, vector<string>());

    int aa = a;
    for(int i=0; i<M; i++) {
      int thisi = aa % N;
      aa /= N;
      Ts[thisi].push_back(S[i]);
    }

    //If some is empty, not valid;
    bool valid = true;
    for(int i=0; i < N; i++)
      if(Ts[i].empty()) valid = false;
    if(!valid)
      continue;

    ll thismax = countnodes(Ts);
    if(thismax>max) {
      max = thismax;
      count = 0;
    } 
    if (thismax==max) {
      count ++;
    }

  }

  std::cout << max << " " << (count % 1000000007);
  
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
    //CHOICE B
    std::cout << "Case #" << i << ": ";
    solve();
    std::cout << "\n"; //Either of these should be removed.
  }

  return 0;
}
