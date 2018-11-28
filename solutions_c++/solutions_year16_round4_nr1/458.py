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

void order(string & s) {
  for (ll len=1; len < s.size(); len *= 2) {
    for (ll i=0; i<s.size(); i+= 2*len) {
      //cout << s.size() << " " << i << " " << len << "\n";
      string s1 = s.substr(i, len);
      string s2 = s.substr(i+len, len);
      if (s2 < s1) {
	for (ll j=0; j<len; j++) {
	  swap(s[i+j], s[i+len+j]);
	}
      }
    }
  }
}

string sol(ll R, ll P, ll S) {

  //cout << "Sol: " << R << " " << P << " " << S << endl;

  if (R+P+S==1) {
    if (R==1) {
      return "R";
    }
    if (S==1) {
      return "S";
    }
    if (P==1) {
      return "P";
    }
  }

  if (R+P+S==2) {
    if (R==1 && P==1) {
      return "PR";
    }
    if (R==1 && S==1) {
      return "RS";
    }
    if (P==1 && S==1) {
      return "PS";
    }
    return "IMPOSSIBLE";
  }

  ll r=0, p=0, s=0;
  
  while (R+P+S > 0) {
    if (R>=P && R>=S) {
      R -= 2;
      P -= 1;
      S -= 1;
      p += 1;
    }
    else if (P>=S && P>=R) {
      P -= 2;
      S -= 1;
      R -= 1;
      s += 1;
    }
    else if (S>=R && S>=P) {
      S -= 2;
      R -= 1;
      P -= 1;
      r += 1;
    }
  }

  if (R<0 || P<0 || S<0) { 
    return "IMPOSSIBLE"; 
  }

  string ss = sol(r, p, s);
  if (ss=="IMPOSSIBLE") { return ss; }

  string res;
  res.reserve(R+P+S);
  for (char c : ss) {
    if (c=='S') { res += "PRPS"; }
    if (c=='R') { res += "PSRS"; }
    if (c=='P') { res += "PRRS"; }
  }

  return res;

}

string solve() {
  
  ll N, R, P, S;
  cin >> N >> R >> P >> S;

  string res = sol(R, P, S);
  if (res != "IMPOSSIBLE") 
    order(res);
  return res;

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
