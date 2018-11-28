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
#include <bitset>
using namespace std;

#define gcd(a, b) if (!b) ? return a : return gcd(b, a % b);
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

vector<int> numToVec(long long a) {
  vector<int> v;
  while (a) {
    v.push_back(a % 10);
    a /= 10;
  }
  return v;
}

long long countSheep(long long a) {
  long long count = 1, original = a, last;
  unordered_set<long long> s;
  bitset<10> b;
  while (b.count() != 10) {
    a = original * count;
    if (s.find(a) == s.end()) s.insert(a);
    else return -1;

    vector<int> v = numToVec(a);

    for (int i = 0; i < v.size(); ++i) b[v[i]] = 1;

    ++count;
    last = a;
  }
  return last;
}

int main() {
  int n, case_num = 1;
  cin >> n;
  for (int k = 0; k < n; ++k) {
    int a;
    cin >> a;
    int count = countSheep(a);

    cout << "Case #" << case_num++ << ": ";
    if (count == -1) cout << "INSOMNIA" << endl;
    else cout << count << endl;
  }
}
