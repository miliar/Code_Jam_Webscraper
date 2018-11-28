#include <stdio.h>
#include <iostream>
using namespace std;
int m1[20][20], m2[20][20];
int f[20];

void check() {
  int freq2 = 0;
  for(int i=1; i<=16; i++) {
    if(f[i] == 2) {
      if (freq2 != 0) {
	cout << "Bad magician!\n";
	return;
      }
      freq2 = i;
    }
  }
  if (freq2 == 0) {
    cout << "Volunteer cheated!\n";
  } else {
    cout << freq2 << endl;
  }
}

int main () {
  int t, T, a1, a2;
  cin >> T;
  for(int t=1; t<=T; t++) {
    cin >> a1;
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++){
	cin >> m1[i][j];
      }

    cin >> a2;
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++){
	cin >> m2[i][j];
      }

    memset(f, 0, sizeof(f));
    for(int j=0; j<4; j++) {
      f[m1[a1-1][j]]++;
      f[m2[a2-1][j]]++;
    }
    cout << "Case #" << t << ": ";
    check();
  }
  return 0;
}
