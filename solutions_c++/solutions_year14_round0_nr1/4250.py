#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int row;
    cin >> row;
    int cards[4];
    for(int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
	int aux;
	cin >> aux;
	if (i == row - 1) {
	  cards[j] = aux;
	}
      }
    }
    cin >> row;
    int possible_cards = 0;
    int card = 0;
    for(int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
	int aux;
	cin >> aux;
	if (i == row - 1) {
	  for (int k = 0; k < 4; ++k) {
	    if (cards[k] == aux) {
	      ++possible_cards;
	      card = aux;
	    }
	  }
	}
      }
    }
    cout << "Case #" << cas << ": ";
    if (possible_cards == 0) cout << "Volunteer cheated!" << endl;
    else if (possible_cards == 1) cout << card << endl;
    else cout << "Bad magician!" << endl;
  }
}