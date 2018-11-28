#include <iostream>
#include <iomanip>
#include <array>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

// I'm sure there's more room for generalization, but this works.
template <typename Winner, typename Loser>
int losing_score(Winner const& winner, Loser const& loser) {
  int score = 0;
  typename Winner::const_iterator iw = winner.begin();
  typename Loser::const_iterator il = loser.begin();
  for (; iw != winner.end(); ++iw) {
    while (il != loser.end() && *il++ > *iw) {
      score += 1;
    }
  }
  return score;
}

int main() {

  int T;
  cin >> T;

  for (int t = 0; t < T; ++t) {
    int n;
    cin >> n;
    vector<double> naomi, ken;

    copy_n(istream_iterator<double>(cin), n, back_inserter(naomi));
    copy_n(istream_iterator<double>(cin), n, back_inserter(ken));

    sort(naomi.begin(), naomi.end(), greater<double>());
    sort(ken.begin(), ken.end(), greater<double>());

    cout << "Case #" << (t + 1) << ": ";
    cout << (n - losing_score(naomi, ken)) << " ";
    cout << losing_score(ken, naomi) << endl;
  }
}

