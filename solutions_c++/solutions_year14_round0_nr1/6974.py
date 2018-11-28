#include <iostream>

using namespace std;

void solve(int c) {
  int picked[16];
  
  for (int p = 0; p < 16; p++)
    picked[p] = 0;

  int r1; cin >> r1;
  
  for (int i = 0; i < 16; i++) {
    int c; cin >> c;
    int cr = i / 4 + 1;
    if (cr == r1) picked[c - 1]++;
  }

  int r2; cin >> r2;
  
  for (int i = 0; i < 16; i++) {
    int c; cin >> c;
    int cr = i / 4 + 1;
    if (cr == r2) picked[c - 1]++;
  }

  int selected = -1;


  for (int p = 0; p < 16; p++) {
    if (picked[p] == 2 && selected == -1)
      selected = p;
    else if (picked[p] == 2) {
      selected = -2;
      break;
    }
  }

  cout << "Case #" << c << ": "; 
  if (selected == -1)
    cout << "Volunteer cheated!" << endl;
  else if (selected == -2) 
    cout << "Bad magician!" << endl;
  else cout << selected + 1 << endl;

}

int main() {
  int t; cin >> t;
  
  for (int i = 1; i <= t; i++) solve(i);
}
