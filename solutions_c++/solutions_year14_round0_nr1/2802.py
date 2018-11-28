#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;

const int N = 4;

int maze1[N][N];
int maze2[N][N];


int main() {
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t, a, b, cases = 0;
  cin >> t;
  while (t--) {
    cin >> a;
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j)
        cin >> maze1[i][j];
    cin >> b;
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j)
        cin >> maze2[i][j];
    bool vis[16+1] = {0};
    for (int i = 0; i < N; ++i)
      vis[maze1[a-1][i]] = 1;
    int cnt = 0;
    int num;
    for (int i = 0; i < N; ++i)
      if (vis[maze2[b-1][i]]) {
        ++cnt;
        num = maze2[b-1][i];
      }
    cout << "Case #" << ++cases << ": ";
    if (cnt > 1)
      cout << "Bad magician!" << endl;
    else if (cnt == 0)
      cout << "Volunteer cheated!" << endl;
    else
      cout << num << endl;
  }
  return 0;
} 
