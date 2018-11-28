#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
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

int n;
vector<string> mask_str;
vector<string> curr_str;

int mask[4];

void read_input() {
  cin >> n;
  mask_str.resize(n);
  forn (i, n) {
    cin >> mask_str[i];
  }
}

bool ok(int man_used, int job_used) {
  if (man_used == (1 << n) - 1) {
    return true;
  }
  int good = 0;
  int bad = 0;
  forn (i, n) {
    if (((man_used >> i) & 1) == 0) {
      forn (j, n) {
        if (((job_used >> j) & 1) == 0) {
          if (curr_str[i][j] == '1') {
            
            if (ok(man_used | (1 << i), job_used | (1 << j))) {
              good++;
            } else {
              return false;
            }          
          }
        }
      }      
    }
  }
  return bad == 0 && good > 0;
}

int gen_works(int iMan, int iSkill, int cost) {
  if (iSkill == n) {
    iMan++;
    iSkill = 0;
  }

  if (iMan == n) {    
    return ok(0, 0) ? cost : numeric_limits<int>::max();
  }
  
  curr_str[iMan][iSkill] = mask_str[iMan][iSkill];
  int a = gen_works(iMan, iSkill + 1, cost);
  curr_str[iMan][iSkill] = '1';
  int b = gen_works(iMan, iSkill + 1, cost + 1);  
  
  return min(a, b);
}

void solve() {
  curr_str = mask_str;
  cout << gen_works(0, 0, 0) << endl;  
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
