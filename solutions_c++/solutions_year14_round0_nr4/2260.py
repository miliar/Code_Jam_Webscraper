#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int scoreForNaomiNormal(vector<double>*& naomi, vector<double>*& ken) {
  int result = naomi->size();
  vector<double>::iterator kitr = ken->begin();
  bool kend = false;
  for(vector<double>::iterator nitr = naomi->begin(); nitr != naomi->end(); nitr++){
    while(*kitr < *nitr) {
      kitr++;
      if (kitr == ken->end()) {
	kend = true;
	break;
      }
    }
    if (kend)
      break;
    kitr++;
    result--;
    if (kitr == ken->end()) {
      kend = true;
      break;
    }
  }
  return result;
}

int scoreForNaomiDeceit(vector<double>*& naomi, vector<double>*& ken) {
  return naomi->size() - scoreForNaomiNormal(ken, naomi);
}

int main() {
  int cases; 
  cin >> cases;
  for(int i = 0; i < cases; i++) {
    int count;
    cin >> count;
    vector<vector<double>*>* allblocks = new vector<vector<double>*>; 
    for(int j = 0; j < 2; j++) {
      vector<double>* player = new vector<double>;
      for(int k = 0; k < count; k++) {
	double mass;
	cin >> mass;
	player->push_back(mass);
      }
      sort(player->begin(), player->end());
      allblocks->push_back(player);
    }
    int normalr = scoreForNaomiNormal(allblocks->at(0), allblocks->at(1));
    int deceitr = scoreForNaomiDeceit(allblocks->at(0), allblocks->at(1));
    cout << "Case #" << i+1 << ": " << deceitr << " " << normalr << endl;
    delete allblocks;
  }
  return 0;
}
