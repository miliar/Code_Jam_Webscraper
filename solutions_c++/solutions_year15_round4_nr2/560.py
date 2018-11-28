#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

typedef long double Double;

const int N = 100 + 10;

struct Node {
  Double r, c;
  bool operator < (const Node& node) const {
    return c < node.c;
  }
} nodes[N];

int n;
Double v, x;

Double Solve(std::vector<Node>& vec, Double tmax) {
  Double result = 0;
  Double volumn = 0, temp = 0;
  for (int i = 0; i < vec.size(); ++ i) {
    Double fill = std::min(v - volumn, vec[i].r * tmax);
    temp = (vec[i].c * fill + temp * volumn) / (volumn + fill);
    volumn += fill;
  }
  return temp;
}

bool Check(Double tmax) {
  Double sum = 0;
  for (int i = 1; i <= n; ++ i) {
    sum += nodes[i].r * tmax;
  }
  if (sum < v) {
    return false;
  }

  std::vector<Node> vec;
  for (int i = 1; i <= n; ++ i) {
    vec.push_back(nodes[i]);
  }
  Double minimum = Solve(vec, tmax);
  vec.clear();
  for (int i = n; i >= 1; -- i) {
    vec.push_back(nodes[i]);
  }
  Double maximum = Solve(vec, tmax);
  return minimum <= x && x <= maximum;
  const double EPS = 1E-15;
  return minimum - x <= EPS && x - maximum <= EPS;
}

int main() {
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; ++ t) {
    //fprintf(stderr, "%d\n", t);

    scanf("%d%Lf%Lf", &n, &v, &x);
    for (int i = 1; i <= n; ++ i) {
      scanf("%Lf%Lf", &nodes[i].r, &nodes[i].c);
    }
    if (t == 9) {
      fprintf(stderr, "%d %.5Lf %.5Lf\n", n, v, x);
      for (int i = 1; i <= n; ++ i) {
        fprintf(stderr, "%.5Lf %.5Lf\n", nodes[i].r, nodes[i].c);
      }
    }
    std::sort(nodes + 1, nodes + n + 1);

    Double lower = 0, upper = 1e12;
    Double answer = 0;
    bool flag = false;
    //while (fabs(upper - lower) > 1E-10) {
    for (int counter = 0; counter <= 100; ++ counter) {
      Double middle = (lower + upper) / 2;
      if (Check(middle)) {
        flag = true;
        upper = middle;
      } else {
        lower = middle;
      }
    }
    printf("Case #%d: ", t);
    if (!flag) {
      puts("IMPOSSIBLE");
    } else {
      printf("%.10Lf\n", (lower + upper) / 2);
    }
  }
  return 0;
}
