#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <set>
#include <queue>
#include <cmath>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <ctime>
#include <algorithm>

using namespace std;

typedef pair<double, double> Pair;

double EPS = 1E-10;
int Cmp(const double x) {
  if (abs(x) < EPS) {
    return 0;
  }
  if (x > 0.0) {
    return 1;
  } else {
    return -1;
  }
}

int main() {
  freopen("//Users//zxj//Desktop//poj_input.txt", "r", stdin);
  int cases;
  scanf("%d", &cases);
  for (int i = 0; i < cases; ++i) {
    int N;
    double V, R;
    scanf("%d %lf %lf", &N, &V, &R);
    V *= 1000;
    R *= 1000;
    vector<Pair> points(N);
    for (int i = 0; i < N; ++i) {
      scanf("%lf %lf", &points[i].first, &points[i].second);
    	points[i].first *= 1000;
    	points[i].second *= 1000;
    }
    if (N == 1) {
      if (Cmp(R - points[0].second) == 0) {
        printf("Case #%d: %lf\n", i + 1, V / points[0].first);
      } else {
        printf("Case #%d: IMPOSSIBLE\n", i + 1);
      }
    } else if (N == 2){
      if (Cmp(points[0].second - points[1].second) == 0) {
        if (Cmp(R - points[0].second) == 0) {
          printf("Case #%d: %lf\n", i + 1, V / (points[0].first + points[1].first));
        } else {
          printf("Case #%d: IMPOSSIBLE\n", i + 1);
        }
      } else {
        double v1 = (V * R - V * points[1].second) / (points[0].second - points[1].second);
        double v2 = V - v1;
        if (Cmp(v1) < 0 || Cmp(v2) < 0) {
          printf("Case #%d: IMPOSSIBLE\n", i + 1);
        } else {
        //  cout << v1 << "===" << v2 << endl;
          double t = max(v1 / points[0].first, v2 / points[1].first);
          printf("Case #%d: %lf\n", i + 1, t);
        }
      }
    }
  }
}
