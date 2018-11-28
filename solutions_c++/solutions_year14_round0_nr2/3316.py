#include <cstdio>

using namespace std;

void input(void);
void solve(void);
double get_time(int n);

double c, f, x;
int case_cnt = 1;

int main(void) {
  int t;
  scanf("%d", &t);
  while (t--) {
    input();
    solve();
  }
  return 0;
}

void input(void) {
  scanf("%lf %lf %lf", &c, &f, &x);
}

void solve(void) {
  double best = get_time(0);
  for (int i = 1; ; i++) {
    double t = get_time(i);
    if (t < best) {
      best = t;
    } else {
      break;
    }
  }
  printf("Case #%d: %.7lf\n", case_cnt++, best);
}

double get_time(int n) {
  double t = 0.0;
  for (int i = 0; i < n; i++) {
    t += c / (2 + i * f);
  }
  return t + x / (2 + n * f);
}


