#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>

using namespace std;

#define all(x) x.begin(), x.end()
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define debug(x) std::cerr << "DEBUG: " << #x << " = " << (x) << std::endl
#define mp make_pair
#define pb push_back
#define PATH "C:\\Users\\Valentin\\Desktop\\"

template<class T> inline int sz(const T& x) { return (int) x.size(); }
template<class T> inline void mx(T& x, const T& y) { x = std::max(x, y); }
template<class T> inline void mn(T& x, const T& y) { x = std::min(x, y); }

// SOLUTION BEGINS HERE

// #define INPUT "in.txt"

// map<string, string> winner;

int n, k;
vector<double> p;


void read_input() {
  cin >> n >> k;
  p.resize(n);
  forn (i, n) {
    cin >> p[i];
  }
}

long double calc(int mask) {
  // debug(mask);
  vector<long double> p_curr(n + 2, 0.0);
  p_curr[0] = 1.0;
  forn (i, n) {
    if ((mask >> i) & 1) {
      vector<long double> p_next(n + 2, 0.0);
      forn (j, n + 1) {
        p_next[j] += p_curr[j] * (1 - p[i]);
        p_next[j + 1] += p_curr[j] * (p[i]);        
      }      
      p_curr = p_next;
    }
  }
  return p_curr[k / 2];
}

void solve() {
  long double ans = 0.0;
  forn (i, 1 << n) {
    int bit_count = 0;
    forn (j, n) {
      bit_count += (i >> j) & 1;
    }
    if (bit_count != k) {
      continue;
    }
    mx(ans, calc(i));
  }  
  cout << fixed << setprecision(9) << (double) ans << endl;
}


// SOLUTION ENDS HERE

void run(int iMinTest, int iMaxTest) {  
  // freopen(PATH"in.txt", "r", stdin);  
  // freopen(PATH"out.txt", "w", stdout);
  int nTest;
  std::cin >> nTest;
  // init();
  forn (iTest, nTest) {
    read_input();
    if (iMinTest <= iTest && iTest < iMaxTest) {
      std::cout << "Case #" << (iTest + 1) << ": ";
      solve();      
    }
  }
}

int main(int argc, char* argv[]) {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int iMinTest = 0;
  int iMaxTest = std::numeric_limits<int>::max();
  if (argc == 3) {
    iMinTest = std::atoi(argv[1]);
    iMaxTest = std::atoi(argv[2]);
  }
  run(iMinTest, iMaxTest);
  std::cout.flush();
  return 0;
}
