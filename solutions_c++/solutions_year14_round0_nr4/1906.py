#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXN = 1001;

double naomi[MAXN];
double ken[MAXN];
int n;

int war(double a[], double b[]) {
  int res = 0;
  int i = n - 1;
  int j = n - 1;

  for (int k = 0; k < n; ++k) {
    if (b[j] > a[i]) {
      --j;
      --i;
    } else {
      --i;
      ++res;
    }
  }
  return res;
}

int dwar(double a[], double b[]) {
  int res = 0;
  int i = 0;
  int j = 0;
  
  for (int k = 0; k < n; ++k) {
    if (a[i] > b[j]) {
      ++res;
      ++i;
      ++j;
    } else {
      ++i;
    }
  }

  return res;
}

void solve(int test) {
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> naomi[i];
  }
  for (int i = 0; i < n; ++i) {
    cin >> ken[i];
  }
  sort(naomi, naomi + n);
  sort(ken, ken + n);
  int w = war(naomi, ken);
  int dw = dwar(naomi, ken);

  cout << "Case #" << test << ": " << dw << " " << w << "\n";
}

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  int nTests;
  cin >> nTests;
  for (int test = 1; test <= nTests; ++test) {
    solve(test);
  }
  return 0;
}
