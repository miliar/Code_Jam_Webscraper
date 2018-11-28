#include <iostream>
#include <vector>
using namespace std;
typedef vector <vector <int> > M;
int main() {
  int cases;
  int case_num = 0;
  int count = 0;
  cin >> cases;
  while (cases != 0) {
    count = 0;
    int answer1, answer2;
    M card_grid1(4, vector <int>(4,0));
    M card_grid2(4, vector <int>(4,0));
    int save = 0;
    cin >> answer1;
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) cin >> card_grid1[i][j];
    cin >> answer2;
    for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) cin >> card_grid2[i][j];
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
	if (card_grid1[answer1 - 1][i] == card_grid2[answer2 - 1][j]) {
	  if (count == 0) save = card_grid1[answer1 - 1][i];
	  count++;
	}
      }
    }
    case_num++;
    cout << "Case #";
    cout << case_num;
    cout << ": ";
    if (count == 1) cout << save;
    if (count  > 1) cout << "Bad magician!";
    if (count == 0) cout << "Volunteer cheated!"; 
    cout << endl;
    count = 0;
    cases--;
  }
}