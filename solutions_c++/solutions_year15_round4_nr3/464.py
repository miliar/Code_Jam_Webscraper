#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> MI;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> MII;
typedef long long ll;
typedef vector<ll> Vll;
typedef vector<Vll> Mll;
#define X first
#define Y second

const int inf = 1e9;
const double eps = 1e-9;

const int ANY = -1;
const int ENG = 0;
const int FR = 1;
const int BOTH = 2;
VI values;
void setX(int id, int x) {
  if (values[id] == ANY) values[id] = x;
  else {
    if (values[id] != x) values[id] = BOTH;
    else values[id] = x;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  int T; cin >> T;
  int ncase = 0;
  while (T--) {
    int N; cin >> N;
    MI sentences(N);
    cin.ignore();
    map<string,int> msi;
    int id = 0;
    for (int i = 0; i < N; ++i) {
      string line;
      getline(cin,line);
      stringstream ss(line);
      string s;
      while (ss >> s) {
        if (msi.find(s) == msi.end()) {
          sentences[i].push_back(id);
          msi[s] = id++;
        }
        else {
          sentences[i].push_back(msi[s]);
        }
      }
    }

    int ans = 1e9;
    for (int mask = 0; mask < (1<<(N-2)); ++mask) {
      values = VI(id, -1);
      for (int i = 0; i < int(sentences[0].size()); ++i)
        setX(sentences[0][i], ENG);
      for (int i = 0; i < int(sentences[1].size()); ++i)
        setX(sentences[1][i], FR);

      // For all other sentences
      for (int i = 0; i < (N-2); ++i) {
        int x = 0;
        if (mask & (1<<i)) x = 1;
        for (int j = 0; j < int(sentences[i+2].size()); ++j) {
          setX(sentences[i+2][j], x);
        }
      }

      // Count both
      int t = 0;
      for (int i = 0; i < id; ++i) {
        if (values[i] == BOTH) ++t;
      }
      ans = min(ans, t);
      
    }
    cout << "Case #" << ++ncase << ": " << ans << endl;
  }


   
}
