#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
using namespace std;

bool done;
vector<int> ord;
int n;

void check() {
  vector<int> t[2];
  t[0] = ord;
  int k = 1<<n;
  while(k != 1) {
    for (int i=0;i<k;i+=2) {
      if (t[0][i] == t[0][i+1]) {
        return;
      }
      if (t[0][i] + t[0][i+1] == 2) {
        t[1].push_back(0);
      } else {
        t[1].push_back(max(t[0][i], t[0][i+1]));
      }
    }
    t[0].swap(t[1]);
    t[1].clear();

    k /= 2;
  }
  done = true;
  for (int i : ord) {
    printf("%c", "RPS"[i]);
  }
}

void solve(int r, int p, int s) {
  if (done) return;
  if(r + p + s == 0) {
    check();
    return;
  }
  if (p) {
    ord.push_back(1);
    solve(r, p-1, s);
    ord.pop_back();
  }
  if (r) {
    ord.push_back(0);
    solve(r-1, p, s);
    ord.pop_back();
  }
  if (s) {
    ord.push_back(2);
    solve(r, p, s-1);
    ord.pop_back();
  }
}


int main() {
  int Z;
  scanf("%d", &Z);
  for (int z=1;z<=Z;z++) {
    printf("Case #%d: ", z);
    int r, p, s;
    scanf("%d %d %d %d", &n, &r, &p, &s);
    done = false;
    ord.clear();
    solve(r, p, s);
    if (!done) {
      printf("IMPOSSIBLE");
    }
    printf("\n");
  }
  return 0;
}
