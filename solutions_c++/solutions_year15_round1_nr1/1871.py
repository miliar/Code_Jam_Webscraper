#include <cstdio>

int m[1001];

int main(){
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++){
    int N;
    long long y = 0, z = 0, zHigh = 10001, zLow = -1, h, l, diff1, diff2, aux;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) scanf("%d", &(m[i]));

    for (int i = 1; i < N; i++) {
      if (m[i] < m[i-1]) y += m[i-1] - m[i];

      // For z
      if (m[i] <= m[i-1]){
        diff1 = m[i-1] - m[i];
        diff2 = m[i-1];

        if (diff1 > diff2){
          aux = diff1;
          diff1 = diff2;
          diff2 = aux;
        }

        if (diff1 > zLow) zLow = diff1;
        if (diff2 < zHigh) zHigh = diff2;
//printf("%d %d - %d %d\n", zLow, zHigh, diff1, diff2);
      } // TODO else
    }

    if (zLow != zHigh) zHigh = zLow;

    for (int i = 0; i < N-1; i++) {
      if (m[i] > zHigh) z += zHigh;
      else z += m[i];
    }

    printf("Case #%d: %lld %lld\n", t, y, z);
  }
  
  return 0;
}