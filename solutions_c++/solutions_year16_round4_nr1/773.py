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

#define INPUT "in.txt"

int n, r, p, s;

string DP(int r, int p, int s) {

  if (r + p + s == 1) {
    if (r == 1) return "R";
    if (p == 1) return "P";
    return "S";    
  }

  string ret = "";
  for (int pr = min(p, r); pr >= 0; --pr) {
    int rs = r - pr;
    int ps = p - pr;

    if (rs + ps != s) {
      continue;
    }

    string winners = DP(rs, pr, ps);

    if (winners.empty()) {
      continue;
    }
    
    string result;
    for (char c : winners) {
      if (c == 'P') result += "PR";
      if (c == 'S') result += "PS";
      if (c == 'R') result += "RS";
    }
    ret = result;
  }

  return ret;
}


// map<string, string> winner;

void solve() {

  int n, r, p, s;
  cin >> n >> r >> p >> s;

  string ans = DP(r, p, s);
  if (ans.empty()) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  
  for (int size = 2; size <= (1 << n); size *= 2) {
    string next_ans = "";
    for (int i = 0; i < (1 << n); i += size) {
      string a = ans.substr(i, size / 2);
      string b = ans.substr(i + size / 2, size / 2);
      next_ans += min(a, b);
      next_ans += max(a, b);
    }
    ans = next_ans;
  }
  cout << ans << endl;
  
  
}

void init() {
}

// SOLUTION ENDS HERE

void run() {  
  freopen(PATH"A-large.in", "r", stdin);  
  freopen(PATH"out.txt", "w", stdout);
  int nTest;
  std::cin >> nTest;
  init();
  forn (iTest, nTest) {
    std::cout << "Case #" << (iTest + 1) << ": ";
    solve();
  }
}

int main(int argc, char* argv[]) {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  run();
  // int iMinTest = 0;
  // int iMaxTest = std::numeric_limits<int>::max();
  // if (argc == 3) {
    // iMinTest = std::atoi(argv[1]);
    // iMaxTest = std::atoi(argv[2]);
  // }
  // run(iMinTest, iMaxTest);
  std::cout.flush();
  return 0;
}
