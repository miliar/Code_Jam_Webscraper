#include<iostream>
#include <string>
using namespace std;

int main(){
  int cases = 0;
  cin >> cases;
  for(int i = 0; i < cases; i++){
    string current;
    cin >> current;
    string output;
    char last = current[0];
    output += last;
    for(int j = 1; j < current.length(); j++){
      if(current[j] >= output[0]){
        output.insert(0, 1,current[j]);
      }else{
        output += current[j];
      }
      last = current[j];
    }
    cout << "Case #" << i + 1 << ": " << output << endl;
  }
  return 0;
}
