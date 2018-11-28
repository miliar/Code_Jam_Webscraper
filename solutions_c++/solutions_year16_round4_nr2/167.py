#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 202;

void print_answer(int case_id, long double answer) {
  printf("Case #%d: %.15lf\n", case_id, (double) answer);
}

long double a[MAX_N];
long double p[MAX_N];
long double q[MAX_N];
long double f[MAX_N][MAX_N];

long double calculate_dp(int m, long double p[], long double q[]) {
  memset(f, 0, sizeof(f));

  f[0][0] = 1.0;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j <= i; j++) {
      int k = i - j;

      f[i + 1][j + 1] += f[i][j] * p[i + 1];
      f[i + 1][j] += f[i][j] * q[i + 1];
    }
  }

  return f[m][m / 2];
} 

void solve(int case_id) {
  int n, m; cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }

  sort(a + 1, a + n + 1);
  
  long double answer = 0.0;
  for (int i = 0; i <= m; i++) {
    int h = 0;
    for (int j = 1; j <= i; j++) {
      p[++h] = a[j];
    }

    for (int j = 1; j <= m - i + 1; j++) {
      p[++h] = a[n - j + 1];
    }

    sort(p + 1, p + m + 1);
    for (int j = 1; j <= m; j++) {
      q[j] = 1.0 - p[j];
    }

    answer = max(answer, calculate_dp(m, p, q));
  }


  print_answer(case_id, answer);
}

int main() {
  int cases; cin >> cases;

  for (int i = 1; i <= cases; i++) {
    solve(i);
  }

  return 0;
}