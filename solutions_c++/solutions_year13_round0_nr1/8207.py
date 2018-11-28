#include <iostream> 
#include <string>

#define row1 0b1111
#define row2 0b11110000
#define row3 0b111100000000
#define row4 0b1111000000000000
#define col1 0b0001000100010001
#define col2 0b0010001000100010
#define col3 0b0100010001000100
#define col4  0b1000100010001000
#define singrow 0b1111
#define singcol 0b1
#define diag1 0b0001001001001000
#define diag2 0b1000010000100001
using namespace std;
int solve();
int main(){
  int T;
  cin>>T;
  string res[4] ={"X won","O won","Draw","Game has not completed"};
  for (int i = 0; i < T; ++i){

    cout<<"Case #"<<i+1<<": "<<res[solve()]<<endl; 
    //    cout<<"Case #"<<i<<": "<<solve()<<endl; 
  }
}
int solve(){
  int T=0,X=0,O=0; 
  string row;
  for (int i = 0; i < 4; ++i){
    cin>>row;
    for (int j = 0; j < 4; ++j){
      if (row[j] == 'X'){
	X|=(1<<(4*i+j));
      }
      else if(row[j] == 'O'){
	O|=(1<<(4*i+j));
      }
      else if( row[j] == 'T'){
	T|=(1<<(4*i+j));
      }
    }
  }
  bool winlose[3] = {false,false,false};
  int temp = 0;
  for (int i = 0; i < 4; ++i){
    if (((T|X)&(singrow<<(4*i))) == singrow<<(4*i)){
      winlose[0]|=true;
    }
    if (((T|O)&(singrow<<(4*i))) == singrow<<(4*i)){
      winlose[1]|=true;
    }
    temp = 1<<i;
    for(int j = 0; j < 3; ++j){
      temp=(temp<<(4))|temp;
    }
    if(((T|X)&temp) == temp){
      winlose[0]|=true;
    }
    if(((T|O)&temp) == temp){
      winlose[1]|=true;
    }
    
  }
  if(((T|O|X) ^ (1<<16)-1) == 0){
      winlose[2] = true;
  }
  if(((T|X) ^ diag1) == 0 ||((T|X)^diag2) == 0){
    winlose[0] = true; 
  }
  if(((T|O) ^ diag1) == 0 ||((T|O)^diag2) == 0){
    winlose[1] = true; 
  }
  for (int i = 0; i < 3; ++i){
    if(winlose[i])
      return i; 
  }
  return 3; 
}


