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


int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

//Solution:
bool dfs(int H, int W, vector<vector<bool> > &b, int x, int y, int dir) {
  if(b[y][x]) return false;
  b[y][x] = true;
  
  //  cout << "DFS at " << x << " " << y << "\n";

  if(y==H-1) return true;

  for(int dd=-1; dd<=2; dd++) {
    int dirn = (dd + dir + 4) % 4;

    int xn = x + dx[dirn];
    int yn = y + dy[dirn];

    //    cout << "Trying to go to " << xn << " " << yn << "\n";

    if((xn<0) || (xn>=W) || (yn<0) || (yn>=H))
      continue;
    if(b[yn][xn]) 
      continue;

    //    b[yn][xn] = true;
    if(dfs(H, W, b, xn, yn, dirn))
      return true;
  }

  return false;
}

ll solve() {
  szt W, H, B;
  cin >> W;
  cin >> H;
  cin >> B;
  
  vector<int> x0 (B, 0), y0 (B, 0), x1 (B, 0), y1 (B, 0);
  for(szt i=0; i<B; i++) {
    cin >> x0[i];
    cin >> y0[i];
    cin >> x1[i];
    cin >> y1[i];
  }

  vector<vector<bool> > b(H,vector<bool>(W,false));

  for(szt i=0; i<B; i++) {
    for(int y=y0[i]; y<=y1[i]; y++)
      for( int x=x0[i]; x<=x1[i]; x++)
	b[y][x] = true;
  }


  for(int y=0; y<H; y++) {
    //    print_vector(b[y]);
    //    cout << "\n";
  }
  
  int res = 0;
  for(int xstart=0; xstart<W; xstart++) {
    //    std::cout << "Start " << xstart << "\n";
    if (dfs(H, W, b, xstart, 0, 0))
      res ++;
    
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
