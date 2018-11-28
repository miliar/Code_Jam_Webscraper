#include <cstdio>

double time_required(double goal, double current, double production) {
  if (current >= goal)
    return 0.0;

  return (goal-current)/production;
}

double solve() {
  double cost,farm_production,goal;
  double production = 2.0;
  double current_state = 0.0;
  double current_time = 0.0;
  scanf("%lf %lf %lf",&cost,&farm_production,&goal);
  double finish_time1, finish_time2, purchase_time;
  do {
    finish_time1 = current_time + time_required(goal, current_state, production);
    purchase_time = time_required(cost, current_state, production);
    production += farm_production;
    current_time += purchase_time;
    finish_time2 = current_time + time_required(goal, 0.0, production);
    //    printf("goal: %f current_state: %f production: %f finish_time1: %f purchase_time: %f finish_time2: %f\n", goal, current_state, production, finish_time1, purchase_time, finish_time2);
  } while (finish_time2 < finish_time1);
  return finish_time1;
}

int main() {
  int t;
  scanf("%d",&t);
  for (int tc=1; tc<=t; tc++) {
    double answer = solve();
    printf("Case #%d: %.7f\n", tc, answer);
  }
}
