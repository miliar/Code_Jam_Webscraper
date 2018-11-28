#include <cstdio>
#include <deque>
#include <algorithm>
#include <vector>
#include <list>

using namespace std;

vector<double> ken, naomi;

int solve2() {
  deque<double> KEN, NAOMI;
  for (int i = 0; i < ken.size(); ++i) KEN.push_back(ken[i]);
  for (int i = 0; i < naomi.size(); ++i) NAOMI.push_back(naomi[i]);
  int sol = 0;

  while (KEN.size()) {
    if (KEN.back() < NAOMI.back()) {
      KEN.pop_front();
      NAOMI.pop_back();
      ++sol;
    } else {
      KEN.pop_back();
      NAOMI.pop_back();
    }
  }
  return sol;
}

int solve1() {
  list<double> KEN, NAOMI;
  for (int i = 0; i < ken.size(); ++i) KEN.push_back(ken[i]);
  for (int i = 0; i < naomi.size(); ++i) NAOMI.push_back(naomi[i]);
  int sol = 0;
  list<double>::iterator naomi_iter = NAOMI.begin();

  while (naomi_iter != NAOMI.end()) {
    while (naomi_iter != NAOMI.end() && *naomi_iter < *KEN.begin()) {
      ++naomi_iter;
    }
    if (naomi_iter != NAOMI.end()) {
      ++sol;
      ++naomi_iter;
      KEN.pop_front();
    }
  }
  return sol;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    int N;
    scanf("%d", &N);
    ken.resize(N);
    naomi.resize(N);
    for (int i = 0; i < naomi.size(); ++i) scanf("%lf", &naomi[i]);
    for (int i = 0; i < ken.size(); ++i) scanf("%lf", &ken[i]);
    sort(ken.begin(), ken.end());
    sort(naomi.begin(), naomi.end());

    printf("Case #%d: %d %d\n", tt, solve1(), solve2());
  }
  return 0;
}
