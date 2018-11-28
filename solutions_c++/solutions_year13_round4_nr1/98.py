#include <cstdio>
#include <algorithm>

using namespace std;

const int mod = 1000002013;

const int MAXN = 1001;

int a[MAXN], b[MAXN], p[MAXN];

int f(int a, int b, int p, int n) {
  int k = b-a;
  return p*(k*n - (k*(k-1)/2));
}

int main(void) {
  int t;
  scanf("%d", &t);
  for(int c = 1; c <= t; ++c) {
    int n, m;
    scanf("%d %d", &n, &m);

    int s = 0;
    for(int i = 0; i < m; ++i) {
      scanf("%d %d %d", a+i, b+i, p+i);
      s += f(a[i], b[i], p[i], n);
    }

    int ch = 1;
    
    int ans = 0;
    while(ch) {
      int maks = 0, p1, p2;
      for(int i = 0; i < m; ++i)
        for(int j = 0; j < m; ++j)
          if(i != j && a[i] <= a[j] && a[j] <= b[i]) {
            int prije = (f(a[i], b[i], p[i], n) + f(a[j], b[j], p[j], n));
            int mini = min(p[i], p[j]);
            int poslije = 0;
            poslije += f(a[i], b[j], mini, n);
            poslije += f(a[i], b[i], p[i]-mini, n);
            poslije += f(a[j], b[i], mini, n);
            poslije += f(a[j], b[j], p[j]-mini, n);
            if(prije-poslije > maks) {
              maks = prije-poslije;
              p1 = i, p2 = j;
            }
          }

      //printf("%d %d %d\n", maks, p1, p2);
      ch = 0;
      if(maks > 0) {
        ch = 1;
        ans += maks;
        int pi = p[p1], pj = p[p2];
        int mini = min(pi, pj);
        p[p1] = p[p2] = mini;
        if(pi > mini) a[m] = a[p1], b[m] = b[p1], p[m] = pi-mini, m++;
        if(pj > mini) a[m] = a[p2], b[m] = b[p2], p[m] = pj-mini, m++;
        swap(b[p1], b[p2]);
      }
    } 
          
    printf("Case #%d: %d\n", c, ans);
  }
  return 0;
}
