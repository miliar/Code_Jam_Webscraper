#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, M, N;
string S[1100];
int Max, Num;
int server[1100];
int next[100][26];

void calc() {
  int total = 0;
  FOR(i, 0, N) {
    int numstr = 0;
    memset(next, -1, sizeof(next));
    int nodes = 1;
    FOR(j, 0, M) {
      if (server[j] != i) continue;
      numstr++;
      int cur = 0;
      FOR(k, 0, sz(S[j])) {
        int c = S[j][k] - 'A';
        if (next[cur][c] == -1) {
          next[cur][c] = nodes++;
        }
        cur = next[cur][c];
      }
    }
    if (numstr == 0) return;
    total += nodes;
  }
  if (total > Max) {
    Max = total;
    Num = 1;
  } else if (total == Max) {
    Num++;
  }
}

void rek(int ind) {
  if (ind == M) {
    calc();
    return;
  }
  FOR(i, 0, N) {
    server[ind] = i;
    rek(ind+1);
  }
}

int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    cin >> M >> N;
    FOR(i, 0, M) cin >> S[i];
    Max = 0, Num = 0;
    rek(0);
    cout << "Case #" << cs << ": " << Max << " " << Num << endl;
  }
	return 0;
}
