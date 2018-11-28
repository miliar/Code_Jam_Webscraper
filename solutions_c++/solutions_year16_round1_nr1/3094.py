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

int main() {
  int n, case_num = 1;
  cin >> n;
  while (n--) {
    string s;
    cin >> s;
    list<char> ll;

    ll.push_back(s[0]);
    for (int i = 1; i < s.size(); ++i) {
      if (s[i] >= ll.front()) ll.push_front(s[i]);
      else ll.push_back(s[i]);
    }

    cout << "Case #" << case_num++ << ": ";
    for (list<char>::iterator iter = ll.begin(); iter != ll.end(); ++iter) {
      cout << *iter;
    }
    cout << endl;

  }
}
