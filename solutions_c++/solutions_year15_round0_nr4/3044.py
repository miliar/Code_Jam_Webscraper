#include<iostream>
#include<vector>
using namespace std;

int main(){
  int t;
  cin >> t;
  for(int test=1;test<=t;test++){
    int x,r,c;
    cin >> x >> r >> c;
    if(x==1){
      cout << "Case #" << test << ": " << "GABRIEL" << endl;
      continue;
    }
    if(x==2){
      if(r%2==0||c%2==0){
	cout << "Case #" << test << ": " << "GABRIEL" << endl;
	continue;
      }
      
	cout << "Case #" << test << ": " << "RICHARD" << endl;;
      continue;
    }
    if(x==3){
      if((r==2&&c==3)||(r==3&&c==2)||(r==3&&c==3)||(r==4&&c==3)||(r==3&&c==4)){
	cout << "Case #" << test << ": " << "GABRIEL" << endl;
	continue;
      }
      
	cout << "Case #" << test << ": " << "RICHARD" << endl;;
      continue;
    }
    if(x==4){
      if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4)){
	cout << "Case #" << test << ": " << "GABRIEL" << endl;
	continue;
      }
      
	cout << "Case #" << test << ": " << "RICHARD" << endl;;
      continue;
    }
  }
  return 0;
}