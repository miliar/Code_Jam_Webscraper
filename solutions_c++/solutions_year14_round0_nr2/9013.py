#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
#define INF 1e18
double c, f, x;

double cost_for_n_machines(int n) { 
  double ans = 0; 
  for (int i = 0; i < n; i ++) { 
    ans += c / (2 + i * f);
  }
  ans += x / (2 + n * f);
  return ans;
}

double ternary_search(int low, int high) { 
  if (high - low < 3) { 
    double ans = INF;
    for (int i = low; i <= high; i ++)
      ans = min(ans, cost_for_n_machines(i));
    return ans;
  }
  int left =  low + (high - low) * 1 / 3; 
  int right = low + (high - low) * 2 / 3;
  double leftCost = cost_for_n_machines(left);
  double rightCost = cost_for_n_machines(right);
  if (leftCost < rightCost) { 
    return ternary_search(low, right);
  } else {
    return ternary_search(left, high);
  }
}
int main() {
  freopen("cookie.in", "r", stdin);
  int tests;
  cin >> tests;
  for (int caseno = 1; caseno <= tests; caseno ++) { 
    cin >> c >> f >> x;
    printf("Case #%d: %.7f\n", caseno, ternary_search(0, x));
  }
  return 0;
}
