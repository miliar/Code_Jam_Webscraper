#include <iostream>

using namespace std;

int main(){
  int t, a1, a2;
  t = a1 = a2 = 0;
  int m1[4][4];
  int m2[4][4];
  cin>>t;
  for(int l = 1; l<=t; l++){
    cin>>a1;
    int card = 0;
    for(int i = 0; i< 4; i++){
      for(int j = 0; j < 4; j++){
        cin>>m1[i][j];
      }
    }
    cin>>a2;
    for(int i = 0; i< 4; i++){
      for(int j = 0; j < 4; j++){
        cin>>m2[i][j];
      }
    }
    for(int k1 = 0; k1<4;k1++){
      for(int k2 = 0; k2 < 4; k2++){
        if(m1[a1-1][k1] == m2[a2-1][k2]){
          if(card == 0) card = m1[a1-1][k1];
          else card = -1;
        }
      }
    }
    if(card > 0) cout << "Case #"<<l<<": "<<card<<endl;
    else if(card == -1) cout << "Case #"<<l<<": Bad magician!"<<endl;
    else cout << "Case #"<<l<<": Volunteer cheated!"<<endl;
  }
  return 0;
}