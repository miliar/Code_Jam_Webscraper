#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int search_weight(double x, vector<double> list) {
  for (int i= 0; i < list.size(); ++i) {
    if (x < list[i]) {
      return i;
    }
  }
  return -1;
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N;
    cin >> N;
    vector<double> naomi, ken, naomi2, ken2;
    for (int j = 0; j < N; ++j) {
      double w;
      cin >> w;
      naomi.push_back(w);
      naomi2.push_back(w);
    }
    for (int j = 0; j < N; ++j) {
      double w;
      cin >> w;
      ken.push_back(w);
      ken2.push_back(w);
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    int victories = 0;
    for (int j = 0; j < N; ++j) {
      double ken_w = ken.front();
      int naomi_index = search_weight(ken_w, naomi);
      if (naomi_index != -1) {
        victories++;
        ken.erase(ken.begin());
        naomi.erase(naomi.begin() + naomi_index);
      } else {
        ken.erase(ken.begin());
        naomi.erase(naomi.begin());
      }
    }
    sort(naomi2.begin(), naomi2.end());
    sort(ken2.begin(), ken2.end());
    int losses = 0;
    for (int j = 0; j < N; ++j) {
      double naomi_w = naomi2.back();
      int ken_index = search_weight(naomi_w, ken2);
      if (ken_index != -1) {
        losses++;
        naomi2.pop_back();
        ken2.erase(ken2.begin() + ken_index);
      } else {
        naomi2.pop_back();
        ken2.erase(ken2.begin());
      }
    }
    cout << "Case #" << i << ": " << victories << " " << (N - losses) << endl;
  }
  return 0;
}
