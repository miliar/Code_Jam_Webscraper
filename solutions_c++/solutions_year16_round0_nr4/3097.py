#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <fstream>
#include <queue>
#include <stack>
#include <list>
#include <sstream>
#include <bitset>
#include <algorithm>
#include <utility>
#include <climits>
using namespace std;

#define gcd(a, b) return (!b) ? a : (b, a % b);
#define lcm(n, m) (m * n) / gcd(m, n);

#define print(v) for (int i = 0; i < v.size(); ++i) cout << v[i] << " "; cout << endl;
template <class T>
void printMatrix(vector< vector< T > >& matrix) {
  for (int i = 0; i < matrix.size(); ++i) {
    for (int j = 0; j < matrix[i].size(); ++j) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
}

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector< ii > vii;

const int UNVISITED = -1;
const int VISITED = 1;
const int INF = 1000000005;

vector<vi> AdjMatrix;
vector<int> dfs_num;

string findGold(int k, int c, int s) {
  if (k == 1) return "1";

  if (c == 1) {
    if (k > s)
      return "IMPOSSIBLE";
    else { 
      string s = "";
      for (int i = 1; i <= k; ++i) {
	s += to_string(i);
	if (i != k) s += ' ';
      }
      return s;
    }
  }

  if (s <= k - 2) {
    return "IMPOSSIBLE";
  } else {
    string s = "";
    for (int i = 2; i <= k; ++i) {
      s += to_string(i);
      if (i != k) s += ' ';
    }
    return s;
  }
  
}

int main() {
  int n, case_num = 1;
  cin >> n;
  while (n--) {
    int k, c, s;
    cin >> k >> c >> s;
    cout << "Case #" << case_num++ << ": " << findGold(k, c, s) << endl;
  }
}
