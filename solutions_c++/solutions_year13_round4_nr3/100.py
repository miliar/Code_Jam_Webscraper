#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 2002;

int a[MAXN], b[MAXN], c[MAXN], x[MAXN];
vector<int> e[MAXN];

void add(int a, int b) {
  e[a].push_back(b);
  c[b]++;
}

int main(void) {
  int t;
  scanf("%d", &t);
  for(int cc = 1; cc <= t; ++cc) {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i) {
      scanf("%d", a+i);
      e[i].clear();
      c[i] = 0;
    }
    for(int j = 0; j < n; ++j)
      scanf("%d", b+j);

    for(int i = 0; i < n; ++i) {
      bool same = false, prev = false;
      for(int j = i+1; j < n; ++j)
        if(b[i] == b[j] && !same) add(i, j), same = true; else
          if(b[i] < b[j]) add(i, j); else
            if(b[i]-1 == b[j] && !prev) add(j, i), prev = true;
    }

    for(int i = n-1; i >= 0; --i) {
      bool same = false, prev = false;
      for(int j = i-1; j >= 0; --j)
        if(a[i] == a[j] && !same) add(i, j), same = true; else
          if(a[i] < a[j]) add(i, j); else
            if(a[i]-1 == a[j] && !prev) add(j, i), prev = true;
    }
    
    for(int i = 0; i < n; ++i)
      for(int j = 0; j < n; ++j)
        if(c[j] == 0) {
          x[j] = i;
          c[j] = -1;
          for(int k = 0; k < (int)e[j].size(); ++k)
            c[e[j][k]]--;
          break;
        }
    
    printf("Case #%d:", cc);
    for(int i = 0; i < n; ++i)
      printf(" %d", x[i]+1);
    putchar('\n');
  }
  return 0;
}
