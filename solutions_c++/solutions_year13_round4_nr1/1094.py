#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int cal(int n) {
  return ((1 + n) * n) / 2;
}

struct Ticket {
  Ticket (int s, int e, int n) : s(s), e(e), num(n) {}
  int s, e, num;
};

int main() {
  int T, C = 1;
  scanf("%d", &T);
  while (T--) {
    int n, m, need = 0;
    scanf("%d%d", &n, &m);
    vector<Ticket> v;
    for (int i = 0; i < m; i++) {
      int s, e, p;
      scanf("%d%d%d", &s, &e, &p);
      need += cal(e - s) * p;
      v.push_back(Ticket(s, e, p));
    }
    while (1) {
      int a = -1, b = -1, max = 0;
      for (int i = 0; i < v.size(); i++)
        for (int j = 0; j < v.size(); j++) {
          if (i == j || v[i].num <= 0 || v[j].num <= 0) continue;
          if (v[i].s <= v[j].s && v[j].s <= v[i].e) {
            int add = (-cal(v[i].e - v[i].s) - cal(v[j].e - v[j].s) + cal(v[i].e - v[j].s) + cal(v[j].e - v[i].s));
            if (add > max) max = add, a = i, b = j;
          }
        }
      if (a == -1) break;
      int c = v[a].num < v[b].num ? v[a].num : v[b].num;
      v[a].num -= c;
      v[b].num -= c;
      // need += c * max;
      // printf("%d\n", max);
      v.push_back(Ticket(v[b].s, v[a].e, c));
      v.push_back(Ticket(v[a].s, v[b].e, c));
    }
    int newNeed = 0;
    for (int i = 0; i < v.size(); i++)
      /*printf("%d %d %d\n", v[i].s, v[i].e, v[i].num), */newNeed += cal(v[i].e - v[i].s) * v[i].num;
    printf("Case #%d: %d\n", C++, newNeed - need);
  }
  return 0;
}
