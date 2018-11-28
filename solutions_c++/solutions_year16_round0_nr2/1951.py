#include <iostream>
#include <string>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    string tmp;
    cin >> tmp;
    string pancakes = tmp + '+';
    char last = pancakes[0]; 
    int ret = 0;
    for(int i = 0; i < pancakes.size(); i++){
      if (pancakes[i] != last){
        ret ++;
        if(last == '+'){
          last = '-';
        } else {
          last = '+';
        }
      }
    }
    
    cout << "Case #" << i + 1 << ": " << ret << endl;
  }
}

