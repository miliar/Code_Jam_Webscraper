#include <cstdio>

void solve(int tt)
{
  double s = 2;
  int farm = 0;
  double elapsed_time = 0;
  double c, f, x;

  scanf("%lf %lf %lf",&c,&f,&x);

  double best_time = x/2;
  
  while(true) {
    elapsed_time += c/s;
    s += f;
    double current_time = elapsed_time + (x / s);
    if(current_time > best_time)
      break;
    best_time = current_time;
  }
  printf("Case #%d: %.7lf\n",tt+1,best_time);
}

main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++)
    solve(tt);
}
