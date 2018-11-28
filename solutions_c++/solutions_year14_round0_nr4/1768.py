#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T , t = 1, N, dscore, score;
  vector<double> naomi;
  vector<double> ken;
  cin >> T;

  while (t <= T) {
    naomi.clear();
    ken.clear();
    dscore = score = 0;
    cin >> N;
    double temp;
    for (int i = 0; i < N; i++) {
      cin >> temp;
      naomi.push_back(temp);
    }
    for (int i = 0; i < N; i++) {
      cin >> temp;
      ken.push_back(temp);
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());

    //deque<double> dwar_n(naomi.begin(), naomi.end());
    deque<double> dwar_k(ken.begin(), ken.end());

    for (int i = 0; i < N; i++) {
      if (naomi[i] < dwar_k[0]) {
        dwar_k.pop_back();
      } else {
        dscore++;
        dwar_k.pop_front();
      }
    }
    
    deque<double> war_k(ken.begin(), ken.end());
    for (int i = 0; i < N; i++) {
      bool win = true;
      for (int j = 0; j < war_k.size(); j++) {
        if (naomi[i] < war_k[j]) {
          war_k.erase(war_k.begin() + j);
          win = false;
          break;
        }
      }
      if (win) {
        score++;
        war_k.pop_front();
      }
    }
    cout << "Case #" << t << ": " << dscore << " " << score;
    if (t != T) cout << "\n";
    t++;
  }
}
