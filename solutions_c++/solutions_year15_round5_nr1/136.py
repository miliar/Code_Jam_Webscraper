#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long int64;

const int oo = 0x3f3f3f3f;
const int NIL = -1;

vector< vector<int> > Tree;
int V, Root, MaxDiff, Solution;
vector<int> Value, Father, Size;

inline void Insert(const int x) {
  Size[x] = 1;
  for (const auto &y: Tree[x])
    Size[x] += Size[y];
  for (int y = Father[x]; y != NIL && Size[y] > 0; y = Father[y])
    Size[y] += Size[x];
}

inline void Erase(const int x) {
  for (int y = Father[x]; y != NIL && Size[y] > 0; y = Father[y])
    Size[y] -= Size[x];
  Size[x] = 0;
}

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int testCount;
  cin >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    cin >> V >> MaxDiff;
    Root = 0;
    Value = Father = Size = vector<int>(V, 0);
    Tree = vector< vector<int> >(V, vector<int>());
    {
      int s, as, cs, rs;
      cin >> s >> as >> cs >> rs;
      int m, am, cm, rm;
      cin >> m >> am >> cm >> rm;
      for (int x = 0; x < V; ++x) {
        Value[x] = s;
        if (x == Root)
          Father[x] = NIL;
        else
          Father[x] = m % x;
        s = (s * as + cs) % rs;
        m = (m * am + cm) % rm;
      }
    }
    for (int x = 1; x < V; ++x)
      Tree[Father[x]].push_back(x);
    vector<int> nodes = vector<int>(V);
    for (int x = 0; x < V; ++x)
      nodes[x] = x;
    sort(nodes.begin(), nodes.end(), [](const int &x, const int &y) -> bool {
      return Value[x] < Value[y];
    });
    Solution = 0;
    for (int l = 0, r = 0; r < V; ++l) {
      while (r < V && Value[nodes[r]] - Value[nodes[l]] <= MaxDiff)
        Insert(nodes[r++]);
      Solution = max(Solution, Size[Root]);
      Erase(nodes[l]);
    }
    cout << "Case #" << test << ": " << Solution << "\n";
  }
  cin.close();
  cout.close();
  return 0;
}
