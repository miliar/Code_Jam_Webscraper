#include <cstdio>

int T;
double C, F, X;
double now;
double ans;

int main(){
  int i;

  freopen( "B-large.in", "r", stdin);
  freopen( "B-large.out", "w", stdout);

  scanf("%d", &T);
  for( int tt = 1; tt <= T; tt++){

    scanf("%lf %lf %lf", &C, &F, &X);

    ans = 0;
    now = 2.0;

    while( ( X / now) > ( C / now + X / ( now + F))){
      ans += C / now;
      now += F;
    }
    ans += X / now;

    printf("Case #%d: ", tt);
    printf("%.7lf\n", ans);
  }
}
