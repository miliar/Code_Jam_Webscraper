#include <iostream>
#include <vector>
using namespace std;

int main() {
  int cases=0;
  cin >> cases;
  int casenum=0;
  while (casenum < cases) {
    casenum++;
    int row1=0;
    vector<int> candidates;
    candidates.assign(17,0);
    vector<int> winners;
    cin >> row1;
    int card=0;
    for (int i=1; i<=4; i++) {
      for (int j=1; j<=4; j++) {
       cin >> card;
       if (i==row1) candidates[card]=1;
      }
    }
    int row2=0;
    cin >> row2;
    for (int i=1; i<=4; i++) {
      for (int j=1; j<=4; j++) {
        cin >> card;
        if (i==row2 && candidates[card]==1) winners.push_back(card);
      }
    }
    cout << "Case #" << casenum << ": ";
    switch (winners.size()) {
      case 0:
        cout << "Volunteer cheated!" << endl;
        break;
      case 1:
        cout << winners[0] << endl;
        break;
      default:
        cout << "Bad magician!" << endl;
        break;
    }
  }
  return 0;
}

