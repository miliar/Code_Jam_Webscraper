#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  
  for(int t=0; t<T; t++) {
    int r, tmp;
    int rowA[4];
    int rowB[4];
    
    cin >> r;

    for(int i=1; i<=4; i++) {
      if(i==r) {
        cin >> rowA[0] >> rowA[1] >> rowA[2] >> rowA[3];
      } else {
        cin >> tmp >> tmp >> tmp >> tmp;
      }
    }

    cin >> r;

    for(int i=1; i<=4; i++) {
      if(i==r) {
        cin >> rowB[0] >> rowB[1] >> rowB[2] >> rowB[3];
      } else {
        cin >> tmp >> tmp >> tmp >> tmp;
      }
    }

    int m=0;
    int n;
    for(int i=0; i<4; i++) {
      for(int j=0; j<4; j++) {
        if(rowA[i] == rowB[j]) {
          n=rowA[i];
          m++;
        }
      }
    }

    cout << "Case #" << (t+1) << ": ";
    if(m==0) cout << "Volunteer cheated!";
    else if(m==1) cout << n;
    else cout << "Bad magician!";
    cout << endl;
  }

  return 0;
}
