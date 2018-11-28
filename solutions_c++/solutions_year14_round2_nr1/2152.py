#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long i64;

int average(int sum, int div) {
  double ds = (double)sum, dd = (double) div;
  double r = ds / dd;
  return (r - floor(r) >= 0.5l) ? (int)ceil(r) : (int)floor(r);
}

void reduce(char *in, char *out, int *dists) {
  char orig = '\0';
  int idx = 0;
  while (*in) {
    if (orig != *in) {
      out[idx] = *in;
      dists[idx] = 0;
      idx++;
      orig = *in;
    } else {
      dists[idx-1]++;
    }
    in++;
  }
  out[idx] = '\0';
}

void run(istream& in, int t) {
  int N;
  char str[100][100];
  char red[100];
  int dists[100][100];
  in >> N;
  for (int i = 0; i < N; ++i) {
    string tt;
    in >> tt;
    strcpy(str[i], tt.c_str());
    if (i == 0) {
      reduce(str[i], red, dists[i]);
    } else {
      char tmp[100];
      reduce(str[i], tmp, dists[i]);
      if (strcmp(tmp, red)) {
        cout << "Case #" << t << ": Fegla Won" << endl;
        return;
      }
    }
  }

  int l = strlen(red);
  int op = 0;
  for (int j = 0; j < l; ++j) {
    int sum = 0;
    for (int i = 0; i < N; i++) {
      sum += dists[i][j];
    }
    int t = average(sum, N);
    for (int i = 0; i < N; i++) {
      int d = dists[i][j] - t;
      op += ((d < 0) ? -d : d);
    }
  }
  cout << "Case #" << t << ": " << op << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    run(cin, i + 1);
  }
}
