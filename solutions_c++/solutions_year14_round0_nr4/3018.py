#include <iostream>
#include <set>
#include <vector>

using namespace std;

const unsigned int NUM_PLAYERS = 2;

int main() {
  // Read in # test cases
  unsigned int T;
  cin >> T;
  for (unsigned int i = 1; i <= T; ++i) {
    // Parse inputs
    unsigned int N;
    vector<set<double> > warWeights(NUM_PLAYERS, set<double>());
    vector<set<double> > deWarWeights(NUM_PLAYERS, set<double>());
    cin >> N;
    for (unsigned int j = 0; j < NUM_PLAYERS; ++j) {
      for (unsigned int k = 0; k < N; ++k) {
        double weight;
        cin >> weight;
        warWeights[j].insert(weight);
	deWarWeights[j].insert(weight);
      }
    }

    // Compute answers 
    // Note that &*(reverse_iterator(i)) == &*(i - 1)
    // (i) War
    int warAns = 0;
    while (!warWeights[0].empty() && !warWeights[1].empty()) {
      set<double>::iterator it2_b = warWeights[1].begin();
      set<double>::reverse_iterator
	it1_e = warWeights[0].rbegin(),
        it2_e = warWeights[1].rbegin();

      if (*it1_e > *it2_e) {
	warWeights[0].erase(--it1_e.base());
	warWeights[1].erase(it2_b);
	++warAns;
      } else {
	warWeights[0].erase(--it1_e.base());
        warWeights[1].erase(--it2_e.base());
      }
    }


    // (ii) Deceitful War
    int deWarAns = 0;
    while (!deWarWeights[0].empty() && !deWarWeights[1].empty()) {
      set<double>::iterator it1_b = deWarWeights[0].begin();
      set<double>::reverse_iterator
	it1_e = deWarWeights[0].rbegin(),
        it2_e = deWarWeights[1].rbegin();

      if (*it1_e > *it2_e) {
        deWarWeights[0].erase(--it1_e.base());
        deWarWeights[1].erase(--it2_e.base());
	++deWarAns;
      } else {
        deWarWeights[0].erase(it1_b);
        deWarWeights[1].erase(--it2_e.base());
      }
    }


    // Print answers
    cout << "Case #" << i << ": " << deWarAns << " " << warAns << "\n";
  }

  return 0;
}
