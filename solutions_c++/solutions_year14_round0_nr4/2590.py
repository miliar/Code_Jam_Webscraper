#include <iostream>
#include <set>

using namespace std;

int score(set<double>& naomi, set<double> ken)
{
  int score = 0;
  for (auto x : naomi) {
    auto it = ken.upper_bound(x);
    if (it == ken.end())
      ++score;
    else
      ken.erase(it);
  }

  return score;
}

int score_deceptive(set<double>& naomi, set<double> ken)
{
  int score = 0;
  for (auto x : naomi) {
    auto it = ken.lower_bound(x);
    if (it != ken.begin()) {
      ++score;
      ken.erase(ken.begin());
    } else {
      it = ken.end();
      ken.erase(--it);
    }
  }

  return score;
}

int solve(set<double> naomi, set<double> ken)
{
  int best_score = score(naomi, ken);

  while (!naomi.empty()) {
    auto it = naomi.begin();
    naomi.erase(it);

    it = ken.end();
    --it;
    ken.erase(it);

    best_score = max(score_deceptive(naomi, ken), best_score);
  }

  return best_score;
}

int main()
{
  int T; cin >> T;
  for (int k = 1; k <= T; ++k) {
    set<double> naomi;
    set<double> ken;

    int N; cin >> N;
    for (int i = 0; i < N; ++i) {
      double x; cin >> x;
      naomi.insert(x);
    }
    for (int i = 0; i < N; ++i) {
      double x; cin >> x;
      ken.insert(x);
    }

    cout << "Case #" << k << ": ";
    cout << solve(naomi, ken) << " " << score(naomi, ken) << "\n";
  }

  return 0;
}
