#include <iostream>
#include <cmath>

using namespace std;

bool checkFaS(int num){
  int digit[100];
  int i,maxk;
  int oldnum = num;
  for(i=1;;i++){
    digit[i] = num % 10;
    num /= 10;
    if(num == 0){
      break;
    }
  }
  
  maxk = (i+1)/2;
  for(int k=i;k>i-maxk;k--){
    if(digit[k] != oldnum%10){
      return false;
    }
    else{
      oldnum /=10;
    }
  }
  return true;

}

int main(){
  int loop;
  int from,endnum;
  int ans;
  cin >> loop;
  for(int i=0;i<loop;i++){
    cin >> from >> endnum;
    int rfrom = sqrt(from);
    if(rfrom*rfrom != from){
      ++rfrom;
    }
    int rendnum = sqrt(endnum);
    //cout << rfrom << " " << rendnum << endl;
    ans = 0;
    for(int number=rfrom;number<=rendnum;number++){
      if(checkFaS(number)){
	if(checkFaS(number * number)){
	  //	  cout << number << endl;
	  ++ans;
	}
	//	cout << number << " is F" << endl;
      }
    }

    cout << "Case #" << i+1 << ": ";
    cout << ans << endl;
    
  }
}
