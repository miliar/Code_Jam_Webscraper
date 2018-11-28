#include <iostream>
#include <fstream>
using namespace std;

int main(){
  int cases, cur;
  string output;
  cin >> cases;

  for(int i = 0; i < cases; i++){
    cin >> cur;
    if (cur == 0){cout << "Case #" << i+1 << ": INSOMNIA" <<endl; continue;}
    int digits = 0, copy;
    int numbers[10] = {0};
    for(int j = 1; digits != 10; j++){
      copy = cur*j;
      int dcopy = copy;
      while(dcopy){
        if(!numbers[dcopy % 10]){
          digits++;
          numbers[dcopy % 10] = 1;
        }
        dcopy /= 10;
      }
    }
    cout << "Case #" << i+1 << ": " << copy << endl;
  }
  return 0;
}
