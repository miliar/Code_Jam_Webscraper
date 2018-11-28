#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int warOptimal(vector<double> naomi, vector<double> ken) {
  int result = 0;

  for (int i = naomi.size()-1; i >= 0; --i) {
    double nt = naomi[i];
    int kc = -1;
    for (int k = 0; k < ken.size(); ++k) {
      if (nt < ken[k]) {
        kc = k;
        break;
      }
    }
    kc = max(kc, 0);
    result += (nt > ken[kc]);
    ken.erase(ken.begin()+kc);
  }

  return result;
}

bool pairwisebigger(const vector<double>& a, const vector<double>& b) {
  for (int i = 0; i < a.size(); ++i) {
    if (a[i] < b[i]) return false;
  }
  return true;
}

int deceitfulWar(vector<double> naomi, vector<double> ken) {
  int result = 0;

  if (naomi.size() == 1)
    return naomi[0] > ken[0];

  int cnt = 1;
  while (!naomi.empty() && !pairwisebigger(naomi, ken)) {
    naomi.erase(naomi.begin());
    ken.pop_back();
/*    cout << "after move "<< cnt <<":"<<endl;
    cout << "nao: ";
    for (int i = 0; i < naomi.size(); ++i)
      cout << naomi[i] << " ";
    cout << endl;
    cout << "ken: ";
    for (int i = 0; i < ken.size(); ++i)
      cout << ken[i] << " ";
    cout << endl;*/
  }

  return naomi.size();
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    int N;
    cin >> N;

    vector<double> naomi(N, 0);
    vector<double> ken(N, 0);
    int y = 0, z = 0;

    for (int i = 0; i < N; ++i)
      cin >> naomi[i];
    for (int i = 0; i < N; ++i)
      cin >> ken[i];

    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());

/*    cout << "nao: ";
    for (int i = 0; i < naomi.size(); ++i)
      cout << naomi[i] << " ";
    cout << endl;
    cout << "ken: ";
    for (int i = 0; i < ken.size(); ++i)
      cout << ken[i] << " ";
    cout << endl;*/


    z = warOptimal(naomi, ken);
    y = deceitfulWar(naomi, ken);


    cout << "Case #" << test << ": " << y << " " << z << endl; 
  }
}
