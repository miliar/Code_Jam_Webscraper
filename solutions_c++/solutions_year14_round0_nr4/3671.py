#include <algorithm>
#include <iostream>
#include <deque>

using namespace std;

int get_war_score(deque<double> naomi, deque<double> ken) {
  int score = 0;
  for (int i = 0; i < naomi.size(); ++i) {
    double weight = naomi[i];
    double bigger = 0;
    for (int j = 0; j < ken.size(); ++j) {
      if (ken[j] > weight) {
        bigger = ken[j];
        break;
      }
    }
    if (bigger > weight) {
      ken.erase(remove(ken.begin(), ken.end(), bigger), ken.end());
    } else {
      ++score;
    }
  }
  return score;
}

int get_deceitful_war_score(deque<double> naomi, deque<double> ken) {

  int score = 0;
  while(ken.size() > 0) {
    double best = ken.back();
    double tell = 0;
    for (double weight : naomi) {
      if (weight < best)
        continue;
      tell = weight;
      break;
    }

    if (tell == 0) {
      naomi.pop_front();
    } else {
      naomi.erase(remove(naomi.begin(), naomi.end(),tell), naomi.end());
      ++score;
    }
    ken.pop_back();
  }
  return score;
}


int main() {

  int num_cases;
  cin >> num_cases;

  for (int i = 1; i <= num_cases; ++i) {

    int num_boxes;
    deque<double> naomi;
    deque<double> ken;
    cin >> num_boxes;
    naomi.clear();
    ken.clear();

    double weight;
    for (int i = 0; i < num_boxes; ++i) {
      cin >> weight;
      naomi.push_back(weight);
    }
    for (int i = 0; i < num_boxes; ++i) {
      cin >> weight;
      ken.push_back(weight);
    }

    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    int war_score = get_war_score(naomi, ken);
    int deceitful_war_score = get_deceitful_war_score(naomi, ken);
    cout << "Case #" << i << ": " << deceitful_war_score << " " << war_score << endl;
  }

}
