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

void solve() {

  int R, C;
  cin >> R >> C;
  vector<string> T;
  read_to_vector(R, T);

  int count = 0;

  for(int i=0; i<R; i++) {
    for (int j=0; j<C; j++) {
      
      if(T[i][j] == '.') continue;
      int di [4] = {-1, 0, 0, 1};
      int dj [4] = {0, 1, -1, 0};

      bool dirs [4] = {0,0,0,0};

      for(int dir = 0; dir<4; dir++) {
	int i0 = i+di[dir];
	int j0 = j+dj[dir];
	while(i0>=0 && i0<R && j0>=0 && j0<C) {
	  if(T[i0][j0] != '.') 
	    dirs[dir] = true;
	  i0 += di[dir];
	  j0 += dj[dir];
	}
      }

      char dirc [4] = {'^', '>', '<', 'v'};

      bool possible = false;
      bool change = true;
      for(int dir=0; dir<4; dir++) {
	if(dirs[dir]) {
	  possible = true;
	  if(dirc[dir] == T[i][j]) {
	    change = false;
	  }
	}
      }

      if(!possible) {
	//	cerr << i << " " << j << "\n";
	cout << "IMPOSSIBLE";
	return;
      }

      if(change) {
	count ++;
      }
    }
  }

  cout << count;
  
}

int main() {
  std::cout << std::setprecision(15);
  size_t T;
  std::cin >> T;
  for(size_t i=1; i<=T; i++) {
    std::cout << "Case #" << i << ": ";
    solve();
    std::cout << "\n"; //Either of these should be removed.
  }

  return 0;
}
