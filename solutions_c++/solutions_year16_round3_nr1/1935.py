#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;

const int MAXN = 26;

int N;

struct data {
  int id;
  int cnt;
  friend bool operator <(const data& a, const data& b) {
    return a.cnt < b.cnt;
  }
} d[MAXN];

priority_queue<data> pq;

bool check(const vector<int>& v, int numLeft) {
  for (int i = 0; i < N; ++i) {
    if (v[i] > numLeft / 2) {
      return false;
    }
  }
  return true;
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int T = 1; T <= cases; ++T) {
    scanf("%d", &N);
    int M = 0;
    for (int i = 0; i < N; ++i) {
      d[i].id = i;
      scanf("%d", &d[i].cnt);
      M += d[i].cnt;
    }
    printf("Case #%d: ", T);
    int space = 0;
    int cnt = 0;
    while (1) {
      data maxData1;
      maxData1.cnt = 0;
      maxData1.id = -1;
      for (int i = 0; i < N; ++i) {
        if (maxData1 < d[i]) {
          maxData1 = d[i];
        }
      }
      if (maxData1.id != -1) {
        d[maxData1.id].cnt -= 1;
      } else {
        break;
      }
      data maxData2;
      maxData2.cnt = 0;
      maxData2.id = -1;
      for (int i = 0; i < N; ++i) {
        if (maxData2 < d[i]) {
          maxData2 = d[i];
        }
      }
      if (space++) putchar(' ');
      if (maxData2.id != -1) {
        d[maxData2.id].cnt -= 1;
        bool ok = true;
        for (int i = 0; i < N; ++i) {
          if (M - cnt - 2 < 2 * d[i].cnt) {
            ok = false;
          }
        }
        if (!ok) {
          d[maxData2.id].cnt += 1;
          printf("%c", maxData1.id + 'A');
          cnt += 1;
        } else {
          printf("%c%c", maxData1.id + 'A', maxData2.id + 'A');
          cnt += 2;
        }
      } else {
        printf("%c", maxData1.id + 'A');
        cnt += 1;
      }
      for (int i = 0; i < N; ++i) {
        if (M - cnt < 2 * d[i].cnt) {
          puts("@@@@@");
        }
      }
    }
    puts("");
    // do {
    //   for (int i = 0; i < M; ++i) {

    //   }
    // } while (next_permutation())
  }
}