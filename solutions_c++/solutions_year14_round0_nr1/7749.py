#include <iostream>

using namespace std;

#define GOOD 0
#define BAD -1
#define CHEAT -2

int main(){
  int num_case;
  cin>>num_case;

  int i,j,p;
  int guess1,guess2;
  int card1[4][4], card2[4][4];
  int status[100];
  
  for(i=0;i<num_case;i++){
    cin >> guess1;
    for(j=0;j<4;j++){
      for(p=0;p<4;p++){
	cin>>card1[j][p];
      }
    }
    cin >> guess2;
    for(j=0;j<4;j++){
      for(p=0;p<4;p++){
	cin>>card2[j][p];
      }
    }

    // determine 
    int num_com = 0;
    int comm = 0;
    for(j=0;j<4;j++){
      for(p=0;p<4;p++){
	if(card1[guess1-1][j] == card2[guess2-1][p]){
	  comm = card2[guess2-1][p];
	  num_com++;
	}
      }
    }
    if(num_com == 1){
      // GOOD
      status[i] = comm;
    }
    else if(num_com >= 2){
      // BAD
      status[i] = BAD;
    }
    else if(num_com == 0){
      // CHEAT
      status[i] = CHEAT;
    }

  }


  for(i=0;i<num_case;i++){
    cout<<"Case #"<<i+1<<": ";
    if(status[i] > 0){
      cout<<status[i];
    }
    else if(status[i] == BAD){
      cout<<"Bad magician!";
    }
    else if(status[i] == CHEAT){
      cout<<"Volunteer cheated!";
    }
    cout<<endl;
  }
  return 0;
}
