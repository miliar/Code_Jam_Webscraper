#include <stdio.h>
#include <math.h>

main () {

  int n;
  scanf("%d", &n);
  int cn = 0;
  for (; cn < n; cn ++)
  {
    double c, f, x;
    scanf("%lf %lf %lf", &c, &f, &x);
    double t = 0;
    double rate = 2;
    double best = 100000000000.d;

    while(1){
      double nextt = c/rate;
      double win = x/rate;
       //printf("t: %f, win: %f\n, c: %f", t, win, c);

      if(t+ win < best){
         best = t + win;
      }  else {
        break;
      }
      t += nextt;
      rate += f;
    }
    printf("Case #%d: %.8lf\n", cn+1, best);
  }
  return  0;
}
