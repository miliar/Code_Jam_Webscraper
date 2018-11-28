#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

struct attack {
  int day;
  int start;
  int end;
  int strength;
  attack(int day, int start, int end, int strength): day(day), start(start), end(end), strength(strength) {}
};

bool operator< (const attack& a, const attack& b) {
  return a.day < b.day;
}

const int MAX_LEN = 10000;
const int OFFSET = 5000;
struct wall {
  int h[MAX_LEN];
  wall() {
    memset(h, 0, sizeof(h));
  }

  int getMin(int start, int end) {
    start += OFFSET;
    end += OFFSET;
    int res = h[start];
    for (int i = start; i < end; ++i) {
      if (h[i] < res) {
        res = h[i];
      }
    }
    return res;
  }

  void raise(int start, int end, int height) {
    start += OFFSET;
    end += OFFSET;
    for (int i = start; i < end; ++i) {
      h[i] = max(h[i], height);
    }
  }
};

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    int N;
    scanf("%d", &N);
    vector<attack> all;
    for (int i = 0; i < N; ++i) {
      int firstDay;
      int count;
      int start, end;
      int strength;
      int deltaDays;
      int deltaEast;
      int deltaStrength;
      scanf("%d %d %d %d %d", &firstDay, &count, &start, &end, &strength);
      scanf("%d %d %d", &deltaDays, &deltaEast, &deltaStrength);
      for (int i = 0; i < count; ++i) {
        all.push_back(attack(firstDay + i * deltaDays, start + i * deltaEast, end + i * deltaEast, strength + i * deltaStrength));
      }
    }
    wall w;
    sort(all.begin(), all.end());
    int lastRebuilt = all[0].day;
    int res = 0;
    for (int i = 0; i < all.size(); ++i) {
      const attack& a = all[i];
      if (lastRebuilt != -1 && lastRebuilt != a.day) {
        for (int j = i - 1; j >= 0 && all[j].day == lastRebuilt; --j) {
          w.raise(all[j].start, all[j].end, all[j].strength);
        }
        lastRebuilt = a.day;
      }
//      printf("attack on day %d from %d to %d with power %d\n", a.day, a.start, a.end, a.strength);
      if (w.getMin(a.start, a.end) < a.strength) {
//        printf("successful\n");
        ++res;
      }
    }
    printf("Case #%d: %d\n", t + 1, res);
  }
}
