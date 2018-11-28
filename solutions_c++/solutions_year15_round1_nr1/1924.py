#include <cstdio>
#include <algorithm>

#define rep(i,n) for (int i = 0; i < n; i++)

using namespace std;

int main(void)
{
  int T;
  scanf ("%d",&T);
    rep (t,T)
      {
        int N;
        scanf ("%d",&N);
        int m[1000];
        int a1 = 0,a2 = 0;
        int d = 0;
        rep (i,N)
          {
            int a;
            scanf ("%d",&a);
            m[i] = a;
            if (i > 0) {
              a1 += max (0,m[i-1] - m[i]);
              d = max (d,m[i-1] - m[i]);
            }
          }
        
        rep (i,N)
          {
            if (i > 0) {
              a2 += min (d,m[i-1]);
            }
          }
        printf ("Case #%d: %d %d\n",t+1,a1,a2);
      }
  return 0;
}

