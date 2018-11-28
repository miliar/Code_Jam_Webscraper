#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector< vector<int> > cards;
vector<int> first, second;

int main(int argc, char*argv[]) {
  ifstream file (argv[1]);

  cards.resize(4);
  for (int i = 0; i < cards.size(); i++) {
    cards.at(i).resize(4);
  }

  if (file.is_open()) {
    int N, C, D, tmp;
    file >> N;

    for (int i = 0; i < N; i++) {
      D = -1;
      first.clear();
      second.clear();

      // Read in row number
      file >> C;

      // Read in cards
      for (int j = 0; j < 4; j++) {
        for (int k = 0; k < 4; k++) {
          file >> tmp;
          cards.at(j).at(k) = tmp;
        }
      }

      // Get Row
      first = cards.at(C-1);

      // Read in row number
      file >> C;

      // Read in cards
      for (int j = 0; j < 4; j++) {
        for (int k = 0; k < 4; k++) {
          file >> tmp;
          cards.at(j).at(k) = tmp;
        }
      }

      // Get Row
      second = cards.at(C-1);


      for (int l = 0; l < first.size(); l++) {
        vector<int>::iterator pos = find(second.begin(), second.end(), first.at(l));
        if( pos != second.end() ){
          D = first.at(l);
          second.erase(pos);
        }
      }

      if (first.size() - second.size() == 1) {
        cout << "Case #" << i+1 << ": " << D << endl;
      } else if (D != -1) {
        cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
      } else {
        cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
      }
    }
  }
}
