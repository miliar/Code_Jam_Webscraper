#include <iostream>
#include <string>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=1; t<=T; ++t){
    int max;
    string line;
    cin >> max;
    cin >> line;
    int needed = 0;
    int standing = 0;
    for(int i=0; i<=max; ++i){
      if(line[i]!='0'){
        if(standing < i){
          needed += i - standing;
          standing = i;
        }
        standing += stoi(line.substr(i,1));
      }
    }
    
    cout << "Case #" << t << ": " << needed << endl;
  }
}
