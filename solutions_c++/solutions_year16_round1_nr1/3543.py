#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
  long t, counter = 0;
  cin >> t;
  string input;
  while(t--){
    counter++;
    cin >> input;
    string current = "";
    for(long i = 0;i < input.length();i++){
      if(i == 0){
        current = current + input[i];
      }
      else{
        if(current[i - 1] > input[i]){
          current += input[i];
        }
        else{
          string before(1, input[i]);
          string temp;
          if(current[0] > input[i]){
            temp = current + before;
          }
          else{
            temp = before + current;
          }
          current = temp;
        }
      }
    }
    cout << "Case #" << counter << ": " << current << endl;
  }
  return 0;
}
