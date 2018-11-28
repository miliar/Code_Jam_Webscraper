#include <cstdio>
#include <vector>

using namespace std;

#define NMAX 12

#define min(a, b) ((b)<(a) ? (b) : (a))

int countsort(int tab[NMAX], int size) {
  int nswaps = 0;
  bool changed;
  while (1) {
    changed = false;
    for (int i = 0; i < size - 1; i++)
      if (tab[i] > tab[i+1]) {
        int tmp;
        tmp = tab[i];
        tab[i] = tab[i+1];
        tab[i+1] = tmp;
        changed = true;
        nswaps++;
      }
    if (!changed)
      break;
  }
  return nswaps;
}

int main() {
  int ncases;
  scanf("%d", &ncases);
  for (int ncase = 0; ncase < ncases; ncase++) {
    int N;
    scanf("%d", &N);
    vector<int> v;
    v.clear();
    for (int i= 0 ;i < N; i++ ) {
      int tmp;
      scanf("%d", &tmp);
      v.push_back(tmp);
    }
    long best = 100000000000;
    for (int p = 0; p < (1 << N); p++) {
      int cnt = 0; // num of 1, that go left
      for (int i = 0; i < N; i++)
        if (p & (1 << i))
          cnt++;
      long nm = 0, seen = 0;
      for (int i = 0; i < N; i++) {
        if (p & (1 << i))
          seen++;
        else
          nm+= (cnt - seen); // still to jump
      }
      int tosort[NMAX];
      int pos = 0;
      for (int i = 0; i < N; i++)
        if (p & (1 << i))
          tosort[pos++] = v[i];
      nm += countsort(tosort, pos);  
      pos = 0;
      for (int i = N-1; i >= 0; i--)
        if (!(p & (1 << i)))
          tosort[pos++] = v[i];
      nm += countsort(tosort, pos);  
      //if (best > nm) {
        //printf("improved to %ld with %d\n", nm, p);
      //}
      best = min(best, nm);
    }
    printf("Case #%d: %ld\n", ncase+1, best);
  }
  return 0;
}
