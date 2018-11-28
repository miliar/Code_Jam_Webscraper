#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

int war(int n, set<double> naomi, set<double> ken) {
  int score = 0;
  for (int i = 0; i < n; ++i) {
    double naomi_choice = *naomi.begin();
    set<double>::iterator ken_it = ken.lower_bound(naomi_choice);
    double ken_choice = ken_it == ken.end() ? *ken.begin() : *ken_it;
    if (naomi_choice > ken_choice) score++;
    // cout << "naomi> " << naomi_choice << " ken> " << ken_choice << " score = " << score << endl;
    naomi.erase(naomi_choice);
    ken.erase(ken_choice);
  }
  return score;
}

int deceptive_war(int n, set<double> naomi, set<double> ken) {
  int score = 0;
  while(!naomi.empty()) {
    double ken_chosen = *ken.begin();
    set<double>::iterator it = naomi.upper_bound(ken_chosen);
    double bound = (it == naomi.end()) ? *naomi.rbegin() : *it;
    if (bound > ken_chosen) score++;
    //cout << "2  naomi > " << bound << " ken > " << ken_chosen << " score = " << score << endl;
    naomi.erase(bound);
    ken.erase(*ken.begin());
  }
  return score;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int n;
    cin >> n;
    set<double> naomi;
    set<double> ken;
    // double naomi[n], ken[n];
    for (int j = 0; j < n; ++j) {
      double w;
      cin >> w;
      naomi.insert(w);
    }
    for (int j = 0; j < n; ++j) {
      double w;
      cin >> w;
      ken.insert(w);
    }
    // for (int j = 0; j < n; ++j) cin >> naomi[j];
    // for (int j = 0; j < n; ++j) cin >> ken[j];
    int wr = war(n, naomi, ken);
    int dr = deceptive_war(n, naomi, ken);
    printf("Case #%d: %d %d\n", i+1, dr, wr);
  }
  return 1;
}
