#include <iostream>
using namespace std;

int main(void){
  int t;
  cin >> t;
  for(int i=0; i < t; i++){
    int a1, a2;
    cin >> a1;
    int row1[4], row2[4], discard;

    for(int x=1; x<=4; x++){
      for(int y=0; y<4; y++){
        if (x!=a1){ cin >> discard; }
        else{ cin >> row1[y]; }
      }
    }

    cin >> a2;
    for(int x=1; x<=4; x++){
      for(int y=0; y<4; y++){
        if (x!=a2){ cin >> discard; }
        else{ cin >> row2[y]; }
      }
    }

    int answer=0, found=0;
    for(int x=0; x<4; x++){
      for(int y=0; y<4; y++){
        if (row1[x] == row2[y]){ 
          found++;
          answer = row1[x]; 
        }
      }
    }
    cout << "Case #" << i+1 << ": ";
    
    if(answer == 0){
      cout << "Volunteer cheated!";
    } else if (found > 1) {
      cout << "Bad magician!";
    } else {
      cout << answer;
    }
    cout << endl;

  }
  return 1;
}

