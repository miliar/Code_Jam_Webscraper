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

int flips;
void flipPancakes(string& s) {
  char side = s[0];
  int count = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == side) ++count;
    else break;
  }

  if (count == s.size() && side == '+') return;
  
  // Flip
  char newSide;
  if (side == '-') newSide = '+';
  else newSide = '-';
  for (int i = 0; i < count; ++i) {
    s[i] = newSide;
  }
  ++flips;

  flipPancakes(s);
}

int main() {
  int n, case_num = 1;
  cin >> n;
  while (n--) {
    flips = 0;
    string line;
    cin >> line;

    flipPancakes(line);
    cout << "Case #" << case_num++ << ": " << flips << endl;
  }
}
