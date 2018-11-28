#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {

  int n;
  cin >> n;
  for (int i = 0; i< n; i++) {
    int row1;
    cin >> row1;
    int b1[4][4];
    for (int j=0;j<4;j++) {
      for (int k=0;k<4;k++) {
	cin >> b1[j][k];
      }
    }
    int row2;
    cin >> row2;
    int b2[4][4];
    for (int j=0;j<4;j++) {
      for (int k=0;k<4;k++) {
	cin >> b2[j][k];
      }
    }
    vector<bool> pos_cards;
    pos_cards.resize(17,false);
    for (int j=0;j<4;j++) {
      pos_cards[b1[row1-1][j]]=true;
    }
    vector<bool> pos_cards2;
    pos_cards2.resize(17,false);
    for (int j=0;j<4;j++) {
      //cout << b2[row2-1][j] << endl;
      pos_cards2[b2[row2-1][j]] = true;
    }
    int c = 0;
    int last = 0;
    for (int j=1;j<17;j++) {
      // Count the number of both true;
      if (pos_cards[j]&&pos_cards2[j]) {
	c++;
	last = j;
      }
    }
    cout << "Case #"<<i+1<<": ";
    if (c==1) {
      cout << last << endl;
    } else {
      if (c==0) {
	cout << "Volunteer cheated!" << endl;
      } else {
	cout << "Bad magician!" << endl;
      }
    }
  }
}

    
