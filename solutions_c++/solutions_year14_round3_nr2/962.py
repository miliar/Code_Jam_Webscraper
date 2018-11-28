#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <set>


using namespace std;

#define PI acos(-1.)
#define EPS 1e-7
#define LL long long
#define U unsigned int
#define LU long unsigned
#define LLU long long unsigned


LLU mod;

string cars[100];
map<char, set<int> > graph;


LLU calc(int n, int num, int N, set<char> chars, vector<bool> was) {
  LLU sum = 0;
  was[n] = true;
  for (int i = 1; i < cars[n].size(); ++i) {
    set<char>::iterator it;
    if ((it = chars.find(cars[n][i])) != chars.end() && cars[n][i] != cars[n][i-1]) {
      return 0;
    } else {
      chars.insert(cars[n][i]);
    }
  }
  if (num == N - 1) return 1;
  char last = cars[n][cars[n].size() - 1];
  int k = 0; int l = 0;
  if (graph.find(last) != graph.end()) {
    for (set<int>::iterator it = graph[last].begin(); it != graph[last].end(); ++it) {
      ++k;
      if (!was[*it]) {
        sum = (sum + calc(*it, num + 1, N, chars, was)) % mod;
      } else {
        ++l;
      }
    }
  }
  if (k == l) {
    for (int i = 0; i < N; ++i) {
      if (!was[i] && chars.find(cars[i][0]) == chars.end()) {
        chars.insert(cars[i][0]);
        sum = (sum + calc(i, num + 1, N, chars, was)) % mod;
        chars.erase(cars[i][0]);
      }
    }
  }
  return sum;
}


int main() {
  // Declare members
  mod = 1000000007;
  int num_case;
  cin >> num_case;
  int N;


  for (int nc = 1; nc <= num_case; ++nc) {
    // Init members
    cin >> N;
    graph.clear();
    
    for (int i = 0; i < N; ++i) {
      cin >> cars[i];
      graph[cars[i][0]].insert(i);
    }
    
    LLU sum = 0;
    for (int i = 0; i < N; ++i) {
      set<char> chars;
      chars.insert(cars[i][0]);
      vector<bool> was;
      was.resize(N);
      for (int j = 0; j < N; ++j) {
        was[j] = false;
      }
      sum = (sum + calc(i, 0, N, chars, was)) % mod;
    }

    // Print output for case j
    cout << "Case #" << nc << ": " << sum << endl;
  }


  return 0;
}
