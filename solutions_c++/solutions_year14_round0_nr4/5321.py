#include <algorithm>
#include <cassert>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>


#define INF 1000000000
#define MOD 1000000007
#define ALL(x) std::begin(x), std::end(x)


int play_war(const std::vector<double>& a, std::vector<double> b)
{
  int n = 0;

  for (const auto& i : a) {
    auto it = std::upper_bound(ALL(b), i);

    if (it != std::end(b)) {
      b.erase(it);
    }
    else {
      n ++;
      
      b.erase(std::begin(b));
    }
  }
  
  return n;
}

int play_deceiful_war(std::vector<double> a, std::vector<double> b)
{
  int n = 0;
  
  for (int i = 0, size = a.size(); i < size; i ++) {
    bool superior = true;
    
    for (int j = 0, size2 = a.size(); j < size2; j ++)
      if (a[j] < b[j]) {
        superior = false;
        
        break;
      }
    
    if (superior) {
      return a.size();
    }
    else {
      a.erase(std::begin(a));
      b.pop_back();
    }
  }
  
  return 0;
}

int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T, N;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::cin >> N;

    std::vector<double> a(N), b(N);

    for (int i = 0; i < N; i ++)
      std::cin >> a[i];

    for (int i = 0; i < N; i ++)
      std::cin >> b[i];

    std::sort(ALL(a));
    std::sort(ALL(b));

    int n1p = play_deceiful_war(a, b), n2p = 0;

    do {
      n2p = std::max(play_war(a, b), n2p);
    } while (next_permutation(ALL(a)));

    std::cout << "Case #" << t << ": " << n1p << ' ' << n2p << std::endl;
  }

  return 0;
}
