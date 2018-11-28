#include <queue>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <map>
#include <algorithm>

using namespace std;

typedef struct {
  vector<int> state;
  int time;
} Gogo;

int main() {
  int ntc;
  scanf("%d", &ntc);

  for (int tc = 0; tc < ntc; ++tc) {
    map<vector<int>, int> bfsSpace;
    queue<Gogo> q;

    vector<int> space;
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      int p;
      scanf("%d", &p);
      space.push_back(p);
    }
    sort(space.begin(), space.end());
    bfsSpace.insert(pair<vector<int>, int>(space, 0));
    int minim = space[space.size() - 1];
    int maxSearch = minim;

    // Do BFS!
    Gogo st = { space, 0 };
    q.push(st);
    while (!q.empty()) {
      Gogo front = q.front();
      q.pop();

      int biggest = front.state[front.state.size() - 1];
      minim = minim > biggest + front.time ? biggest + front.time : minim;
      if (biggest <= 2) {
        continue;
      }

      int halfBiggest = biggest / 2;
      for (int i = 2; i <= halfBiggest; ++i) {
        vector<int> newState(front.state);
        newState[newState.size() - 1] = i;
        newState.push_back(biggest - i);
        sort(newState.begin(), newState.end());

        if (bfsSpace.find(newState) == bfsSpace.end()) {
          bfsSpace.insert(pair<vector<int>, int>(newState, front.time + 1));
          Gogo nst = { newState, front.time + 1 };
          q.push(nst);
        }
      }
    }

    printf("Case #%d: %d\n", tc + 1, minim);
  }

  return 0;
}
