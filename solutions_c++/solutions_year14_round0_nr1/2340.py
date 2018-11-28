#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int T;


int main() {

  ifstream fin("A-small-attempt0.in");
  ofstream fout("A-small-attempt0.out");

  fin >> T;

  for (int t = 0; t < T; t++) {
    set<int> possibles;
    possibles.clear();

    int answer, input, num_cards = 0, card_found = -1;
    fin >> answer;
    for (int i = 1; i < answer; i++) {
      fin >> input >> input >> input >> input;
    }
    for (int i = 0; i < 4; i++) {
      fin >> input;
      possibles.insert(input);
    }
    for (int i = answer+1; i <= 4; i++) {
      fin >> input >> input >> input >> input;
    }

    fin >> answer;

    for (int i = 1; i < answer; i++) {
      fin >> input >> input >> input >> input;
    }
    for (int i = 0; i < 4; i++) {
      fin >> input;
      if (possibles.find(input) != possibles.end()) {
        num_cards++;
        card_found = *possibles.find(input);
      }
    }
    for (int i = answer+1; i <= 4; i++) {
      fin >> input >> input >> input >> input;
    }

    fout << "Case #" << t+1 << ": ";

    if (num_cards == 1) {
      fout << card_found << endl;
    } else if (num_cards > 1) {
      fout << "Bad magician!" << endl;
    } else {
      fout << "Volunteer cheated!" << endl;
    }
  }

  return 0;
}
