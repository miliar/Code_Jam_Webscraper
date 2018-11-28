#include<iostream>
using namespace std;

int main(void){

  int buf[4];
  int fir[4];
  int sec[4];
  int row;
  int ans;

  int Case;
  cin >> Case;

  for(int i=1;i<=Case;i++){

    cin >> row;
    for(int j=1;j<=4;j++){
      if(j == row){
	for(int k=0;k<4;k++) cin >> fir[k];
      }else{
	for(int k=0;k<4;k++) cin >> buf[k];
      }
    }
    cin >> row;
    for(int j=1;j<=4;j++){
      if(j == row){
	for(int k=0;k<4;k++) cin >> sec[k];
      }else{
	for(int k=0;k<4;k++) cin >> buf[k];
      }
    }
    ans = 0;
    for(int j=0;j<4;j++){
      for(int k=0;k<4;k++){
	if(fir[j] == sec[k]){
	  if(ans == 0) ans = fir[j];
	  else if(ans != 0) ans = -1;
	  else continue;
	}
      }
    }
    cout << "Case #" << i << ": ";

    if(ans == 0){
      cout << "Volunteer cheated!" << endl;
    }else if(ans == -1){
      cout << "Bad magician!" << endl;
    }else{
      cout << ans << endl;
    }

  }
}
