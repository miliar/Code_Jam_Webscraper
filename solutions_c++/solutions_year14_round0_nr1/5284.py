#include <iostream>
#include <sstream>
#include <string>
#include <list>
 
using namespace std;
 
class qa {
 public:
  qa() {
  }

  ostringstream convert;

  string solve() {

    list<int> L1, L2;

    for (int m=0; m<4; m++) {
      L1.push_back(cards[0][answer[0]-1][m]);
      L2.push_back(cards[1][answer[1]-1][m]);
    }

    list<int>::iterator i,j;

    int sol_cnt = 0;
    int sol = -1;
    for(i=L1.begin(); i!=L1.end(); i++) {
      for(j=L2.begin(); j!=L2.end(); j++) {
        if (*i == *j) {
          sol_cnt++;
          sol = *i;
        }
      }
    }

    if (sol_cnt == 0)
      return "Volunteer cheated!";
    else if (sol_cnt == 1) {
      convert << sol;
      return convert.str();
    }
    else
      return "Bad magician!";
  }

  int answer[2];
  int cards[2][4][4];

};
 
int main (void) {
  int n, T;

  cin >> T;

  for (n=1; n<=T; n++) {
    qa *solver = new qa();

    for (int m=0; m<2; m++) {
      cin >> solver->answer[m];
      cin >> solver->cards[m][0][0] >> solver->cards[m][0][1] >> solver->cards[m][0][2] >> solver->cards[m][0][3];
      cin >> solver->cards[m][1][0] >> solver->cards[m][1][1] >> solver->cards[m][1][2] >> solver->cards[m][1][3];
      cin >> solver->cards[m][2][0] >> solver->cards[m][2][1] >> solver->cards[m][2][2] >> solver->cards[m][2][3];
      cin >> solver->cards[m][3][0] >> solver->cards[m][3][1] >> solver->cards[m][3][2] >> solver->cards[m][3][3];
    }
    cout << "Case #" << n << ": " << solver->solve() << endl;
  }

  return 0;
}
