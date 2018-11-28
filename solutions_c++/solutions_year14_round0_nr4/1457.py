#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

vector<double> NP;
vector<double> KP;
vector<double> NC;
vector<double> KC;

int main() {

  int tcase;

  cin >> tcase;

  for (int T=1; T<=tcase; T++) {
    int n;
    double in;

    NP.clear();
    KP.clear();
    NC.clear();
    KC.clear();

    cin >> n;
    for (int i=0; i<n; ++i){
      cin >> in;
      NP.push_back(in);
      NC.push_back(in);
    }
    for (int i=0; i<n; ++i) {
      cin >> in;
      KP.push_back(in);
      KC.push_back(in);
    }

    sort(NC.begin(), NC.end());
    sort(KC.begin(), KC.end());

    int winC = 0;
    for (int i=0; i<n; ++i) {
      double NNNC_f, KKKC_f;

      NNNC_f = NC.front();
      KKKC_f = KC.front();

      vector<double>::iterator up = upper_bound(NC.begin(), NC.end(), KKKC_f);
      if (up == NC.end()) {
        NC.pop_back();
        KC.erase(KC.begin());
      }
      else {
        NC.erase(up);
        KC.erase(KC.begin());
        winC++;
      }
    }














    sort(NP.begin(), NP.end());
    sort(KP.begin(), KP.end());

    int winP = 0;
    for (int i=0; i<n; ++i) {
      double NNNP, KKKP;

      NNNP = NP.back();
      NP.pop_back();

      vector<double>::iterator low,up;
      low = upper_bound(KP.begin(), KP.end(), NNNP);
      if (low == KP.end()) {
        KKKP = KP.front();
      }
      else {
        KKKP = * low;
        KP.erase(low);
      }
      if (NNNP > KKKP) {
        winP++;
      }
    }

    cout << "Case #" << T << ": ";
    cout << winC << " " << winP;
    cout << endl;
  }
}
