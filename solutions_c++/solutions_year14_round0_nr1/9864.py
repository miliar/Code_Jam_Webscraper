#include<iostream>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  
  for(int t = 1; t <= T; t++) {
    int fir, sec;
    cin >> fir;
    int ar1[4][4];
    int ar2[4][4];
    for(int i = 0; i < 4; i++) {
      for(int j =0; j < 4; j++) {
        cin >> ar1[i][j];
      }
    }
    cin >> sec;
    for(int i = 0; i < 4; i++) {
      for(int j =0; j < 4; j++) {
        cin >> ar2[i][j];
      }
    }
    vector<int> ans;
    for(int j = 0; j < 4; j++) {
    for(int i = 0; i < 4; i++) {
      if(ar1[fir-1][j] == ar2[sec-1][i]) {
        ans.push_back(ar1[fir-1][j]);
      }
    }
    }
    cout << "Case #" << t << ": ";
    switch (ans.size()){
      case 0: cout << "Volunteer cheated!" << endl; break;
      case 1: cout << ans[0] << endl; break;
      default: cout << "Bad magician!" << endl; break;
    }
  }

}
