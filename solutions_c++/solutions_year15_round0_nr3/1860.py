#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int table[5][5];
void form_table(void){
  for (int i = 1; i <= 4; i++) table[i][1] = i;
  for (int i = 1; i <= 4; i++) table[1][i] = i;
  for (int i = 2; i <= 4; i++) table[i][i] = -1;
  
  table[3][2] = -4; table[2][3] = 4;
  table[4][2] = 3; table[2][4] = -3;
  table[4][3] = -2; table[3][4] = 2;
}

int main(){
  int t;
  cin >> t;
  form_table();
  for (int idx = 1; idx <= t; idx++){
    int l, x;
    cin >> l >> x;
    string s; 
    cin >> s;
    string str = "";
    for (int i = 0; i < x; i++) str += s;

    int curr = 1; int pos = 1; int stage = 0;
    bool found = false;
    for (int i = 0; i < (l * x); i++){
      int nxt = (int) str[i] - 'g';
      curr = table[curr][nxt];
      if (curr < 0) {
	curr = abs(curr);
	pos = 1 - pos;
      }
      //      cout << str[i] << " " << nxt << " " << curr << " " << pos << endl;
      if (stage == 0){
	if (curr == 2 && pos == 1) {
	  stage = 1;
	  curr = 1;
	}
      } else if (stage == 1){
	if (curr == 3 && pos == 1) {
	  stage = 2;
	  curr = 1;
	}
      } else if (stage == 2){
	if (curr == 4 && pos == 1 && i == (l*x) - 1) found = true;
      }
    }
    cout << "Case #" << idx << ": ";
    if (found) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
  return 0;
}
