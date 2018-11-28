#include <stdio.h>
#include <algorithm>
#include <deque>
#include <list>
#include <vector>

int CalculateDeceitfulWarScore(const std::vector<double>& sorted_naomi,
                               const std::vector<double>& sorted_ken) {
  std::deque<double> naomi(sorted_naomi.begin(), sorted_naomi.end());
  std::deque<double> ken(sorted_ken.begin(), sorted_ken.end());

  int deceitful_war_score = 0;
  while (!naomi.empty() && !ken.empty()) {
    if (naomi.front() < ken.front()) {
      // min(naomi) < min(ken).
      naomi.pop_front();
      ken.pop_back();
    } else {
      naomi.pop_front();
      ken.pop_front();
      ++deceitful_war_score;
    }
  }
  return deceitful_war_score;
}

int CalculateWarScore(const std::vector<double>& sorted_naomi,
                      const std::vector<double>& sorted_ken) {
  std::deque<double> naomi(sorted_naomi.begin(), sorted_naomi.end());
  std::list<double> ken(sorted_ken.begin(), sorted_ken.end());

  int war_score = 0;
  while (!naomi.empty() && !ken.empty()) {
    const double chosen_naomi = naomi.front();
    naomi.pop_front();

    std::list<double>::iterator it =
        std::upper_bound(ken.begin(), ken.end(), chosen_naomi);
    if (it == ken.end()) {
      ken.pop_front();
      ++war_score;
    } else {
      ken.erase(it);
    }
  }
  return war_score;
}

int main() {
  int T = 0;
  scanf("%d", &T);

  std::vector<double> naomi;
  naomi.reserve(1000);
  std::vector<double> ken;
  ken.reserve(1000);

  for (int t = 1; t <= T; ++t) {
    naomi.clear();
    ken.clear();

    int N = 0;
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
      double element = 0.0;
      scanf("%lf", &element);
      naomi.push_back(element);
    }

    for (int i = 0; i < N; ++i) {
      double element = 0.0;
      scanf("%lf", &element);
      ken.push_back(element);
    }

    std::sort(naomi.begin(), naomi.end());
    std::sort(ken.begin(), ken.end());

    printf("Case #%d: %d %d\n",
           t,
           CalculateDeceitfulWarScore(naomi, ken),
           CalculateWarScore(naomi, ken));
  }

  return 0;
}
