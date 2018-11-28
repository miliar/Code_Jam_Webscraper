#include<iostream>
#include<fstream>
using namespace std;

void countdigits(int x, bool[]);
bool somefalse(bool[], int n);


int main(){
  int numIn;
  ifstream ifs;
  ifs.open("s2.txt");
  ifs >> numIn;
  //  cout << numIn;
  for(int i = 0; i < numIn; i++){
    //cout <<i+1 << endl;
    int currIn;
    ifs >> currIn;
    //cout << currIn << endl;
    if (currIn == 0){
      cout << "Case #" << i+1 << ": INSOMNIA" <<endl;
    }
    else{
      bool digits[10];
      for(int j = 0; j < 10; j++){
        digits[j] = false;
      }
      int temp = currIn;
      countdigits(temp, digits);
      for (int j = 1; somefalse(digits, 10); j++){
        temp = j * currIn;
        countdigits(temp, digits);
      }
      cout << "Case #" << i+1 << ": "<< temp <<endl;
      }
  }
}

void countdigits(int x, bool digits[]){
  while(x > 0){
    int r = x %10;
    digits[r] = true;
    x = x/10;
  }
}

bool somefalse(bool digits[], int n){
  for (int i = 0; i < n; i++){
    if (digits[i] == false)
      return true;
  }
  return false;
}
