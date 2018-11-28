#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int deceitful(vector<double> nao, vector<double> ken) {
  int score = 0;
  
  while (!nao.empty()) {
    for (int i = 0; i < nao.size(); ++i) {
      //cout << nao[i] << " ";
    }
    //cout << endl;
    for (int i = 0; i < ken.size(); ++i) {
      //cout << ken[i] << " ";
    }
    vector<double>::iterator naochosen = nao.begin();
    while (naochosen != nao.end() && *naochosen < *ken.begin()) {
      ++naochosen;
    }
    if (naochosen != nao.end()) {
      ++score;
      nao.erase(naochosen);
      ken.erase(ken.begin());
    } else {
      nao.erase(nao.begin());
      ken.erase(ken.begin());
    }
  }
  return score;
}

int honest(vector<double> nao, vector<double> ken) {
  int score = 0;
  
  while(!nao.empty()) {
  
  vector<double>::iterator kenchosen = ken.begin();
  
  while (kenchosen != ken.end() && *kenchosen < *nao.begin()) {
    ++kenchosen;
  }
  if (kenchosen != ken.end()) {
    ken.erase(kenchosen);
    nao.erase(nao.begin());
  } else {
    ++score;
    ken.erase(ken.begin());
    nao.erase(nao.begin());
  }
  }
  
  return score;
}

int main() {
  int ncases;
  cin >> ncases;
  
  for (int test = 0; test < ncases; ++test) {
    int nblocks;
    cin >> nblocks;
    vector<double> nao;
    for (int i = 0; i < nblocks; ++i) {
      double val;
      cin >> val;
      nao.push_back(val);
    }
    sort(nao.begin(), nao.end());
    vector<double> ken;
    for (int i = 0; i < nblocks; ++i) {
      double val;
      cin >> val;
      ken.push_back(val);
    }
    sort(ken.begin(), ken.end());
    cout << "Case #" << test + 1 << ": "
      << deceitful(nao, ken) << " " << honest(nao, ken) << endl;
  }
  
  return 0;
}
