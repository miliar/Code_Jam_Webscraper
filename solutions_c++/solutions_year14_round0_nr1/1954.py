#include<iostream>

using namespace std;

int main(){
  int pn;
  cin >> pn;
  for(int k = 0; k < pn; k++){
    int n1, n2;
    int temp;
    int ans[4] = {};
    cin >> n1;
    for(int i = 0; i < 4; i++){
      for(int j = 0; j < 4; j++){
	cin >> temp;
	if(i == n1-1)      ans[j] = temp;
      }
    }
    int equal = 0, num = 0;
    cin >> n2;
    for(int i = 0; i < 4; i++){
      for(int j = 0; j < 4; j++){
	cin >> temp;
	if(i == n2-1){
	  for(int ii = 0; ii < 4; ii++){
	    if(ans[ii] == temp){
	      equal++;
	      num = temp;
	    }
	  }
	}
      }
    }
    cout << "Case #" << k+1 << ": ";
    if(equal == 0)    cout << "Volunteer cheated!" << endl;
    else if(equal == 1)    cout << num << endl;
    else               cout << "Bad magician!" << endl;
  }
  return 0;
}
