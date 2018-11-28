#include <iostream>
#include <algorithm>

using namespace std;

long double naomi[2000];
long double ken[2000];

int honest(int n) {
  std::pair<long double, bool> values[2000];

  for (int i = 0; i < n; ++i) {
    values[i]   = make_pair(naomi[i], true);
    values[i+n] = make_pair(ken[i], false);
  }

  sort(values, values + n*2);

  int a = 0;
  int maxa = 0;
  for (int i = 0; i < n*2; ++i) {
    if (values[i].second) --a;
    else ++a;

    maxa = std::max(maxa, a);
  }

  return maxa;
}

int deceitful(int n) {
  int a = 0;
  int b = n-1;
  int points = 0;

  for (int i = 0; i < n; ++i) {
    if (naomi[i] > ken[a]) {
      points++;
      a++;
    } else {
      --b;
    }
  }

  return points;
}

void solve(int TEST) {
  int n;

  cin >> n;
  for (int i = 0; i < n; ++i) cin >> naomi[i];
  for (int i = 0; i < n; ++i) cin >> ken[i];

  sort(naomi, naomi+n);
  sort(ken, ken + n);

  int d = deceitful(n);
  int h = honest(n);

   printf("Case #%d: %d %d\n", TEST, d, h);

}

int main() {
  int n = 0;

  cin >> n;
  for (int i = 0; i < n; i++) {
    solve(i+1);
  }
}

