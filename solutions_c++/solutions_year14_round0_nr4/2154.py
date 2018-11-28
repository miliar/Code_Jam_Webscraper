#include <cstdio>
#include <vector>
#include <functional>

using namespace std;

typedef vector<double>::iterator vdit;

int N;

int deceitful (vector<double> n, vector<double> k) {
  int points = 0;

  while (!n.empty()) {
    double nlast, klast;

    nlast = n[n.size() - 1]; klast = k[k.size() - 1];

    if (nlast < klast) {
      // Deceive!
      n.erase(n.begin());
      k.erase(k.begin() + k.size() - 1);
    }
    else {
      n.erase(n.begin() + n.size() - 1);
      k.erase(k.begin() + k.size() - 1);
      points++;
    }
  }

  return points;
}

int war (vector<double> n, vector<double> k) {
  int points = 0;

  while (!n.empty()) {
    double naomi = n[n.size() - 1];
    vdit ken = upper_bound(k.begin(), k.end(), naomi);

    n.erase(n.begin() + n.size() - 1);
    
    if (ken == k.end()) { points++; k.erase(k.begin()); }
    else k.erase(ken);
  }

  return points;
}

int main(int argc, char *argv[]) {
  int T;

  scanf("%d", &T);

  for (int idx = 1; idx <= T; idx++) {
    scanf("%d", &N);
    
    vector<double> n(N), k(N);

    for (int i = 0; i < N; i++) {
      scanf("%lf", &n[i]);
    }

    for (int i = 0; i < N; i++) {
      scanf("%lf", &k[i]);
    }

    sort(n.begin(), n.end());
    sort(k.begin(), k.end());

    printf("Case #%d: %d %d\n", idx, deceitful(n, k), war(n, k));
  }

  return 0;
}
