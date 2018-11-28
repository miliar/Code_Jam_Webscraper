#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

void eraseGT(vector<double> &naomi, double val) {
  int lo = 0, hi = naomi.size() - 1, md;

  while (lo < hi) {
    md = lo + (hi - lo) / 2;
    if (naomi[md] < val) {
      lo = md + 1;
    } else {
      hi = md;
    }
  }
  // cout << endl << "\t" << val << " < " << naomi[lo] << endl;
  naomi.erase(naomi.begin()+lo);
}

void DW(const vector<double> &naomi, const vector<double> &ken) {
  int nPts = 0;
  vector<double> Naomi(naomi);
  vector<double> Ken(ken);

  while (!Naomi.empty()) {
    int idx = Naomi.size() - 1;
    if (Naomi[idx] < Ken[idx]) {
      Ken.pop_back();
      Naomi.erase(Naomi.begin());
    } else {
      ++nPts;
      eraseGT(Naomi, Ken[0]);
      Ken.erase(Ken.begin());
    }
  }

  printf("%d ", nPts);
}

void W(const vector<double> &naomi, const vector<double> &ken) {
  int nPts = 0;
  vector<double> Naomi(naomi);
  vector<double> Ken(ken);

  while (!Naomi.empty()) {
    int idx = Naomi.size() - 1;
    if (Naomi[idx] > Ken[idx]) {
      ++nPts;
      Naomi.pop_back();
      Ken.erase(Ken.begin());
    } else {
      Naomi.pop_back();
      Ken.pop_back();
    }
  }

  printf("%d", nPts);
}

int main() {
  int T, N;
  cin >> T;
  double val;
  vector<double> Naomi, Ken;
  for (int j = 0; j < T; ++j) {
    cin >> N;
    Naomi.clear();
    for (int i = 0; i < N; ++i) {
      cin >> val;
      Naomi.push_back(val);
    }
    sort(Naomi.begin(), Naomi.end());

#if 0
    cout << "\tSorted Naomi:";
    for (auto d : Naomi) {
      cout << "\t" << d;
    }
    cout << endl;
#endif

    Ken.clear();
    for (int i = 0; i < N; ++i) {
      cin >> val;
      Ken.push_back(val);
    }
    sort(Ken.begin(), Ken.end());

#if 0
    cout << "\tSorted Ken:";
    for (auto d : Ken) {
      cout << "\t" << d;
    }
    cout << endl;
#endif

    printf("Case #%d: ", j+1);
    DW(Naomi, Ken);
    W(Naomi, Ken);
    printf("\n");
  }

  return 0;
}
