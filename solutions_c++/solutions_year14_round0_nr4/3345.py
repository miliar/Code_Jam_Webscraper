#include <stdio.h>
#include <list>
#include <vector>

bool Ken(double naomi_wood, std::list<double> *ken_woods) {
  if (naomi_wood > ken_woods->back()) {
    ken_woods->pop_front();
    return false;
  } else {
    std::list<double>::iterator it;
    for (it = ken_woods->begin(); it != ken_woods->end(); ++it) {
      if (*it > naomi_wood) break;
    }
    ken_woods->erase(it);
    return true;
  }
}

int FirstAnswer(std::list<double> *naomi_woods,
                std::list<double> *ken_woods) {
  int size = naomi_woods->size();
  int score = 0;
  for (int i = 0; i < size; ++i) {
    if (naomi_woods->front() < ken_woods->front()) {
      naomi_woods->pop_front();
      ken_woods->pop_back();
    } else {
      naomi_woods->pop_front();
      ken_woods->pop_front();  
      score++;    
    }
  }

  return score;
}

int main() {
  int n_case;
  scanf("%d", &n_case);

  for (int n = 1; n <= n_case; ++n) {
    int n_woods;
    std::vector<double> naomi_vec;
    scanf("%d", &n_woods);
    double wood;
    for (int i = 0; i < n_woods; ++i) {
      scanf("%lf", &wood);
      naomi_vec.push_back(wood);
    }
    sort(naomi_vec.begin(), naomi_vec.end());
    std::list<double> naomi(naomi_vec.begin(), naomi_vec.end());

    std::vector<double> ken_vec;
    for (int i = 0; i < n_woods; ++i) {
      scanf("%lf", &wood);
      ken_vec.push_back(wood);
    }
    sort(ken_vec.begin(), ken_vec.end());
    std::list<double> ken(ken_vec.begin(), ken_vec.end());

    int first_answer = FirstAnswer(&naomi, &ken);

    naomi = std::list<double>(naomi_vec.begin(), naomi_vec.end());
    ken = std::list<double>(ken_vec.begin(), ken_vec.end());
    int second_answer = 0;
    for (std::list<double>::reverse_iterator
         it = naomi.rbegin(); it != naomi.rend(); ++it) {
      if (Ken(*it, &ken) == false) second_answer++;
    }

    printf("Case #%d: %d %d\n", n, first_answer, second_answer);
  }
}